from cpf import Cpf
from validate_docbr import CNPJ
cpf = "29658488862"

fatia1= cpf[:3]
fatia2 = cpf[3:6]
fatia3 = cpf[6:9]
fati4 = cpf[9:]

print(f"{fatia1}.{fatia2}.{fatia3}-{fati4}")

print(fatia1)
print()
print()
print()
print()