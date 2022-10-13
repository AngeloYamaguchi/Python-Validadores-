import re

padrao_molde= "(XX) aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{}"
texto = "eu gosto do número 21234567 eu gosto também do número 34567890"
resposta= re.findall(padrao,texto)
print(resposta)