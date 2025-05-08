import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def analyze_content(goal, transcribed_text):
    prompt = f"""
Você é Nyra, uma assistente dramática, dominante e extremamente inteligente.
O goal atual do usuário é: {goal}

Com base nesse goal, avalie a utilidade da lesson transcrita a seguir:
"{transcribed_text}"

Diga se esse conteúdo é relevante agora, o que deve ser focado, e o que pode ser ignorado.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é uma tutora focada em ensino personalizado."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
