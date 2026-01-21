from flask import Flask, render_template, request
from Home_price_predictor import predict_price


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/modals')
def modals():
    return render_template('modals.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutme.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        price = predict_price(
            int(request.form['area']),
            int(request.form['bedrooms']),
            int(request.form['bathrooms']),
            int(request.form['stories']),
            int(request.form['parking']),
            request.form['city'],
            int(request.form['age'])
        )
        return render_template('index.html', result=price)
    except Exception as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=8000)