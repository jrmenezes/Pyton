#@autor Jr_Menezes
##Resolver reescrita de Algoritmos em pyton
""""Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo.
A última linha, que não entrará nos cálculos, contem o valor da idade igual a zero.
Calcule e escreva a idade media deste grupo de indivíduos"""

soma = 0
contador = 0
idade = int(input("Digite uma Idade: \n"))

while (idade > 0):
        soma+=idade
        contador+=1
        idade = int(input("Digite a próxima idade ou 0 (numero zero) para sair \n"))
        media = soma/contador
print(f" A media de idade é {media} anos")

#verificando os valores no laço de repetição
print(f" A soma das idades é igual a {soma} \n "
      f"A quantidade de individuos é {contador}")

