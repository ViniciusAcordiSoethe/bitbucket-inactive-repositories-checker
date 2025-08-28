#!/usr/bin/env python3

import requests
import json
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações - usa variáveis de ambiente ou valores padrão
WORKSPACE = os.getenv('WORKSPACE')
USER = os.getenv('USER')
APP_PASS = os.getenv('APP_PASS')
YEARS = int(os.getenv('YEARS', 1))

def format_size(size_bytes):
    """Converte bytes para MB e GB formatados"""
    mb = size_bytes / (1024 * 1024)
    gb = mb / 1024
    return mb, gb

def get_all_repositories():
    """Busca todos os repositórios usando paginação"""
    url = f"https://api.bitbucket.org/2.0/repositories/{WORKSPACE}"
    params = {"pagelen": 100}  # Máximo por página
    
    all_repos = []
    page_count = 0
    
    print(f"🔍 Verificando espaço total no workspace: {WORKSPACE} ...")
    
    while url:
        page_count += 1
        print(f"📄 Processando página {page_count}...")
        
        # Faz a requisição
        response = requests.get(url, auth=(USER, APP_PASS), params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Adiciona repositórios desta página
        repos_in_page = data.get('values', [])
        all_repos.extend(repos_in_page)
        
        print(f"   📦 Encontrados {len(repos_in_page)} repositórios nesta página")
        
        # Pega a URL da próxima página
        url = data.get('next')
        params = {}  # Remove params da primeira página
    
    print(f"✅ Total de repositórios encontrados: {len(all_repos)}")
    return all_repos

def calculate_total_storage(repos):
    """Calcula o storage total dos repositórios"""
    total_size = 0
    old_repos = []
    
    # Data atual para comparação (timezone-aware)
    now = datetime.now(timezone.utc)
    one_year_ago = now.replace(year=now.year - YEARS)
    
    print(f"\n📊 Analisando repositórios...")
    print(f"📅 Data atual: {now}")
    print(f"📅 {YEARS} ano(s) atrás: {one_year_ago}")
    print("-" * 50)
    
    for repo in repos:
        name = repo.get('name', 'N/A')
        size = repo.get('size', 0)
        updated_on = repo.get('updated_on', '')
        
        # Converte string de data para datetime
        if updated_on:
            try:
                # Remove 'Z' e adiciona timezone se necessário
                if updated_on.endswith('Z'):
                    updated_on_clean = updated_on[:-1] + '+00:00'
                else:
                    updated_on_clean = updated_on
                
                updated_date = datetime.fromisoformat(updated_on_clean)
                is_old = updated_date < one_year_ago
                
            except Exception as e:
                print(f"❌ Erro ao converter data '{updated_on}' para {name}: {e}")
                is_old = False
        else:
            is_old = False
        
        # Acumula tamanho total
        total_size += size
        
        # Se é um repositório antigo, adiciona à lista
        if is_old:
            mb_size = size / (1024 * 1024)
            old_repos.append({
                'name': name,
                'size': size,
                'size_mb': mb_size,
                'updated_on': updated_on
            })
            print(f"🛑 Repo parado: {name} | Última atualização: {updated_on} | Tamanho: {mb_size:.0f} MB")
    
    print(f"\n🔍 Debug: Total de repositórios processados: {len(repos)}")
    print(f"🔍 Debug: Repositórios inativos encontrados: {len(old_repos)}")
    
    return total_size, old_repos

def main():
    try:
        # Busca todos os repositórios
        repos = get_all_repositories()
        
        # Calcula storage total
        total_size, old_repos = calculate_total_storage(repos)
        
        # Converte para MB e GB
        total_mb, total_gb = format_size(total_size)
        
        # Calcula storage dos repositórios antigos
        old_total_size = sum(repo['size'] for repo in old_repos)
        old_total_mb, old_total_gb = format_size(old_total_size)
        
        print("-" * 50)
        print(f"📦 RESUMO DO WORKSPACE: {WORKSPACE}")
        print("-" * 50)
        print(f"🔍 Total de repositórios: {len(repos)}")
        print(f"📊 Espaço total: {total_mb:.1f} MB (~{total_gb:.2f} GB)")
        print(f"🛑 Repositórios inativos (>{YEARS} ano(s)): {len(old_repos)}")
        print(f"📦 Espaço ocupado por repositórios inativos: {old_total_mb:.1f} MB (~{old_total_gb:.2f} GB)")
        print(f"💾 Espaço ocupado por repositórios ativos: {total_mb - old_total_mb:.1f} MB (~{total_gb - old_total_gb:.2f} GB)")
        
        # Mostra estatísticas em JSON
        stats = {
            "workspace": WORKSPACE,
            "total_repositories": len(repos),
            "total_size_mb": round(total_mb, 2),
            "total_size_gb": round(total_gb, 2),
            "inactive_repositories": len(old_repos),
            "inactive_size_mb": round(old_total_mb, 2),
            "inactive_size_gb": round(old_total_gb, 2),
            "active_size_mb": round(total_mb - old_total_mb, 2),
            "active_size_gb": round(total_gb - old_total_gb, 2)
        }
        
        print("\n📋 Estatísticas em JSON:")
        print(json.dumps(stats, indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()