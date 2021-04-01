def calcula_soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

print(calcula_soma([7, 8, 5, 10]))


def converte_entrada(texto):
    numeros = texto.split(' ')
    lista = []
    for num in lista:
         lista.append(int(num))
        return lista

  lista = converte_entrada(input())
  print(lista)


def processa_numeros(lista):
    lista =  [0 3 4 7 10 ]
    numeros = lista 
    for numeros in numeros:
        numeros = numeros.strip(' ')
        if numeros not in lista:
            quantidade[numeros] = 0
        quantidade[numeros] += 1
    print(quantidade)



 def main():
    entrada = input('insira uma lista')
    lista = entrada.split()
    soma = 0
    for val in lista:
        soma += int(val)
        media = soma / len(lista)
        return media
    resultado = main()
    print(resultado)
