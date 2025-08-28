#!/bin/bash

# Configurações
WORKSPACE="SEU_WORKSPACE"
USER="SEU_USUARIO"
APP_PASS="SUA_APP_PASS"

# Datas
NOW=$(date -u +%s)
YEAR=$((365*24*60*60))

# Endpoint inicial da API
URL="https://api.bitbucket.org/2.0/repositories/$WORKSPACE?pagelen=100"

# Variável acumuladora
total_old_size=0

echo "🔍 Verificando repositórios inativos no workspace: $WORKSPACE ..."
echo "----------------------------------------"

# Loop de paginação da API
while [ -n "$URL" ]; do
  raw=$(curl -s -u $USER:$APP_PASS "$URL")
  response=$(echo "$raw" | tr -d '\000-\031') # Remove caracteres inválidos

  # Extrai nome, tamanho e última atualização
  echo "$response" | jq -r '.values[] | "\(.name) \(.size) \(.updated_on)"' | while read name size updated; do
    updated_ts=$(date -d "$updated" +%s)
    diff=$((NOW - updated_ts))

    # Se passou mais de 1 ano
    if [ $diff -gt $YEAR ]; then
      size_mb=$((size / 1024 / 1024))
      echo "🛑 Repo parado: $name | Última atualização: $updated | Tamanho: ${size_mb} MB"
      total_old_size=$((total_old_size + size))
    fi
  done

  # Pega próxima página (se existir)
  URL=$(echo "$response" | jq -r '.next // empty')
done

echo "----------------------------------------"
echo "📦 Espaço total ocupado por repositórios inativos: $((total_old_size/1024/1024)) MB (~$((total_old_size/1024/1024/1024)) GB)"
