#@autor Jr_Menezes
##Resolvendo reescrita de Algoritmos em pyton
#Exercícios propostos do livro “Algoritmos Estruturados de Harry Farrer & Outros"
"""A conversão de graus Farenheit para centígrados é obtida por
Fazer um algoritmo que calcule e escreva uma tabela de centígrados em função de 
graus farenheit, que variam de 50 a 150 de 1 em 1."""

fh =50
while fh <= 150:
    cent = (5/9)*(fh-32)  
    print(f"Farenheit: {fh}  Centigrados: {cent}")
    fh+=1
