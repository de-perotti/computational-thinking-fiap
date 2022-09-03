from typing import List, Callable


def get_float_input(msg: str) -> float:
    return float(input(msg + "\n> "))


def ex1() -> None:
    """
    O jogo do PIM era uma brincadeira conhecida do Silvio Santos em seu programa
    de auditório que consistia em pedir a alguém que recite uma sequência
    numérica iniciada em 1 e caso o número seja múltiplo de quatro deveria
    substitui-lo pela palavra PIM. Faça um programa que escreva na tela uma
    sequência de 1 a 30 substituindo os múltiplos de quatro pela palavra PIM.
    """
    for i in range(0, 30):
        print("PIM" if (i + 1) % 4 == 0 else i + 1)


def ex2() -> None:
    """
    Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15
    alunos e mostre a média dos checkpoints para cada aluno.
    """
    for i in range(0, 15):
        avg = sum([
            get_float_input(f"Informe a primeira nota para o aluno {i + 1}"),
            get_float_input(f"Informe a segunda nota para o aluno {i + 1}"),
            get_float_input(f"Informe a terceira nota para o aluno {i + 1}"),
        ]) / 3
        print(f"A média do aluno {i + 1} é {avg:.1f}")


def ex3() -> None:
    """
    Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.
    """
    print(f"A soma dos pares entre 1 e 20 é de {sum([x for x in range(2, 21, 2)])}")


if __name__ == "__main__":
    exs: List[Callable[[], None]] = [ex1, ex2, ex3]

    print("Lista 7")
    for idx, ex in enumerate(exs):
        print(f"Exercício {idx + 1}")
        ex()
        print("\n")
