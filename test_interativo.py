import os
from nyrapilot.core.analyzer_offline import analyze_content
from pathlib import Path

# Simulações de entrada
objetivos = [
    "Criar um jogo em Unity com movimentação e pontuação.",
    "Aprender fundamentos de C# aplicados à lógica de programação.",
    "Focar em UX Design para interfaces responsivas."
]

transcricoes = [
    "Hoje aprendemos como usar C# para movimentar um personagem usando Rigidbody em Unity.",
    "A aula falou sobre princípios de design visual e usabilidade em interfaces mobile.",
    "Estudamos estruturas condicionais em C# como if, else e switch."
]

print("🧪 Teste Interativo da Nyra (Modo Offline)")
print("=========================================
")

for i, (goal, texto) in enumerate(zip(objetivos, transcricoes), 1):
    print(f"
🔹 Teste {i}")
    print(f"Objetivo simulado:
→ {goal}")
    print(f"
Transcrição simulada:
→ {texto}")
    resposta = analyze_content(goal, texto)
    print(f"
🧠 Nyra responde:
{resposta}")
    print("-" * 40)

