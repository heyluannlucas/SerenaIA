from flask import Flask
from flasgger import Swagger
from flask_cors import CORS  # 👈 importa o CORS

from app.api.routes import chat_blueprint 

app = Flask(__name__)
CORS(app)  # 👈 habilita CORS para todas as origens (incluindo Angular)

Swagger(app)
app.register_blueprint(chat_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
