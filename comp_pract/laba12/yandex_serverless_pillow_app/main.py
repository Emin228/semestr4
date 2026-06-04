from datetime import datetime
from io import BytesIO
import os
import re
from pathlib import Path

from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError


AUTHOR_LOGIN = os.getenv("MOODLE_LOGIN", "155291")

MIN_SIZE = 10
MAX_SIZE = 2000

IMAGE_DIR = Path(os.getenv("IMAGE_DIR", "images"))
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Yandex Serverless Pillow App")

templates = Jinja2Templates(directory="templates")

# Раздача сохранённых изображений.
app.mount("/stored", StaticFiles(directory=str(IMAGE_DIR)), name="stored")


@app.get("/login")
def login():
    return {"author": AUTHOR_LOGIN}


def render_makeimage_form(request: Request, message: str = ""):
    return templates.TemplateResponse(
        "makeimage.html",
        {
            "request": request,
            "message": message,
        },
    )


@app.get("/makeimage")
def makeimage_get(request: Request):
    return render_makeimage_form(request)


def parse_size(value: str) -> int | None:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None

    if number < MIN_SIZE or number > MAX_SIZE:
        return None

    return number


def sanitize_name(name: str) -> str:
    """
    Делает безопасное имя файла:
    - убирает расширение;
    - оставляет буквы, цифры, дефис и подчёркивание;
    - заменяет остальные символы на подчёркивание.
    """
    name = Path(name.strip()).stem
    name = re.sub(r"[^a-zA-Zа-яА-Я0-9_-]+", "_", name)
    name = name.strip("_")

    if not name:
        name = "image"

    return name


def get_unique_generated_filename() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    return f"generated_{timestamp}.jpg"


def create_image(width: int, height: int, text: str) -> Image.Image:
    image = Image.new(
        mode="RGB",
        size=(width, height),
        color=(230, 230, 230),
    )

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, fill=(0, 0, 0), font=font)

    return image


@app.post("/makeimage")
async def makeimage_post(
    request: Request,
    width: str = Form(...),
    height: str = Form(...),
    text: str = Form(""),
):
    image_width = parse_size(width)
    image_height = parse_size(height)

    if image_width is None or image_height is None:
        return render_makeimage_form(request, 'Invalid image size')

    image = create_image(image_width, image_height, text)

    # Сохраняем изображение, чтобы оно появилось на странице /images.
    filename = get_unique_generated_filename()
    saved_path = IMAGE_DIR / filename
    image.save(saved_path, format="JPEG", quality=90)

    # Возвращаем изображение напрямую браузеру.
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=90)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg",
        headers={
            "Content-Disposition": 'inline; filename="generated.jpg"',
        },
    )


def render_load_form(request: Request, message: str = ""):
    return templates.TemplateResponse(
        "load_image.html",
        {
            "request": request,
            "message": message,
        },
    )


@app.get("/load_image")
def load_image_get(request: Request):
    return render_load_form(request)


@app.post("/load_image")
async def load_image_post(
    request: Request,
    image_name: str = Form(""),
    image_file: UploadFile = File(...),
):
    if not image_file.filename:
        return render_load_form(request, "No file selected")

    if not image_name.strip():
        image_name = image_file.filename

    safe_name = sanitize_name(image_name)
    filename = f"{safe_name}.jpg"
    save_path = IMAGE_DIR / filename

    if save_path.exists():
        return render_load_form(request, "Image name already exists")

    try:
        content = await image_file.read()
        source = Image.open(BytesIO(content))
        source.verify()

        # После verify файл нужно открыть заново.
        source = Image.open(BytesIO(content)).convert("RGB")
        source.save(save_path, format="JPEG", quality=90)

    except (UnidentifiedImageError, OSError, ValueError):
        return render_load_form(request, "Invalid image file")

    return templates.TemplateResponse(
        "load_image.html",
        {
            "request": request,
            "message": f'Image "{safe_name}" uploaded successfully',
        },
    )


@app.get("/images")
def images_get(request: Request):
    images = []

    for path in sorted(IMAGE_DIR.glob("*.jpg")):
        images.append(
            {
                "name": path.stem,
                "url": f"/stored/{path.name}",
            }
        )

    return templates.TemplateResponse(
        "images.html",
        {
            "request": request,
            "images": images,
        },
    )
