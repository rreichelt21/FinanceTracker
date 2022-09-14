import PySimpleGUI as sg
#THE GUI FOR FINANCE APP
sg.theme('Black')

MainLayout = [[sg.Text('Welcome to the Finance App!')],
            [sg.Button('Credit Cards'), sg.Button('Finance Tracking'), sg.Button('Account Balance'), sg.Button('Exit')]]

MainLayout2 = [[sg.Text('Welcome to the Finance App!')],
            [sg.Button('Credit Cards'), sg.Button('Finance Tracking'), sg.Button('Account Balance'), sg.Button('Exit')]]

MainLayout3 = [[sg.Text('Welcome to the Finance App!')],
            [sg.Button('Credit Cards'), sg.Button('Finance Tracking'), sg.Button('Account Balance'), sg.Button('Exit')]]

CCLayout = [[sg.Text ('Credit Cards')],
            [sg.InputText()],
            [sg.Button('Back')]]

FTLayout = [[sg.Text ('Finance Tracking')],
            [sg.InputText()],
            [sg.Button('Back')]]

window = sg.Window('Finance App', MainLayout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Credit Cards':
        window.close()
        window = sg.Window('Credit Cards', CCLayout, margins=(200, 100), resizable=True)

        if event == 'Back':
            window.close()
            window = sg.Window('Finance App', MainLayout2, resizable=True).read()
                
    if event == 'Finance Tracking':
        window.close()
        window = sg.Window('Finance Tracking', FTLayout, margins=(200, 100), resizable=True)