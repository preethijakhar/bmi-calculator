from flask import Flask, request, render_template
from bmi import calculate_bmi


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi_result = calculate_bmi(weight, height)
    return render_template('index.html', bmi=bmi_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
