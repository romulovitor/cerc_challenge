# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
# for i in range(20):
#    print(data_list[i])
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
header = data_list[0]
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

genero_index = header.index('Gender')

for line in data_list[:20]:
    print(line[genero_index])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Adiciona pelo index as colunas da lista principal para um secundária
    :param data: Dados do dataset
    :param index: A posição desejada para extrair a informação
    :return: Uma lista contendo todas as informações de uma determinada coluna do dataset
    """
    column_list = []
    for line in data:
        column_list.append(line[index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
# assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
todos_generos = column_to_list(data_list, -2)
male = todos_generos.count('Male')
female = todos_generos.count('Female')

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Cria uma lista secundária com a quantidade de gênero masculino e feminino encontrada na lista de entrada

    :param data_list: Lista com as informações do dataset
    :return: Uma lista com 2 posição com a quantidade de cada gênero
    """
    female = 0
    male = 0
    for line in data_list:
        if line[genero_index] == "Male":
            male = male + 1
        elif line[genero_index] == "Female":
            female = female + 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
# assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Determina qual é o gênero mais popular entre masculino e feminino, baseado na lista de entrada.

    :param data_list: Lista contendo os gêneros do dataset
    :return: retorna o mais popular
    """
    answer = ""
    retorno = count_gender(data_list)
    if retorno[0] > retorno[1]:
        answer = 'Male'
    else:
        answer = 'Female'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

types = ["Customer", "Subscriber"]
user_types = column_to_list(data_list, -3)
quantity = [user_types.count("Customer"), user_types.count("Subscriber")]
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade agrupado por User Types')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Nesse caso podemos dizer que o campo gênero não foi obrigatório quando foi feito a coleta das informações. " \
         "Com isso, existe " \
         "algumas posições na lista vázia, para somar o tamanho real da lista deve considerar a string vázia como " \
         "parte da contagem. "
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
def sort(array):
    """
    Inicio do Método de ordenação Merge Sort
    :param array: Lista de entrada como inteiro
    :return: Lista ordenada
    """
    sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    """
    Ordena a lista, além disso, é uma função recurssiva, essa abordagem é conhecida como dividir para conquistar.

    :param array: Array para ordenar
    :param start: Posição inicial para ondenação
    :param end: Posição final para ordenação
    :return: Retorna a lista inicial informada ordenada
    """
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)

    merge(array, start, end)


def merge(array, start, end):
    """
    Recebe um lista que deve percorrer, partindo de um ponto inicial e final informado pelo processo,
    Faze assim, a junção entre as duas parte da lista que foi dividida anteriormente no processe de ondenação
    :param array: Uma lista informada pelo próprio algoritmo
    :param start: Posição inicial da lista
    :param end: Posição final da lista
    :return: retorna um array ordenado
    """
    array[start: end + 1] = sorted(array[start: end + 1])


def calculo_media(trip_duration_list):
    """
    Calcula a média, baseado em uma lista de entrada

    :param trip_duration_list: Uma lista ordenada com o tempo de viagem realizado
    :return: retorna um inteiro contendo a média calculada
    """
    total = 0
    for num in trip_duration_list:
        total = num + total
    return total / len(trip_duration_list)


def calculo_mediana(trip_duration_list):
    """
    Calcula a mediana baseado na lista de entrada.

    :param trip_duration_list: Recebe uma lista de duração das viagens, com os valores já ordenados
    :return: retorna um inteiro baseado
    """
    n = len(trip_duration_list)
    if n < 1:
        return None
    if n % 2 == 1:
        return trip_duration_list[n // 2]
    else:
        return total_trip_list(trip_duration_list[n // 2 - 1:n // 2 + 1]) / 2


def total_trip_list(list):
    """
    Recebe uma lista de viagens realizada
    :param list: contêm a duração de todas as viagens em uma lista de inteiros
    :return: um inteiro contendo a soma de todas as viagens da lista.
    """
    total = 0
    for i in list:
        total = total + i
    return total


trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(int, trip_duration_list))

sort(trip_duration_list)

min_trip = round(trip_duration_list[0], 0)
max_trip = round(trip_duration_list[-1], 0)

mean_trip = round(calculo_media(trip_duration_list), 0)
median_trip = round(calculo_mediana(trip_duration_list), 0)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
# assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
# assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()

for elem in data_list:
    start_stations.add(elem[3])

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
# """
# Função de exemplo com anotações.
# Argumentos:
#    param1: O primeiro parâmetro.
#    param2: O segundo parâmetro.
# Retorna:
#    Uma lista de valores x.

# """

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"


def count_items(column_list):
    """
    Recebe uma lista de entrada mapea os tipos utilizando a função zip do pyhton. Faz um agrupamento por tipo e faz um count

    :param column_list: lista contendo o dataset
    :return:  duas listas, a item_types retorna categorias da lista, a count_items a quantidade por categoria)
    """
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    # assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
