import PySimpleGUI as sg
import numpy as np


def main():
    # Layout da primeira janela
    layout = [
        [sg.Text("Digite a quantidade de pessoas que deseja cadastrar:")],
        [sg.Input(key='N')],
        [sg.Button("OK"), sg.Button("CANCELAR")]
    ]

    janela = sg.Window("Cadastro de Pessoas", layout)

    # Lê a quantidade de pessoas
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
            except ValueError:
                sg.popup("Por favor insira um valor válido!")

    janela.close()

    # Lista para armazenar os cadastros completos
    cadastro = []

    # Loop para receber os n cadastros
    for i in range(n):
        layout = [
            [sg.Text(f"Digite o nome da {i + 1}ª pessoa:")],
            [sg.Input(key='nome')],

            [sg.Text(f"Digite a idade da {i + 1}ª pessoa:")],
            [sg.Input(key='idade')],

            [sg.Text(f"Digite o peso (kg) da {i + 1}ª pessoa:")],
            [sg.Input(key='peso')],

            [sg.Button("OK"), sg.Button("CANCELAR")]
        ]

        janela = sg.Window(f"Cadastro {i + 1}", layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, "CANCELAR"):
                janela.close()
                exit()

            if evento == "OK":
                nome = valores['nome'].strip()
                idade = valores['idade'].strip()
                peso = valores['peso'].strip()

                # Validação dos campos
                if nome == "":
                    sg.popup("Por favor, insira um nome válido!")
                    continue
                if not idade.isdigit():
                    sg.popup("Por favor, insira uma idade numérica!")
                    continue
                try:
                    peso_float = float(peso)
                except ValueError:
                    sg.popup("Por favor, insira um peso válido (número)!")
                    continue

                # Armazena o cadastro como dicionário
                cadastro.append({
                    "Nome": nome,
                    "Idade": int(idade),
                    "Peso (kg)": peso_float
                })
                break

        janela.close()

    # Calcula média dos pesos
    pesos = [pessoa["Peso (kg)"] for pessoa in cadastro]
    media_peso = np.mean(pesos)

    # Monta texto final
    texto_final = "PESSOAS CADASTRADAS:\n\n"
    for i, pessoa in enumerate(cadastro, start=1):
        texto_final += f"{i}. Nome: {pessoa['Nome']} | Idade: {pessoa['Idade']} | Peso: {pessoa['Peso (kg)']} kg\n"
    texto_final += f"\nMédia dos pesos: {media_peso:.2f} kg"

    sg.popup("Cadastro concluído!", texto_final)


if __name__ == "__main__":
    main()
