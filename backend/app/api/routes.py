from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.core.responder import gerar_resposta

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/chat', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'mensagem',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Resposta empática do chatbot',
            'schema': {
                'type': 'object',
                'properties': {
                    'resposta': {'type': 'string'}
                }
            }
        }
    }
})
def chat():
    data = request.get_json()
    user_msg = data.get("mensagem", "")
    resposta = gerar_resposta(user_msg)
    return jsonify({"resposta": resposta})
