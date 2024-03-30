from flask import Flask, url_for, request, render_template
import requests
from work_model import predict

app = Flask(__name__)


@app.route('/')
@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        print(request.form.get('addres'))
        full_sq = request.form.get('full_sq')
        life_sq = request.form.get('life_sq')
        level = request.form.get('level')
        max_floor = request.form.get('max_floor')
        material = request.form.get('material')
        build_year = request.form.get('build_year')
        num_room = request.form.get('num_room')
        kitchen_sq = request.form.get('kitch_sq')
        state = request.form.get('state')
        print("Данные получены")

        value_list = {
            'full_sq': float(full_sq),
            "life_sq": float(life_sq),
            "level": float(level),
            "max_floor": float(max_floor),
            "material": float(material),
            "build_year": float(build_year),
            "num_room": float(num_room),
            "kitchen_sq": float(kitchen_sq),
            "state": float(state)
        }
        print("Составлени список данных")
        print(value_list)

        cost = predict(value_list)
        print(cost)
        return f"Расчетная стоимость: {cost}"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
