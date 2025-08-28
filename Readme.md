# Bitbucket Inactive Repositories Checker

Este script em **Bash** lista todos os repositórios inativos (sem atualizações há mais de 1 ano) de um workspace do Bitbucket e calcula o espaço total ocupado por eles.

---

## Funcionalidades

- Consulta todos os repositórios de um workspace Bitbucket via API.
- Filtra os repositórios que não foram atualizados há mais de 1 ano.
- Mostra o tamanho de cada repositório inativo em MB.
- Calcula o total de espaço ocupado pelos repositórios inativos.

---

## Pré-requisitos

- **Bash** (Linux, macOS ou WSL no Windows)
- **curl**
- **jq** (para parse de JSON)   

---

### Instale o curl e o jq
```bash
sudo apt-get install curl jq
```

## Como usar

1. Salve o script em um arquivo, por exemplo `bitbucket_script.sh`.
2. Dê permissão de execução:
   ```bash
   chmod +x bitbucket_script.sh

3. Execute o script:
   ```bash
   ./bitbucket_script.sh
   ```

4. Forneça as credenciais do Bitbucket:
   ```bash
   USER=SEU_USUARIO
   APP_PASS=SUA_APP_PASS
---
5. Rode o script:
   ```bash
   ./bitbucket_script.sh
   ```

6. O script vai listar todos os repositórios inativos e calcular o espaço total ocupado por eles.

---

## Exemplo de saída 
```bash
🔍 Verificando repositórios inativos no workspace: Boxti ...
----------------------------------------
🛑 Repo parado: Boxti-API | Última atualização: 2024-08-28T12:00:00Z | Tamanho: 100 MB
🛑 Repo parado: Boxti-API | Última atualização: 2024-08-28T12:00:00Z | Tamanho: 100 MB      
----------------------------------------
Total de repositórios inativos: 2
Total de espaço ocupado: 200 MB
```

---

## Observações
- O script usa a API do Bitbucket para consultar os repositórios.
- O script é limitado a 100 repositórios por consulta. (para remover o limite, basta alterar o valor de `pagelen` no script)

---

## Contribuições

- Pull requests são bem-vindos!
- Se você encontrar algum problema, por favor, abra uma issue.
- Se você quiser adicionar uma funcionalidade, por favor, abra uma issue primeiro.  
