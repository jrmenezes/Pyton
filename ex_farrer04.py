#@autor Jr_Menezes
##Resolvendo reescrita de Algoritmos em pyton
#Exercícios propostos do livro “Algoritmos Estruturados de Harry Farrer & Outros"
"""Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele 
comercializa. Para isto, mandou digitar numa linha para cada mercadoria com o nome, 
preço de compra e preço de venda das mesmas.
Fazer um algoritmo que:
 determine e escreva quantas mercadorias proporcionam:
a) lucro menor que 10%
b) lucro entre 10% e 20%
c) lucro maior que 20%
 determine e escreva o valor total de compra e de venda de todas as mercadorias, 
assim como o lucro total.
Obs: o aluno deve adotar um flag."""


quant1 = 0
quant2 = 0
quant3 = 0
total_compra=0
total_venda =0
flag = 1

while flag > 0:
    nome_prod = input("informe o nome do produto: ")
    p_compra = float(input("Informe o preço de compra: "))
    p_venda = float(input("Informe o preço de venda: "))

    lucro = (p_venda-p_compra)/p_compra*100

    if lucro < 10:
            quant1+=1
           
    elif lucro >= 10 and lucro <= 20:
            quant2+=1
           
    else:
            quant3+=1
            
    total_compra+=p_compra
    total_venda+=p_venda
    lucro_total= (total_venda-total_compra)/total_compra*100


    #Validação de calculos
    """print(f"O lucro é de {lucro} % \n"
          f"A quantidade 1 {quant1} \n"
          f"A quantidade 2 {quant2} \n"
          f"A quantidade 3 {quant3} \n"
          f"Total compra {total_compra} \n"
          f"total venda {total_venda} \n"
          f"total venda {lucro_total} \n")
    """
    flag = int(input("Digite 1 para continuar ou 0 zero para finalizar"))
    
print(f"Quantidade de mercadorias com lucro < 10%: {quant1} \n"
      f"Quantidade de mercadorias com lucro < 20%: {quant2}\n" 
      f"Quantidade de mercadorias com lucro > 20%: {quant3}\n" 
      f"Valor total das compras:  R$ {total_compra}\n" 
      f"Valor total das vendas:   R$ {total_venda}\n"
      f"Lucro total: {lucro_total} (%)")

