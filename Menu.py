import MenuCarro as MenuCarro
import Locadora as Locadora
import MenuLocacao as MenuLocacao
import Arquivos as Arquivos
import Factory as Factory
from tkinter import *

class menu():
    Fabrica1 = Factory.ConcreteFactoryLocacao()
    Fabrica2 = Factory.ConcreteFactoryCarro()
    def Menu(self):
        self.fontepadrao = ("Arial", "10")
        self.saida = True
        self.locadora = Locadora.Locadora()
        self.arquivos = Arquivos.Arquivos.instancias()
        self.arquivos.Leitura_Arquivo(self.locadora) # Modelo
        while (self.saida): # Visao
            self.JMenu = Tk()
            self.JMenu.title("Menu")
            self.JMenu.geometry("500x300")
            self.JMenu['bg'] = "light blue"
            self.JMenu.resizable(0,0)

            self.Container1 = Frame(self.JMenu)
            self.Container1["pady"] = 5
            self.Container1['bg'] = "light blue"
            self.Container1.pack()

            self.titulocontainer1 = Label(self.Container1, text = "Menu Principal",bg = "light blue")
            self.titulocontainer1["font"] = ("Arial","30","bold","underline")
            self.titulocontainer1.pack()

            self.Container2 = Frame(self.JMenu)
            self.Container2["padx"] = 20
            self.Container2['bg'] = "light blue"
            self.Container2.pack()


            self.mensagem =Label(self.Container2,text ="\nMarque o que deseja fazer: \n",bg ="light blue")
            self.mensagem["font"] = ("Arial", "15")
            self.mensagem.pack(side=LEFT)

            self.Container3 = Frame(self.JMenu)
            self.Container3["padx"] = 20
            self.Container3['bg'] = "light blue"
            self.Container3.pack()

            self.valor = IntVar()
            Radiobutton(self.Container3, text = "Sair do Programa", variable = self.valor, value = 1, bg = "light blue",font = ("Arial","12")).pack()
            Radiobutton(self.Container3, text = "Entrar no Menu de Locacoes", variable = self.valor, value = 2, bg = "light blue",font = ("Arial","12")).pack()
            Radiobutton(self.Container3, text = "Entrar no Menu de Carros", variable = self.valor, value = 3, bg = "light blue",font = ("Arial","12")).pack()

            self.Container4 = Frame(self.JMenu)
            self.Container4["padx"] = 20
            self.Container4['bg'] = "light blue"
            self.Container4.pack()

            self.botao = Button(self.Container4,text="Confirmar")
            self.botao["width"] = 8
            self.botao["font"] = self.fontepadrao
            self.botao["command"] = self.decisao # Controle
            self.botao.pack(side=LEFT)

            self.JMenu.mainloop()
        self.arquivos.Escrita_Arquivo(self.locadora)

    def decisao(self): # Controle

        if (self.valor.get() == 1):
            self.saida = False
            self.JMenu.destroy() # Visao
        elif (self.valor.get() == 2):
            self.JMenu.destroy()
            self.menuLoca = self.Fabrica1.Create_Menu()
            self.menuLoca.Menulocacao(self.locadora)
        elif (self.valor.get() == 3):
            self.JMenu.destroy()
            self.menuCarros = self.Fabrica2.Create_Menu()
            self.menuCarros.Menucarro(self.locadora)

lp = menu()
lp.Menu()
