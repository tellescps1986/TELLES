import PySimpleGUI as sg
import numpy as np


def main():
    # Layout da primeira janela
    layout = [
        [sg.Text("Digite a quantidade de números que deseja inserir:")],
        [sg.Input(key='N')],
        [sg.Button("OK"), sg.Button("CANCELAR")]
    ]

    janela = sg.Window("Calculadora", layout)

    # Lê a quantidade de números
    while True:
        evento, valores = janela.read()

        if evento in (sg.WIN_CLOSED, "CANCELAR"):
            janela.close()
            exit()  # Sai do programa

        if evento == "OK":
            try:
                n = int(valores['N'])
                if n <= 0:
                    sg.popup("Insira somente números positivos!")
                    continue
                break
            except:
                sg.popup("Por favor insira um valor válido!")

    janela.close()

    # Lista para armazenar os números
    numeros = []

    # Loop para receber os n números
    for i in range(n):
        layout = [
            [sg.Text(f"Digite o {i + 1}° número:")],
            [sg.Input(key='numero')],
            [sg.Button("OK"), sg.Button("CANCELAR")]
        ]

        janela = sg.Window("Entrada de Números", layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, "CANCELAR"):
                janela.close()
                exit()

            if evento == "OK":
                try:
                    num = float(valores['numero'])
                    numeros.append(num)
                    break
                except:
                    sg.popup("Por favor insira um valor válido!")

        janela.close()

    # Conversão e cálculos
    vetor = np.array(numeros)
    soma = np.sum(vetor)
    media = np.mean(vetor)

    # Layout do resultado
    resultado_layout = [
        [sg.Text("Elementos do Vetor:")],
        [sg.Text(", ".join(map(str, vetor)))],
        [sg.Text(f"Soma dos Elementos: {soma}")],
        [sg.Text(f"Média dos Elementos: {media:.2f}")],
        [sg.Button("FECHAR")]
    ]

    # Janela de resultado
    resultado_janela = sg.Window("Resultado", resultado_layout)

    while True:
        evento, _ = resultado_janela.read()
        if evento in (sg.WINDOW_CLOSED, "FECHAR"):
            break

    resultado_janela.close()

if __name__ == "__main__":
    main()
