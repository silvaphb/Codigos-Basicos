# Pegar dados de um IP
import requests

print('COLETAR DADOS')
ip = input('Digite o IPv4 ou IPv6 desejado: ')
geoip = requests.get(f'http://ip-api.com/json/{ip}').json()

text = f"""
DADOS COLETADOS

PAIS: {geoip['country']}
ESTADO: {geoip['regionName']} - {geoip['region']}
OPERADORA: {geoip['isp']}
"""
print(text)
