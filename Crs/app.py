from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

model = keras.models.load_model("models/my_model")
x = np.zeros(9)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test1.html', name='Для анализа введите r')

def processing_params(param1, param2, param3, param4, param5, param6, param7, param8, param9 ):
    x[0]=param1
    x[1]=param2
    x[2]=param3
    x[3]=param4
    x[4]=param5
    x[5]=param6
    x[6]=param7
    x[7]=param8
    x[8]=param9
    pred = model.predict(x).flatten()
    message = f"Соотношение матрица-наполнитель = {pred}"
    return message


@app.route('/r/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        param1 = request.form.get('param1')  # запрос к данным формы
        param2 = request.form.get('param2')
        param3 = request.form.get('param3')
        param4 = request.form.get('param4')
        param5 = request.form.get('param5')
        param6 = request.form.get('param6')
        param7 = request.form.get('param7')
        param8 = request.form.get('param8')
        param9 = request.form.get('param9')

        param1 = float(param1)
        param2 = float(param2)
        param3 = float(param3)
        param4 = float(param4)
        param5 = float(param5)
        param6 = float(param6)
        param7 = float(param7)
        param8 = float(param8)
        param9 = float(param9)

        message = processing_params(param1, param2, param3, param4, param5, param6, param7, param8, param9)

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run()
