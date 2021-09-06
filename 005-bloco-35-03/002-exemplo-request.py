import requests

try:
    resp = requests.get('https://www.betrybe.com/', timeout=2)
except requests.Timeout:
    resp = requests.get('https://www.betrybe.com/', timeout=10)
finally:
    print(resp.status_code)

# Exemplo requisição com tratamento de erros