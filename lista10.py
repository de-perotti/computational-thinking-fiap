from typing import List, Callable


def ex1() -> None:
    """
    1. Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista.
    Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar.
    Por fim, imprima as 3 listas.
    """

    lista = []
    par = []
    impar = []
    for i in range(10):
        lista.append(int(input(f"Digite o {i + 1}º número: ")))
        if lista[i] % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])
    print(f"Lista: {lista}\nPares: {par}\nÍmpares: {impar}")


def ex2() -> None:
    """
    2. Faça um programa em Python que leia duas listas com 10 elementos cada.
    Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das 2 listas.
    """

    lista1 = []
    lista2 = []
    lista3 = []
    for i in range(10):
        lista1.append(int(input(f"Digite o {i + 1}º número da lista 1: ")))
        lista2.append(int(input(f"Digite o {i + 1}º número da lista 2: ")))
    for i in range(10):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    print(f"Zip: {lista3}")


def ex3() -> None:
    """
    3. Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno.
    Em seguida, imprima o número de alunos com média maior ou igual a 7.0.
    """

    alunos = []
    for i in range(10):
        alunos.append(
            [int(input(f"Digite a nota 1 do {i + 1}º aluno: ")),
             int(input(f"Digite a nota 2 do {i + 1}º aluno: ")),
             int(input(f"Digite a nota 3 do {i + 1}º aluno: "))])
    media = [sum(aluno) / len(aluno) for aluno in alunos]
    print(f"Média: {media}")
    print(f"Alunos com média maior ou igual a 7.0: {len([aluno for aluno in media if aluno >= 7])}")


def ex4() -> None:
    """
    4. Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
    encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
    Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    a. Calcule e mostre a soma dos valores;
    b. Calcule e mostre a média dos valores;
    c. Calcule e mostre a quantidade de valores acima da média calculada;
    d. Calcule e mostre a quantidade de valores abaixo de sete.
    """

    notas = []
    while True:
        nota = int(input("Digite uma nota: "))
        if nota == -1:
            break
        notas.append(nota)
    print(f"Quantidade de valores lidos: {len(notas)}")
    print(f"Soma dos valores: {sum(notas)}")
    media = sum(notas) / len(notas)
    print(f"Média dos valores: {media}")
    print(f"Valores acima da média: {len([nota for nota in notas if nota > media])}")
    print(f"Valores abaixo de 7: {len([nota for nota in notas if nota < 7])}")


if __name__ == "__main__":
    exs: List[Callable[[], None]] = [ex1, ex2, ex3, ex4]
    for index, ex in enumerate(exs, start=1):
        print(f"Exercício {index}")
        ex()
        print()
