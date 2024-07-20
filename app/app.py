from flask import Flask, render_template,jsonify

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categoria')
def categoria():
    return render_template('cat1.html')


if __name__ == '__main__':
    app.run(debug=True,port=5000)
    