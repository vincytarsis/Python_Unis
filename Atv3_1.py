import PySimpleGUI as sg

sg.theme('dark')

layout = [[sg.Text('Nome do Paciente', size=(15, 1)), sg.InputText(key='nome')],
          [sg.Text('Endereço Completo', size=(15, 1)), sg.InputText(key='endereço')],
          [sg.Text('Altura(cm)', size=(8, 1)), sg.Input(key='altura')],
          [sg.Text('Peso(Kg)', size=(8, 1)), sg.Input(key='peso')],
          [sg.Output(key='imc', size=(50, 5))],
          [sg.Button('Calcular'), sg.Button('Reiniciar'), sg.Button('Sair')],
          ]

windows = sg.Window('Cálculo do IMC - Índice de Massa Corporal ', layout)

while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    elif event == 'Reiniciar':
        for key in values:
            windows['nome'].update('')
            windows['endereço'].update('')
            windows['altura'].update('')
            windows['peso'].update('')

    elif event == 'Calcular':
        altura = float(values['altura'])
        peso = float(values['peso'])

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print(f'IMC = {imc:.1f}\nAbaixo do Peso!')

        elif 18 <= imc < 25:
            print(f'IMC = {imc:.1f}\nPeso ideal')

        elif 25 <= imc < 30:
            print(f'IMC = {imc:.1f}\nSobrepeso')

        elif 30 <= imc < 40:
            print(f'IMC = {imc:.1f}\nObesidade')

        else:
            print(f'IMC = {imc:.1f}\nObesidade mórbida')

windows.close()
