# Bitbucket Storage Analyzer

A Python tool to analyze storage usage across all repositories in a Bitbucket workspace, identifying inactive repositories and calculating total storage consumption.

## 📋 About

This tool connects to the Bitbucket API to fetch all repositories in a workspace, analyzes their last update dates, and provides detailed storage statistics. It helps identify inactive repositories that haven't been updated in a specified time period and calculates the total storage footprint of your Bitbucket workspace.

## 🚀 Features

- **Complete Repository Analysis**: Fetches all repositories using pagination
- **Inactive Repository Detection**: Identifies repositories not updated in X years
- **Storage Statistics**: Calculates total, active, and inactive storage usage
- **Flexible Configuration**: Supports environment variables for easy deployment
- **Docker Support**: Ready-to-use Docker container
- **JSON Output**: Provides structured data for further processing

## 📦 Installation

### Prerequisites

- Docker
- Bitbucket App Password with repository read permissions

### Docker Installation
```bash
cp .env.example .env
```
```bash
# Build the Docker image
docker build -t bitbucket-storage-analyzer .
```

## 🔧 Configuration

### Creating Bitbucket App Password

1. Go to Bitbucket Settings → App passwords
2. Create a new app password with **Repository read** permissions
3. Copy the generated password to your `.env` file

## 🚀 Usage

### Basic Usage

```bash
python bitbucket_check_all_sotorage.py
```

### Docker Usage

```bash
# Using pre built .env file
docker run bitbucket-storage-analyzer

```

## 📊 Output Example

#### This output is in Portuguese because I am from Brazil, and the executives and sales team will read this. But feel free to fork it and translate it into English if you want

```
🔍 Verificando espaço total no workspace: Facehook ...
📄 Processando página 1...
   📦 Encontrados 100 repositórios nesta página
📄 Processando página 2...
   📦 Encontrados 19 repositórios nesta página
✅ Total de repositórios encontrados: 119

📊 Analisando repositórios...
📅 Data atual: 2025-08-28 20:37:03.383536+00:00
📅 1 ano(s) atrás: 2024-08-28 20:37:03.383536+00:00
--------------------------------------------------
🛑 Repo parado: portal-amazon | Última atualização: 2017-09-20T19:02:29.976932+00:00 | Tamanho: 28 MB
🛑 Repo parado: portal-soethe | Última atualização: 2021-07-15T21:13:14.920329+00:00 | Tamanho: 21 MB

--------------------------------------------------
📦 RESUMO DO WORKSPACE: Facehook
--------------------------------------------------
🔍 Total de repositórios: 119
📊 Espaço total: 4378.5 MB (~4.28 GB)
🛑 Repositórios inativos (>1 ano(s)): 67
📦 Espaço ocupado por repositórios inativos: 1234.5 MB (~1.21 GB)
💾 Espaço ocupado por repositórios ativos: 3144.0 MB (~3.07 GB)

📋 Estatísticas em JSON:
{
  "workspace": "Facehook",
  "total_repositories": 119,
  "total_size_mb": 4378.54,
  "total_size_gb": 4.28,
  "inactive_repositories": 67,
  "inactive_size_mb": 1234.5,
  "inactive_size_gb": 1.21,
  "active_size_mb": 3144.04,
  "active_size_gb": 3.07
}
```

## 🔒 Security

- **Never commit `.env` files** to version control
- Use `.env.example` as a template
- App passwords should have minimal required permissions

## 🛠️ Development

### Project Structure

```
├── bitbucket_check_all_sotorage.py  # Main script
├── Dockerfile                        # Docker configuration
├── .dockerignore                     # Docker ignore file
├── .env                              # Environment variables (create this)
└── README.md                         # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

### Common Issues

**Authentication Error**
```
❌ Erro na requisição: 401 Client Error: Unauthorized
```
- Check your App Password permissions
- Verify username and workspace name

**No Repositories Found**
```
✅ Total de repositórios encontrados: 0
```
- Verify workspace name
- Check if you have access to the workspace



