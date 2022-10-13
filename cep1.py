import requests
from cep import BuscaEndesreco

cep = "06210050"
objeto_cep = BuscaEndesreco(cep)
print(objeto_cep)

#r = requests.get("https://viacep.com.br/ws01001000/json/")
#print(r.text)

bairro,cidade, uf = objeto_cep.acessa_via_cep()
print(bairro,cidade,uf)
