from typing import List, Callable


def get_int_input(msg: str) -> int:
    return int(input(msg + "\n> "))


def get_float_input(msg: str) -> float:
    return float(input(msg + "\n> "))


def ex1() -> None:
    """
    1. Escreva um programa que pergunte ao usuário qual foi a média
    anual de um aluno e ao final diga se ele está aprovado, reprovado
    ou de exame. Considere que o aluno está aprovado caso a média
    seja maior ou igual a 6.0; de exame com a média entre 3.0 e 5.9
    e reprovado com média menor do que 3.0.
    """
    avg = get_float_input("Qual é a média do aluno?")
    if avg < 3.0:
        print("Aluno foi reprovado")
    elif avg < 6:
        print("Aluno está de exame")
    else:
        print("Aluno foi aprovado")


def ex2() -> None:
    """
    2. Escreva um programa que pergunte as medidas dos três lados de um
    triângulo e diga que o mesmo é isósceles, equilátero ou escaleno.
    """
    first_side = get_float_input("Qual é a medida do primeiro lado do triângulo?")
    second_side = get_float_input("Qual é a medida do segundo lado do triângulo?")
    third_side = get_float_input("Qual é a medida do terceiro lado do triângulo?")
    if first_side == second_side and second_side == third_side:
        print("O triângulo é equilátero")
    elif first_side == second_side or second_side == third_side:
        print("O triângulo é isóceles")
    else:
        print("O triângulo é escaleno")


def ex3() -> None:
    """
    3. Escreva um programa que pergunte em qual mês estamos (1-12) e ao final
    utilize uma estrutura de decisão por seleção para escrever o nome do mês
    por extenso na tela.
    """
    current_month = get_int_input("Em qual mês estamos (1-12)?")
    current_month_str = {
        "1": "Janeiro",
        "2": "Fevereiro",
        "3": "Marco",
        "4": "Abril",
        "5": "Maio",
        "6": "Junho",
        "7": "Julho",
        "8": "Agosto",
        "9": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro",
    }[current_month]
    print(f"Estamos em {current_month_str}")


def ex4() -> None:
    """
    4. Escreva um programa que leia um ano qualquer e verifique se o mesmo está
    entre 1000 e 2999, caso não esteja apresentar uma mensagem de erro. Caso
    esteja nessa faixa verificar se o ano é bissexto. Um ano é bissexto caso
    seja divisível por 4, mas não por 100. Um ano também é bissexto se for
    divisível por 400.
    """
    current_year = get_int_input("Qual ano quer verificar se é bissexto? (1000-2999)")
    if current_year > 2999 or current_year < 1000:
        print('Ano inválido')
    elif current_year % 400 == 0:
        print('Ano bissexto')
    elif current_year % 4 == 0 and current_year % 100 != 0:
        print('Ano bissexto')
    else:
        print('Ano não é bissexto')


def ex5() -> None:
    """
    5. Uma livraria resolveu fazer uma promoção, com os seguintes critérios:
    a. Livros com preços até R$ 10,00 - desconto de 8%
    b. Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%
    c. Livros com preços acima de R$ 60,00 - desconto de 20%
    Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto
    oferecido, em reais.
    """
    book_price = get_float_input("Qual é o preco do livro?")
    if book_price >= 60:
        print(f"Com desconto, o valor fica em R${(book_price * 0.8):.2f}")
    elif book_price > 10:
        print(f"Com desconto, o valor fica em R${(book_price * 0.9):.2f}")
    else:
        print(f"Com desconto, o valor fica em R${(book_price * 0.92):.2f}")


def ex6() -> None:
    """
    6. Considerando o IMC (índice de massa corpórea), calculado como
    peso/(altura*altura), exiba a situação da pessoa com base na seguinte tabela:
    | IMC | Situação |
    | <= 18.5 | Abaixo do peso |
    | >18.5 e <=24.9 | Peso ideal |
    | >24.9 | Acima do peso |
    """
    print("Para calcular seu IMC precisaremos de sua altura e seu peso.")
    weight = get_float_input("Qual é seu peso em kg?")
    height = get_float_input("Qual é sua altura em metros?")
    imc = weight / (height ** 2)
    if imc > 24.9:
        print('Seu peso está acima do peso ideal')
    elif imc > 18.5:
        print('Seu peso está ideal')
    else:
        print('Seu peso está abaixo do ideal')


if __name__ == "__main__":
    exs: List[Callable[[], None]] = [ex1, ex2, ex3, ex4, ex5, ex6()]

    print("Lista 6")
    for idx, ex in exs:
        print(f"Exercício {idx + 1}")
        ex()
        print("\n")
