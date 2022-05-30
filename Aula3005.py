#Importar biblioteca
from tkinter import *

#back-end
def imprimir():
    label1['text'] = entry1.get()
# print(entry1.get())

#front-end

#Criar janela
janela = Tk()
janela.geometry('400x200+100+500')
janela.minsize(width=100, height=50)
janela.maxsize(width=800, height=400)
janela.config(bg='black')

#Criar widgets
label1 = Label(janela, text='Cade a Sextaaaa',
                            font='Arial 36 bold')
entry1 = Entry(janela, font='Arial 36')
btn1 = Button(janela, text= 'Sair', font='Arial 36', command=quit)
btn2 = Button(janela, text= 'Imprimir', font='Arial 36', command=imprimir)

#organizar os widgets
label1.pack()
entry1.pack()
btn1.pack()
btn2.pack()
#executar a janela
janela.mainloop()










