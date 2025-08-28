# Configuração do Docker com Variáveis de Ambiente

## 📋 Como configurar as variáveis de ambiente

### 1. Criar arquivo `.env`

Crie um arquivo `.env` na pasta `scripts/` com o seguinte conteúdo:

```bash
cp .env.example .env
```

### 2. Construir a imagem Docker

```bash
cd scripts/
docker build -t bitbucket-storage-checker .
```
### 3. Executar o container

```bash
docker run bitbucket-storage-checker
```

## 🔒 Segurança

- **NUNCA** commite o arquivo `.env` no Git
