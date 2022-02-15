import PySimpleGUI as sg

class mainGUI:
    def __init__(self):
        layout = [
            [sg.FolderBrowse("Choose path"), sg.Input()],
            [sg.Submit("Run")]
        ]
        # Janela
        window = sg.Window("File Computer by DTBrowser").layout(layout)
        # output
        self.button, self.values = window.Read()
    def browsepath(self):
        data = self.values
        return data[0]
    def getValues(self):
        return self.values
