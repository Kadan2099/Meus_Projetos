import Cadastro_pf_Victor_bank
from tkinter import *

janela_principal = Tk()
janela_principal.geometry("750x700")
icon = PhotoImage(file="Sem título.png")
janela_principal.iconphoto(True,icon)
janela_principal.title("Gerador de massa de teste")
janela_principal.config(bg="#202020")

widgetCadastro = Label(janela_principal,text="Cadastros")
widgetContagem = Label(janela_principal,text="Contagem")
widgetCadastro.pack()
widgetCadastro.place(x=0,y=0)
widgetContagem.pack()
#Cadastros a fazer
#Contagem
#Tempo em espera
#Start


janela_principal.mainloop()