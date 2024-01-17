# Importação do Flask
## É ao contrário do JavaScript kkkkkkk
from flask import Flask

app = Flask(__name__)

# Definição de uma rota raiz (página inicial) e da função que será executada ao request.
@app.route('/teste')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
