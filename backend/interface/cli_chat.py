from app.core.responder import gerar_resposta

print("SerenaIA - Chat de apoio emocional. Digite 'sair' para encerrar.\n")

while True:
    msg = input("Você: ")
    if msg.lower() in ['sair', 'exit', 'quit']:
        print("SerenaIA: Estou sempre por aqui. Cuide-se! 💙")
        break
    resposta = gerar_resposta(msg)
    print(f"SerenaIA: {resposta}")
