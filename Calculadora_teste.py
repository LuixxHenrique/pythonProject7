from tkinter import *
#back-end
#funçao soma
def Soma():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        label1['text'] = float(entry1.get()) + float(entry2.get())
    else:
        label1['text'] = 'Valor Invalido!'
#front-end
#window
janela = Tk()
janela.geometry('400x200+100+500')
janela.minsize(width=100, height=50)
janela.maxsize(width=800, height=400)
#janela.config(bg='black')

#valores constantes
fn = 'Arial 26'
# Criar widgets
label1 = Label(janela, text='Resultado', font=fn)
entry1 = Entry(janela, font=fn)
entry2 = Entry(janela, font=fn)
btn1 = Button(janela, text='Soma', font=fn, command=Soma)

# organizar os widgets
label1.pack()
entry1.pack()
entry2.pack()
btn1.pack()
# executar a janela
janela.mainloop()