texto = "target"
string = ""
vetor = []
vetorInvertido = []

#adicioa a string texto em um vetor
for i in texto:
    vetor.append(i)

#inverte o vetor
for i in range(len(texto) - 1, -1,  -1):
    vetorInvertido.append(vetor[i])

#trasnforma o vetor invertido em string
for i in vetorInvertido:
    string += i

print(string)

    
