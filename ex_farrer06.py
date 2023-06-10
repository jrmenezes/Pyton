# @autor Jr_Menezes
##Resolvendo reescrita de Algoritmos em pyton
# Exercícios propostos do livro “Algoritmos Estruturados de Harry Farrer & Outros"
"""Um determinado material radioativo perde metade se sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo
necessário para que essa massa se torne menor do que 0,5 grama. Escreva a massa
inicial, a massa final e o tempo calculado em horas, minutos e segundos."""

class AlgoritmoRadioativo:
    def executar(self):
        #Variaveis
        massaI = float(input("Informe a massa inicial (em gramas): ")) # massa inicial do material radioativo
        massaF = massaI # massa final do material radioativo
        tempo = 0 # tempo em segundos
        horas = 0 # as horas de tempo
        minutos = 0 # os minutos de tempo


        # inicializacao dos acumuladores e constantes
        while massaF >= 0.5:
            massaF = massaF / 2
            tempo = tempo + 50

        # transformando o tempo em horas, minutos e segundos
        segundos = tempo
        while segundos >= 60:
            minutos = minutos + 1
            if minutos == 60:
                horas = horas + 1
                minutos = 0
                segundos = segundos - 60

        #  Resultados
        print(f"Massa inicial (em gramas): {massaI} \n"
              f"Massa final (em gramas): {massaF} \n"
              f"Tempo decorrido em segundos: {tempo}\n"
              f"{horas} horas, {minutos} minutos e {segundos} segundos")
# Utilizando o método
algoritmo = AlgoritmoRadioativo()
algoritmo.executar()
print("Fim da classe AlgoritmoRadioativo")

class AlgoritmoRadioativo_refatorado:
    def executar(self):
        massaI = float(input("Informe a massa inicial (em gramas): "))

        # Calcular a massa final e o tempo decorrido
        massaF = massaI
        tempo = 0
        while massaF >= 0.5:
            massaF /= 2
            tempo += 50

        # Converter o tempo em horas, minutos e segundos
        segundos = tempo
        minutos, segundos = divmod(segundos, 60)
        horas, minutos = divmod(minutos, 60)

        # Exibir os resultados
        print(f"Massa inicial (em gramas): {massaI} \n"
              f"Massa final (em gramas): {massaF} \n"
              f"Tempo decorrido em segundos: {tempo}\n"
              f"{horas} horas, {minutos} minutos e {segundos} segundos")

    # Utilizando o método
algoritmo_ref = AlgoritmoRadioativo_refatorado()
algoritmo_ref.executar()