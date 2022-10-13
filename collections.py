usuarios_data_science = [15,23,43,56]
usuarios_machie_learning = [13,23,56,42]
assitiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machie_learning)
assitiram
len(assitiram)
usuarios_data_science = {15,23,43,56}
usuarios_machie_learning = {13,23,56,42}
usuarios_machie_learning & usuarios_data_science
usuarios_machie_learning ^ usuarios_data_science
usuarios_machie_learning | usuarios_data_science
usuarios_machie_learning - usuarios_data_science

usuarios ={1,5,7,8,12,15}
usuarios.add(13)
print(usuarios)
 usuarios = frozenset(usuarios)

aparicoes= {
    "guilherme" : 1,
    "cachorro":2
    "nome" : 3
    "vindo": 4
}
aparicoes.get("guilherme")
aparicoes = dict("guilherme" :1,)
aparicoes =["carlos"] = 1
del aparicoes["carlos"]

 for elemento in aparicoes.keys():

 for elemento in aparicoes.values():
for chave, valor  in aparicoes.itens():


dicionario = defaultdict(int)

Counter(texto1.lower)



