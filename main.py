# Calculadora Simples em Python usando Tkinter
from tkinter import *
from tkinter import ttk

# Cores da calculadora

cor1 = "#3b3b3b"  # Cor de fundo
cor2 = "#ffffff"  # Cor dos botões
cor3 = "#f06012"  # Cor do texto
cor4 = "#00ff00"  # Cor de destaque
cor5 = "#0000ff"  # Cor de erro

# Criando a janela da calculadora
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Criando os frames para a tela e os botões da calculadora
frame_tela = Frame(janela, width=300, height=100, bg=cor1)# Criando o frame para a tela da calculadora
frame_tela.grid(row=0, column=0)

freme_botoes = Frame(janela, width=300, height=300)# Criando o frame para os botões da calculadora
freme_botoes.grid(row=1, column=0)


# Variável para armazenar a expressão matemática digitada na calculadora
todos_os_valores = ""  # Variável para armazenar todos os valores digitados na calculadora

# Crinado função
def entrar_valores(expressao):
   
   global todos_os_valores # Variável global para armazenar todos os valores digitados na calculadora

   todos_os_valores += str(expressao) # Variável para armazenar todos os valores digitados na calculadora

   # Convertendo o resultado para string para exibir na tela da calculadora
   valor_texto.set(todos_os_valores) 

# Criando função para calcular a expressão matemática digitada na calculadora
def calcular():
  global todos_os_valores # Variável global para armazenar todos os valores digitados na calculadora
  resultado = eval(todos_os_valores) # Variável para armazenar o resultado da expressão matemática digitada na calculadora
  valor_texto.set(str(resultado)) # Convertendo o resultado para string para exibir na tela da calculadora

# Criando função para limpar a tela da calculadora
def limpar_tela():
  global todos_os_valores # Variável global para armazenar todos os valores digitados na calculadora
  todos_os_valores = "" # Variável para armazenar todos os valores digitados na calculadora
  valor_texto.set("") # Limpando a tela da calculadora
# Criando label para a tela da calculadora
valor_texto = StringVar()# Variável para armazenar o texto da tela da calculadora

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)

# Primeira linha de botões da calculadora
botoes0 = Button(freme_botoes, command = lambda: limpar_tela(), text="C", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para limpar a tela da calculadora
botoes0.place(x=0, y=0)
botoes1 = Button(freme_botoes ,command = lambda: entrar_valores("%") ,text="%", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes1.place(x=118, y=0)
botoes2 = Button(freme_botoes, command = lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes2.place(x=177, y=0)

# Segunda linha de botões da calculadora
botoes4 = Button(freme_botoes, command = lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes4.place(x=0, y=52)
botoes5 = Button(freme_botoes, command = lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes5.place(x=59, y=52)
botoes6 = Button(freme_botoes, command = lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes6.place(x=118, y=52)
botoes7 = Button(freme_botoes, command = lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes7.place(x=177, y=52)

# Terceira linha de botões da calculadora
botoes8 = Button(freme_botoes, command = lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes8.place(x=0, y=104)
botoes9 = Button(freme_botoes, command = lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes9.place(x=59, y=104)
botoes10 = Button(freme_botoes, command = lambda: entrar_valores("6"), text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes10.place(x=118, y=104)
botoes11 = Button(freme_botoes, command = lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes11.place(x=177, y=104)

# Quarta linha de botões da calculadora
botoes12 = Button(freme_botoes, command = lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes12.place(x=0, y=156)
botoes13 = Button(freme_botoes, command = lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes13.place(x=59, y=156)
botoes14 = Button(freme_botoes, command = lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes14.place(x=118, y=156)
botoes15 = Button(freme_botoes, command = lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes15.place(x=177, y=156)

# Quinta linha de botões da calculadora
botoes16 = Button(freme_botoes, command = lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)# Botão para calcular o percentual
botoes16.place(x=0, y=208)
botoes17 = Button(freme_botoes, command = lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes17.place(x=118, y=208)
botoes18 = Button(freme_botoes, command = lambda: calcular(), text="=", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botoes18.place(x=177, y=208)


janela.mainloop()