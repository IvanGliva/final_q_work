
from flask import Flask
from flask import request
from flask import render_template
# импорт библиотек для модели
from sklearn.ensemble import RandomForestRegressor
import pickle

# восстановление модели
ForestRegressor_model = RandomForestRegressor(n_estimators=100, min_samples_leaf=1, min_samples_split=2, max_depth=10,
                                              random_state=10)
pkl_filename = './model/RandomForestRegressor_model.pkl'

# загрузка модели
with open(pkl_filename, 'rb') as file:
    ForestRegressor_model = pickle.load(file)

app = Flask(__name__)

#функция прогнозирования значений
def prognoz(x1, x2, x3, x4):
    y_prognoz = ForestRegressor_model.predict([[x1, x2, x3, x4]])
    return y_prognoz[0][0], y_prognoz[0][1]


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    messageD = ''
    messageH = ''
    if request.method == 'POST':
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get('FP')
        if IW != '' and IF != '' and VW != '' and FP != '':
            message = 'Все поля заполнены'
            x1 = int(IW)
            x2 = int(IF)
            x3 = float(VW)
            x4 = int(FP)
            y1, y2 = prognoz(x1, x2, x3, x4)
            messageD = str(y1)
            messageH = str(y2)
        else:
            message = 'Не все поля заполнены'

    return render_template('index.html', message=message, messageD=messageD, messageH=messageH)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
