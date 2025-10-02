from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('portof.html')

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    return f"Bem-vindo, {nome}!"

if __name__ == "__main__":
    app.run(debug=True)