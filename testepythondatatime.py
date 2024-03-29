from tkinter import *
from datetime import datetime

cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

fundo = cor1
cor = cor3

janela = Tk()
janela.title("")
janela.geometry('440x180')
janela.resizable(width=False, height=False)  # Corrigido os valores de width e height
janela.configure(background=fundo)

def relogio():
    global dia_semana, dia, mes, ano
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + ano)
    l1.after(200, relogio)

l1 = Label(janela, font=('Arial', 80), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, font=('Arial', 20), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()

janela.mainloop()
