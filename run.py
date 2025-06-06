from flask import Flask
from flasgger import Swagger
from app.api.routes import chat_blueprint 

app = Flask(__name__)
app.register_blueprint(chat_blueprint)
Swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
