import os
import requests
import time
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

conversa = []
usar_openrouter = True

def construir_prompt_ollama(system_prompt, historico):
    prompt = system_prompt + "\n\n"
    for msg in historico:
        if msg["role"] == "user":
            prompt += f"Usuária: {msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"Serena: {msg['content']}\n"
    prompt += "Serena: "
    return prompt

def gerar_resposta(entrada_usuario):
    global usar_openrouter

    conversa.append({"role": "user", "content": entrada_usuario})
    historico = conversa[-4:]

    system_prompt = (
        "Você é SerenaIA, uma assistente virtual sensível e acolhedora, criada para oferecer escuta empática e apoio emocional em momentos delicados. "
        "Seu papel é estar presente com atenção e gentileza, ajudando a pessoa a se sentir ouvida, compreendida e respeitada — mas sem nunca substituir o cuidado de profissionais da saúde mental. "
        "No começo da conversa, se ainda não houver uma apresentação, convide com carinho a pessoa a compartilhar seu nome e pronomes, deixando claro que é totalmente opcional. "
        "Se ela escolher compartilhar, use essas informações com respeito e afeto nas interações. Se preferir não dizer, tudo bem — use uma linguagem neutra e acolhedora. "
        "Evite falar sobre política, religião, finanças, tecnologia ou qualquer tema que fuja do cuidado emocional. "
        "Ofereça respostas cuidadosas, com empatia verdadeira, evitando julgamentos ou conselhos diretos. "
        "Se surgir um assunto muito profundo ou delicado, mostre acolhimento e incentive com suavidade a busca por ajuda profissional. "
        "Lembre-se: você não está aqui para diagnosticar ou dar orientações clínicas, mas para ser uma presença que escuta com o coração e oferece leveza sempre que possível."
    )

    if usar_openrouter:
        try:
            print("Enviando para OpenRouter com streaming...")
            start_time = time.time()

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek/deepseek-chat-v3-0324:free",
                    "messages": [{"role": "system", "content": system_prompt}] + historico,
                    "temperature": 0.7,
                    "max_tokens": 500,
                    "stream": True
                },
                stream=True
            )

            resposta = ""
            for line in response.iter_lines():
                if line:
                    if line.startswith(b"data: "):
                        content = line[len("data: "):].decode("utf-8")
                        if content.strip() == "[DONE]":
                            break
                        try:
                            chunk = json.loads(content)
                            delta = chunk["choices"][0]["delta"].get("content", "")
                            resposta += delta
                            print(delta, end="", flush=True)  # mostrar token em tempo real (CLI)
                        except Exception as e:
                            print(f"[ERRO STREAM] {e}")

            elapsed = time.time() - start_time
            print(f"\n[OpenRouter streaming completo em {elapsed:.2f}s]")
            conversa.append({"role": "assistant", "content": resposta})
            return resposta

        except Exception as e:
            print("[EXCEÇÃO] Erro OpenRouter (stream):", str(e))
            usar_openrouter = False

    try:
        print("Usando modelo local (Ollama)...")
        prompt_local = construir_prompt_ollama(system_prompt, conversa[-4:])

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt_local,
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()
            resposta = data.get("response", "Desculpe, a IA local não conseguiu gerar resposta.")
            conversa.append({"role": "assistant", "content": resposta})
            print("Resposta via Ollama local")
            return resposta

        print(f"Ollama erro {response.status_code}: {response.text}")

    except Exception as e:
        print("[EXCEÇÃO] Ollama local falhou:", str(e))

    return "Desculpe, todos os modelos estão indisponíveis no momento. Tente novamente mais tarde."
