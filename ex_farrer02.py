#@autor Jr_Menezes
##Resolvendo reescrita de Algoritmos em pyton
#Exercícios propostos do livro “Algoritmos Estruturados de Harry Farrer & Outros"
""""Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50
pessoas. Fazer um algoritmo que calcule e escreva:
 a maior e a menor altura do grupo
 a media de altura das mulheres
 numero de homens"""

soma = 0
cont = 0
mans = 0
womans = 0
alt_maior = 0
alt_menor = 10

while cont < 50:
    altura = float(input("informe a Altura: "))
    sexo = input("Digite seu Sexo M para Masculino e F para Feminino: ")
    print("**************************************************************")
    if altura > alt_maior:
            alt_maior = altura
    if altura < alt_menor:
            alt_menor = altura
    if sexo == 'M' or sexo == 'm':
            mans+=1
    elif sexo == 'F' or sexo == 'f':
            womans+=1
            soma+=altura

    cont+=1

media = soma/womans

print(f"A maior altura é {alt_maior} \n"
      f"A menor altura é {alt_menor}  \n"
      f"A altura media das mulheres é {media} \n"
      f"O numero de homens é {mans}")
