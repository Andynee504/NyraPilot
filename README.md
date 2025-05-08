# NyraPilot

NyraPilot é uma assistente inteligente que acompanha suas aulas, transcreve o conteúdo em tempo real, filtra o que é relevante com base em seus objetivos de estudo, e registra seu progresso.

---

## ✅ Requisitos

- Python **3.10+**
- [ffmpeg](https://ffmpeg.org/) instalado e acessível no terminal
- Conta na [OpenAI](https://platform.openai.com/account/api-keys) com chave de API
- Arquivo `.env` na raiz com: `OPENAI_API_KEY=sua_chave_aqui`

---

## 🧪 Como configurar (do zero)

### 1. Crie um ambiente virtual:

```bash
py -3.10 -m venv nyrapilot-env
```

### 2. Ative o ambiente virtual:

```bash
nyrapilot-env\Scripts\activate
```

### 3. Instale as dependências:

```bash
python.exe -m pip install --upgrade pip
python.exe -m pip install git+https://github.com/openai/whisper.git openai python-dotenv
```

---

## 📂 Estrutura esperada

```
NyraPilot/
├── nyrapilot-env/          ← ambiente virtual
├── audio_temp.wav          ← áudio da aula para transcrição
├── config/
│   └── goal.txt            ← objetivo de estudo atual
├── logs/                   ← registros de estudo
├── nyrapilot/
│   └── core/
│       └── main.py ...
├── .env                    ← chave da API OpenAI
├── setup.py
└── README.md
```

---

## ▶️ Como usar

Com o ambiente ativado:

```bash
python -m nyrapilot
```

---

## 🛠️ Personalização

Edite `config/goal.txt` para alterar o foco da Nyra.  
Modifique `nyrapilot/core/` para personalizar comportamento e fluxos.

---

## 📩 Suporte

Projeto privado e pessoal. Respeite os termos da OpenAI ao distribuir.

