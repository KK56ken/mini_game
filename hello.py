from hello2 import good
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello World"
    # 変更
    return render_template('test.html', title='flask test', name=name)


@app.route("/good")
def hello2():
    name = good()
    return render_template('test2.html', title='flask test', name=name)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
