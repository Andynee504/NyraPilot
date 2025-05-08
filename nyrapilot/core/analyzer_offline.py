def analyze_content(goal, transcribed_text):
    print("\n[Simulação OFFLINE ativada]")
    print(f"Objetivo atual: {goal[:60]}...")
    print(f"Tamanho da transcrição recebida: {len(transcribed_text)} caracteres")
    
    # Lógica simulada (pode ser expandida)
    if goal.lower() in transcribed_text.lower():
        return "Conteúdo altamente relevante para o seu goal atual. Continue focando nesse tipo de lesson."
    elif any(palavra in transcribed_text.lower() for palavra in ["c#", "unity", "script"]):
        return "Alguns elementos podem ser aproveitados para seu projeto, mas há partes que podem ser ignoradas por enquanto."
    else:
        return "O conteúdo desta lesson parece não ser essencial neste momento. Talvez seja melhor revisitar mais tarde."
