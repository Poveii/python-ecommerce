# Importações
## É ao contrário do JavaScript kkkkkkk
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelagem
# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


# Definição de uma rota raiz (página inicial) e da função que será executada ao request.
@app.route('/teste')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
