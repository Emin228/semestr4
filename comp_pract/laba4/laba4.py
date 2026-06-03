from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# Логин в Moodle
MOODLE_LOGIN = "155291"

# Эндпоинт для получения логина автора
@app.route('/login', methods=['GET'])
def login():
    # Возвращаем JSON с логином автора
    return jsonify({"author": MOODLE_LOGIN})

# Эндпоинт для получения размеров PNG-изображения
@app.route('/size2json', methods=['POST'])
def size2json():
    # Проверяем, есть ли файл с ключом 'image' в запросе
    if 'image' not in request.files:
        return jsonify({"result": "invalid filetype"})

    file = request.files['image']

    try:
        # Читаем содержимое файла и открываем его как изображение
        img = Image.open(io.BytesIO(file.read()))

        # Проверяем, что формат изображения — PNG
        if img.format != "PNG":
            return jsonify({"result": "invalid filetype"})

        # Возвращаем ширину и высоту изображения в формате JSON
        return jsonify({
            "width": img.width,
            "height": img.height
        })

    except Exception:
        # В случае любой ошибки (например, повреждённый файл) возвращаем ошибку
        return jsonify({"result": "invalid filetype"})

# Запуск Flask-приложения
if __name__ == '__main__':
    app.run(debug=True)