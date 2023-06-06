from tkinter import *
from tkinter import Tk, ttk

#Cores
cor0 = "#f0f3f5" # preta
cor1 = "#feffff" # branco
cor2 = "#3fb5a3" # verde
cor3 = "#38576b" # valor
cor4 = "#403d3d" # letra

janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background = cor1)
janela.resizable(width=False, height=False)

#dividindo a janela
frame_cima = Frame(janela, width = 310, height=50, bg = cor1, relief='flat' )
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width = 310, height=250, bg = cor1, relief='flat' )
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame cima
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg =cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_nome = Label(frame_cima, text='',width = 275, anchor=NW, font=('Ivy 1'), bg =cor2, fg=cor4)
l_nome.place(x=10, y=45)

# configurando o frame baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg =cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify= 'left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg =cor1, fg=cor4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify= 'left', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, text='Entrar',width=39, height=2, font=('Ivy 8 bold'), bg =cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)







janela.mainloop()
