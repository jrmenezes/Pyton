# @autor Jr_Menezes
##Resolvendo reescrita de Algoritmos em pyton
# Exercícios propostos do livro “Algoritmos Estruturados de Harry Farrer & Outros"
""""Supondo que a população de um pais A seja da ordem de 90.000.000 de habitantes
com uma taxa anual de crescimento de 3% e que a população de um pais B seja,
aproximadamente, de 200.000.000 de habitantes com uma taxa anual de crescimento
de 1,5%, fazer um algoritmo que calcule e escreva o numero de anos necessários
para que a população do pais A ultrapasse ou iguale a população do pais B, mantidas
essas taxas de crescimento"""

paisA = 90000000
paisB = 200000000
anos = 0

while paisA <= paisB:
    paisA += (paisA * 0.03)
    paisB += (paisB * 0.015)
    anos += 1


print(f"Tempo decorrido foi de  {anos} anos\n"
      f"População do País A é de : {paisA} Habitantes\n"
      f"População do País B é de : {paisB} Habitantes")

