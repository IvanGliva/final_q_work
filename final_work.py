# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
from flask import Flask
from flask import request
from flask import render_template  # , flash
# импорт библиотек для модели
# import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import os

# загрузка модели
# Load from file
ForestRegressor_model = RandomForestRegressor(n_estimators=100, min_samples_leaf=1, min_samples_split=2, max_depth=10,
                                              random_state=10)
pkl_filename = os.path.join("model", "RandomForestRegressor_model.pkl")  # './model/RandomForestRegressor_model.pkl'
pkl_filename_scaler = os.path.join("model", 'Scaler_model.pkl')

with open(pkl_filename, 'rb') as file:
    ForestRegressor_model = pickle.load(file)
with open(pkl_filename_scaler, 'rb') as file:
    Scaler_model = pickle.load(file)

app = Flask(__name__)


# app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


def prognoz(x1, x2, x3, x4):
    X_st = Scaler_model.transform ([[x1, x2, x3, x4]])
    y_prognoz = ForestRegressor_model.predict(X_st)
    return y_prognoz[0][0], y_prognoz[0][1]


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    messageD = ''
    messageH = ''
    if request.method == 'POST':
        print(request.form)
        # username = request.form.get('username')
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get('FP')
        if IW != '' and IF != '' and VW != '' and FP != '':
            message = 'Все поля заполнены'
            # flash('Все поля заполнены')
            x1 = int(IW)
            x2 = int(IF)
            x3 = float(VW)
            x4 = int(FP)
            y1, y2 = prognoz(x1, x2, x3, x4)
            messageD = str(y1)
            messageH = str(y2)
        else:
            message = 'Не все поля заполнены'
            # flash('Не все поля заполнены')
    return render_template('index.html', message=message, messageD=messageD, messageH=messageH)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
