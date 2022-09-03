def get_float_input(msg: str) -> float:
    return float(input(msg + "\n> "))


def get_int_input(msg: str) -> int:
    return int(input(msg + "\n> "))


def ex1():
    """
    Um condomínio possui 4 blocos que são abastecidos por duas caixas
    d’água diferentes. A caixa A abastece os blocos pares e a caixa B
    abastece os blocos ímpares. Escreva um algoritmo que pergunte ao
    usuário em qual bloco ele mora (1-4) e escreva na tela qual a
    caixa que abastece seu bloco: a caixa a ou a caixa B;
    """
    bloco = get_int_input("Qual é seu bloco (1-4)?")
    print("A caixa de água que abastece seu bloco é:", "A" if bloco % 2 == 0 else "B")


def ex2():
    """
    Um condomínio possui 20 blocos e para uma correta administração
    possui dois síndicos: o sr José que administra os blocos de 1 a 10
    e o sr Hamilton que administra os blocos de 11 a 20. Escreva um
    algoritmo que pergunte ao usuário em qual bloco ele mora e escreva
    na tela qual o síndico responsável;
    """
    bloco = get_int_input("Qual é seu bloco (1-20)?")
    print("O síndico responsável pelo bloco é:", "O sr José" if (bloco > 0) and (bloco < 11) else "O sr Hamilton")


def ex3():
    """
    Escreva um algoritmo que pergunte o valor de uma mercadoria e qual
    o valor que o usuário tem em mãos e diga se o dinheiro é ou não é
    suficiente para adquirir esta mercadoria;
    """
    price = get_float_input("Qual é o valor da mercadoria?")
    money_to_pay = get_float_input("Quanto de dinheiro possui em mãos?")
    enough_to_pay = money_to_pay >= price
    print("O dinheiro", "é suficiente" if enough_to_pay else "não é suficiente")


def ex4():
    """
    Um estacionamento cobra R$ 5,00 por hora porém possui um teto de
    cobrança máxima de R$ 35,00, independente do número de horas.
    Escreva um algoritmo que pergunte ao usuário qual foi o período
    de permanência em horas e escreva na tela o total a pagar.
    """
    total = get_int_input("Quantas horas ficou no estacionamento?") * 5
    projected_total = 35.0 if total > 35 else total
    print("O total a ser pago é de R$", f"{projected_total:.2f}")


if __name__ == "__main__":
    exs = [ex1, ex2, ex3, ex4]
    for idx, ex in enumerate(exs):
        print("Exercício", idx + 1)
        ex()
        print()
        print("#" * 20)
        print()
