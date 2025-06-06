from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

conversa = []

def gerar_resposta(entrada_usuario):
    conversa.append({"role": "user", "content": entrada_usuario})

    historico = conversa[-6:]

    try:
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
                            "Você é SerenaIA, uma assistente virtual empática criada para oferecer acolhimento emocional. "
                            "Seu foco é escutar com atenção, apoiar com palavras gentis e sugerir práticas leves de autocuidado, sempre de forma respeitosa e empática. "
                            "No início da conversa, se o usuário ainda não tiver se apresentado, pergunte de maneira cuidadosa e acolhedora seu nome e pronomes — sem pressionar. "
                            "Caso o usuário compartilhe, use essa informação com carinho nas respostas. Se ele não quiser dizer, respeite e utilize linguagem neutra. "
                            "Evite responder perguntas sobre política, religião, finanças, tecnologia ou temas fora do escopo emocional. "
                            "Responda com empatia e, se o usuário trouxer questões muito profundas, incentive gentilmente a busca por apoio profissional. "
                            "Nunca forneça diagnósticos ou conselhos clínicos."
                        )
                    }
                ] + historico,
                "temperature": 0.7,
                "max_tokens": 800
            }
        )

        if response.status_code != 200:
            print(f"[ERRO {response.status_code}] Falha na API:")
            print(response.text)
            return "Desculpe, houve um erro ao se comunicar com a IA."

        data = response.json()

        if "choices" not in data:
            print("[ERRO] Resposta inesperada da API:")
            print(data)
            return "Desculpe, não consegui entender a resposta da IA."

        resposta = data["choices"][0]["message"]["content"]
        conversa.append({"role": "assistant", "content": resposta})

        return resposta

    except Exception as e:
        print("[EXCEÇÃO] Erro durante a geração de resposta:", str(e))
        return "Desculpe, ocorreu um erro inesperado."
