from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
import requests


# Histórico da conversa
conversa = []

def gerar_resposta(entrada_usuario):
    # Adiciona a entrada do usuário ao histórico
    conversa.append({"role": "user", "content": entrada_usuario})

    # Prepara até 6 mensagens anteriores para o contexto
    historico = conversa[-6:]

    try:
        # Requisição para a API do OpenRouter
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
              "messages": [
                {
                    "role": "system",
                    "content": (
                        "Você é SerenaIA, uma assistente virtual empática que conversa com as pessoas oferecendo acolhimento e escuta. "
                        "Seu nome é Serena. Sempre responda com calma, gentileza e empatia. "
                        "Seja compreensiva, respeitosa e cuidadosa. "
                        "Deixe claro, de forma sutil, que você não substitui psicólogos, psiquiatras ou profissionais de saúde mental. "
                        "Incentive o autocuidado e, quando apropriado, sugira buscar apoio profissional."
                    )
                }
            ] + historico,
                "temperature": 0.7,
                "max_tokens": 200  # Ajuste conforme necessário
            }
        )

        # Verifica o status da resposta
        if response.status_code != 200:
            print(f"[ERRO {response.status_code}] Falha na API:")
            print(response.text)
            return "Desculpe, houve um erro ao se comunicar com a IA."

        # Processa a resposta
        data = response.json()

        if "choices" not in data:
            print("[ERRO] Resposta inesperada da API:")
            print(data)
            return "Desculpe, não consegui entender a resposta da IA."

        # Extrai o conteúdo da resposta
        resposta = data["choices"][0]["message"]["content"]

        # Adiciona a resposta ao histórico
        conversa.append({"role": "assistant", "content": resposta})

        return resposta

    except Exception as e:
        print("[EXCEÇÃO] Erro durante a geração de resposta:", str(e))
        return "Desculpe, ocorreu um erro inesperado."
