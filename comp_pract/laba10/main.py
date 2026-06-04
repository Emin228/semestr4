from io import BytesIO

from fastapi import FastAPI, Form, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw, ImageFont


app = FastAPI()

templates = Jinja2Templates(directory="templates")

AUTHOR_LOGIN = "155291"

MIN_SIZE = 10
MAX_SIZE = 2000


@app.get("/login")
def login():
    return {"author": AUTHOR_LOGIN}


@app.get("/makeimage")
def makeimage_get(request: Request):
    return templates.TemplateResponse(
        "makeimage.html",
        {
            "request": request,
            "message": ""
        }
    )


def parse_size(value: str) -> int | None:
    try:
        number = int(value)
    except ValueError:
        return None

    if number < MIN_SIZE or number > MAX_SIZE:
        return None

    return number


@app.post("/makeimage")
async def makeimage_post(
    request: Request,
    width: str = Form(...),
    height: str = Form(...),
    text: str = Form("")
):
    image_width = parse_size(width)
    image_height = parse_size(height)

    if image_width is None or image_height is None:
        return templates.TemplateResponse(
            "makeimage.html",
            {
                "request": request,
                "message": "Invalid image size"
            }
        )

    image = Image.new(
        mode="RGB",
        size=(image_width, image_height),
        color=(230, 230, 230)
    )

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2

    draw.text(
        (x, y),
        text,
        fill=(0, 0, 0),
        font=font
    )

    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg",
        headers={
            "Content-Disposition": "inline; filename=generated.jpg"
        }
    )