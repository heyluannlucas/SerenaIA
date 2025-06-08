## Configuração e Execução

### Pré-requisitos

- [Node.js](https://nodejs.org/) (para o frontend)
- [Python 3.10+](https://www.python.org/) (para o backend)
- [pip](https://pip.pypa.io/en/stable/)
- (Recomenda-se usar um ambiente virtual Python)

---

### Backend (FastAPI)

1. Acesse a pasta do backend:
   ```bash
   cd backend
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

---

### Frontend (React)

1. Acesse a pasta do frontend:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o aplicativo:
   ```bash
   npm start
   ```

---

O frontend será iniciado em `http://localhost:3000`  
O backend será iniciado em `http://127.0.0.1:8000`
