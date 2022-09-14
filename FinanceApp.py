#THE GUI FOR FINANCE APP

import PySimpleGUI as sg
sg.theme('Black')

#MAIN LAYOUT

def mainwindow():
    MainLayout = [[sg.Text('Welcome to the Finance App!')],
                  [sg.Button('Credit Cards'), sg.Button('Finance Tracking'), sg.Button('Account Balance'), sg.Button('Exit')]]
    
    return sg.Window('Finance App', MainLayout, finalize=True)

#SUB LAYOUTS INSIDE MAIN LAYOUT

def CreditCards():
    CCLayout = [[sg.Text ('Credit Cards')],
                [sg.InputText()],
                [sg.Button('Back')]]
    
    return sg.Window('Credit Cards', CCLayout, finalize=True)

def FinanceTracker():
    FTLayout = [[sg.Text ('Finance Tracking')],
                [sg.InputText()],
                [sg.Button('Back')]]
    
    return sg.Window('Finance Tracking', FTLayout, finalize=True)

def AccountBalance():
    ABLayout = [[sg.Text ('Account Balance')],
                [sg.InputText()],
                [sg.Button('Back')]]

    return sg.Window('Account Balance', ABLayout, finalize=True)

#WINDOWS

window1 = mainwindow()

#MAIN LOOP
while True:
    event, values = window1.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Credit Cards':
        window1.hide()
        window2 = CreditCards()

        while True:
            event, values = window2.read()
            
            if event == 'Back':
                window2.hide()
                window1.un_hide()
                break

    if event == 'Finance Tracking':
        window1.hide()
        window3 = FinanceTracker()

        while True:
            event, values = window3.read()
            
            if event == 'Back':
                window3.hide()
                window1.un_hide()
                break

    if event == 'Account Balance':
        window1.hide()
        window4 = AccountBalance()

        while True:
            event, values = window4.read()
            
            if event == 'Back':
                window4.hide()
                window1.un_hide()
                break