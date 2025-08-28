FROM python:3.12-slim

RUN pip install requests python-dotenv

# Copia o arquivo .env
COPY .env /app/.env

# Copia o script Python
COPY bitbucket_check_all_sotorage.py /app/bitbucket_check_all_sotorage.py

WORKDIR /app


CMD ["python", "bitbucket_check_all_sotorage.py"]