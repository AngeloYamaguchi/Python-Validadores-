import re

padrao ="\w{5,50}@\w{3,10}.com.br"
texto = "aaaabbbbcccc rodrigo123@gmail.com.br"
resposta= re.search(padrao, texto)
print(resposta.group())
