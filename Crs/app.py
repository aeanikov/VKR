from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World 2!!!!!!!!!!!!'


def processing_params(params):
#     TODO: Добавить логику модели
#     model = keras.load_model()
#     pred = model.predict([param1, param2])
    message = f"Параметры {params}"
    return message


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        params = request.form.get('username')

        params = list(map(float, params.split()))

        message = processing_params(params)

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
