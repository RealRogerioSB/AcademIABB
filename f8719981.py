lista_exclusiva = [1, 3, 5, 6, 9, 10]

pesquisa1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pesquisa2 = [1, 4, 5, 6, 7, 8, 9, 10, 12]


def consta_lista(pesquisa):
    result = [num for num in pesquisa if num in lista_exclusiva]
    return "S" if result == lista_exclusiva else "N"


print(consta_lista(pesquisa1))
print(consta_lista(pesquisa2))
