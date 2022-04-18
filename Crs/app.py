from flask import Flask, request, render_template
import numpy as np
from tensorflow import keras

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World 2!!!!!!!!!!!!'


def processing_params(params):
    message = ""
#     TODO: Добавить логику модели
# model.predict([[param1, param2, ...]])
#     model = keras.models.load_model(path) # путь до модели
#     message = f"Параметры {params}\n"
#     model.summary()
    return message


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        # TODO: добавить обработку нескольких параметров
        params = request.form.get('username')

        params = list(map(float, params.split()))

        message = processing_params(params)

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
