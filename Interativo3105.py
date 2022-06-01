# Importar
from tkinter import *
janela = Tk()
# Back-end
def Diminuir():
    if label1['text'] > -10:
        label1['text'] -= 1
    else:
        pass

def Aumentar():
    if label1['text'] < 10:
        label1['text'] += 1
    else:
        pass

# Layout

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.bind('-', lambda event: Diminuir())
janela.bind('+', lambda event: Aumentar())

# Fonte
fn = 'Arial 26'

# widgets
label1 = Label(janela, text=0, padx=20, pady=10, width=3, font=fn)
btn1 = Button(janela, text='+', font=fn, command=Aumentar, padx=10, pady=10, width=3)
btn2 = Button(janela, text='-', font=fn, command=Diminuir, padx=10, pady=10, width=3)
byt = Button()
# organizar os widgets
label1.grid(row=0, column=1, sticky=NSEW)
btn1.grid(row=0, column=2, sticky=NSEW)
btn2.grid(row=0, column=0, sticky=NSEW)

# executar a janela
janela.mainloop()
