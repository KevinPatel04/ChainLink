from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def trade():
    return render_template('trade.html')

@app.route("/vault")
def vault():
    return render_template('vault.html')

if __name__ == "__main__":
    app.run(debug=True)