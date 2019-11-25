from tkinter import *

class MenuLocacao:
    def __init__ (self):
        self.Janela = None
        self.Container1 = None
        self.Container2 = None
        self.Container3 = None
        self.Container4 = None
        self.Container5 = None
        self.Container6 = None
        self.tituloContainer1 = None
        self.tituloContainer2 = None
        self.tituloContainer3 = None
        self.tituloContainer4 = None
        self.opcao = None
        self.opcao1 = None
        self.decisao = None
        self.menuLoca = True
        self.fontepadrao = ("Arial","10")
    
    def Menulocacao(self): # Visao
        while (self.menuLoca):
            self.Janela = Tk()
            self.Janela.title("Menu Locacao")
            self.Janela.geometry("500x400")
            self.Janela['bg'] = "light blue"
            self.Janela.resizable(0,0)

            self.Container1 = Frame(self.Janela)
            self.Container1["pady"] = 10
            self.Container1['bg'] = "light blue"
            self.Container1.pack()

            self.tituloContainer1 = Label(self.Container1,text = "Menu Locacao", bg = "light blue")
            self.tituloContainer1["font"] = ("Arial","30","bold","underline")
            self.tituloContainer1.pack()

            self.Container2 = Frame(self.Janela)
            self.Container2["padx"] = 20
            self.Container2['bg'] = "light blue"
            self.Container2.pack()

            self.tituloContainer2 = Label(self.Container2, text = "Marque o que deseja fazer\n", bg = "light blue", font = ("Arial","15"))
            self.tituloContainer2.pack()   

            self.Container3 = Frame(self.Janela)
            self.Container3["padx"] = 20
            self.Container3['bg'] = "light blue"
            self.Container3.pack()

            self.opcao = IntVar()
            Radiobutton(self.Container3, text = "Voltar ao Menu Principal", variable = self.opcao, value = 1, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Visualizar uma Locacao", variable = self.opcao, value = 2, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Criar uma nova Locacao", variable = self.opcao, value = 3, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Devolver um Carro da Locacao", variable = self.opcao, value = 4, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Devolver uma Locacao Completa", variable = self.opcao, value = 5, bg = "light blue", font = ("Arial", "12")).pack()

            self.Container4 = Frame(self.Janela)
            self.Container4["padx"] = 20
            self.Container4['bg'] = "light blue"
            self.Container4.pack()

            self.decisao = Button(self.Container4)
            self.decisao["width"] = 8
            self.decisao["text"] = "Confirmar"
            self.decisao["font"] = self.fontepadrao
            self.decisao["command"] = self.decideLocacao
            self.decisao.pack()

            self.Janela.mainloop()

    def VisualizarLocacao(self): # Visao
        self.Janela = Tk()
        self.Janela.title("Visualizar Locacao")
        self.Janela.geometry("500x400")
        self.Janela['bg'] = "light blue"
        self.Janela.resizable(0,0)

        self.Container1 = Frame(self.Janela)
        self.Container1["pady"] = 10
        self.Container1['bg'] = "light blue"
        self.Container1.pack()

        self.tituloContainer1 = Label(self.Container1, text = "Visualizar Locacao")
        self.tituloContainer1['bg'] = "light blue"
        self.tituloContainer1["font"] = ("Arial","30","bold","underline")
        self.tituloContainer1.pack()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label(self.Container2, text = "Escolha a locacao que deseja verificar\n")
        self.tituloContainer2["font"] = ("Arial","12")
        self.tituloContainer2['bg'] = "light blue"
        self.tituloContainer2.pack()
    
        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()
        #self.opcao.IntVar()
        #i = 0
        #while (i < len(locadora.locacoes)):
            #Radiobutton(self.Container3, text = "Voltar ao Menu Principal", variable = self.opcao, value = i+1, bg = "light blue", font = ("Arial", "12")).pack()
            #i = i + 1
        
        self.opcao = IntVar()
        Radiobutton(self.Container3, text = "Teste", variable = self.opcao, value = 1, bg = "light blue").pack()

        self.Container4 = Frame (self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.decisao = Button(self.Container4)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontepadrao
        self.decisao["command"] = self.VisualizaLoca # Controle
        self.decisao.pack(side=LEFT)

        self.Janela.mainloop()

    def VisualizaLoca(self): # Modelo (M)
        print ("OK, Modelo")
        self.Janela.destroy()

    def CriarLocacao(self): # Visao (V)
        self.Janela = Tk()
        # O usuario escolhe os carros com CheckButton
        # O usuario digita o nome e a data de aluguel
        # Insere os carros na locacao
        self.Janela.mainloop()
    
    def DevolverCarro(self): # Visao (V)
        self.Janela = Tk()
        # Mostra para o usuario os carros que existe na locacao com Raddibutton
        # Apaga o carro que o usuario escolheu
        self.Janela.mainloop()
    def DevolverLocacao(self): # Visao (V)
        self.Janela = Tk()
        # Mostra para o usuario as locacoes que existe com Raddiobutton
        # Apaga a locacao que o usuario escolher 
        self.Janela.mainloop()
    
    



    def decideLocacao(self): # Controle
        if (self.opcao.get() == 1):
            self.Janela.destroy()
            self.menuLoca = False
        elif (self.opcao.get() == 2):
            self.Janela.destroy()
            self.VisualizarLocacao()
        elif (self.opcao.get() == 3):
            self.Janela.destroy()
            self.CriarLocacao()
        elif (self.opcao.get() == 4):
            self.Janela.destroy()
            self.DevolverCarro()
        elif (self.opcao.get() == 5):
            self.Janela.destroy()
            self.DevolverLocacao()
