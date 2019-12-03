from tkinter import *
import Carro as Carro
from random import randint

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
        self.nome = None
        self.data = None
        self.tituloContainer4 = None
        self.opcao = None
        self.opcao1 = None
        self.opcao2 = None
        self.decisao = None
        self.menuLoca = True
        self.fontepadrao = ("Arial","10")
        self.locadora = None
        self.mensagem2 = ""

    def Menulocacao(self,locadora): # Visao
        self.locadora = locadora
        self.mensagem2 = ""
        while (self.menuLoca):
            self.Janela = Tk()
            self.Janela.title("Menu Locacao")
            self.Janela.geometry("500x400")
            self.Janela['bg'] = "light blue"

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

            self.tituloContainer2 = Label(self.Container2, text = "O que voce deseja fazer?", bg = "light blue", font = ("Arial","15"))
            self.tituloContainer2.pack()   

            self.Container3 = Frame(self.Janela)
            self.Container3["padx"] = 20
            self.Container3['bg'] = "light blue"
            self.Container3.pack()

            self.opcao = StringVar()
            self.opcao1 = ["Voltar ao Menu Principal", "Visualizar uma Locacao", "Criar uma nova Locacao", "Devolver Carros da Locacao", "Devolver uma Locacao Completa"]
            self.opcao.set(self.opcao1[0])
            OptionMenu(self.Container3,self.opcao,*self.opcao1).pack()

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

            self.Container5 = Frame(self.Janela)
            self.Container5["padx"] = 20
            self.Container5["bg"] = "light blue"
            self.Container5.pack()

            self.tituloContainer4 = Label(self.Container5,text = self.mensagem2, font = ("Arial","12"), bg = "light blue")
            self.tituloContainer4.pack()

            self.Janela.mainloop()

    def VisualizarLocacao(self): # Visao
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()

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
        
        self.opcao = IntVar()
        i = 0
        while (i < len(self.locadora.locacoes)):
            Radiobutton(self.Container3, text = self.locadora.locacoes[i].toString(), variable = self.opcao, value = i+1, bg = "light blue", font = self.fontepadrao).pack()
            i = i + 1
        
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

    def VisualizaLoca(self): # Modelo (M)
        self.mensagem2 = "Locacao do cliente "+self.locadora.locacoes[self.opcao.get()-1].getCliente() +" alugada em "+self.locadora.locacoes[self.opcao.get()-1].getData()+". "+"\n\nCarros na locacao: "
        i = 0
        while (i < self.locadora.locacoes[self.opcao.get()-1].getTam()):
            self.mensagem2 = self.mensagem2 + "\n"+self.locadora.locacoes[self.opcao.get()-1].getCarro(i).toString()
            i = i + 1
        self.Janela.destroy()

    def CriarLocacao(self): # Visao (V)
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label(self.Container2, text = "Digite seu nome: ",font = self.fontepadrao,bg = "light blue")
        self.tituloContainer2.pack()

        self.nome = Entry(self.Container2)
        self.nome["width"] = 30
        self.nome["font"] = self.fontepadrao
        self.nome.pack(side=LEFT)

        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3["bg"] = "light blue"
        self.Container3.pack()

        self.tituloContainer3 = Label(self.Container3,text = "Digite a data: ",font = self.fontepadrao, bg = "light blue")
        self.tituloContainer3.pack()

        self.data = Entry(self.Container3)
        self.data["width"] = 30
        self.data["font"] = self.fontepadrao
        self.data.pack(side=LEFT)

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.tituloContainer4 = Label(self.Container4, text = "\nMarque os carros que voce deseja alugar", bg = "light blue")
        self.tituloContainer4["font"] = ("Arial","15")
        self.tituloContainer4.pack()

        self.Container5 = Frame(self.Janela)
        self.Container5["padx"] = 20
        self.Container5["bg"] = "light blue"
        self.Container5.pack()

        self.opcao = []
        i = 0
        while (i < len(self.locadora.cars)):
            self.opcao1 = IntVar()
            self.opcao.append(self.opcao1)
            Checkbutton(self.Container5,text = self.locadora.cars[i].toString(),onvalue = 1, offvalue = 0, font = self.fontepadrao, variable = self.opcao[i], bg = "light blue").pack()
            i = i + 1
        
        self.Container6 = Frame(self.Janela)
        self.Container6["padx"] = 20
        self.Container6['bg'] = "light blue"
        self.Container6.pack()

        self.decisao = Button(self.Container6)
        self.decisao["width"] = 8
        self.decisao["text"] = "Confirmar"
        self.decisao["font"] = self.fontepadrao
        self.decisao["command"] = self.verificaCriaLoca
        self.decisao.pack()

    def verificaCriaLoca(self):
        i = 0
        carros = []
        while (i < len(self.locadora.cars)):
            if (self.opcao[i].get() == 1):
                self.locadora.cars[i].setAlugado(True)
                self.locadora.carsAlugados.append(self.locadora.cars[i])
                carros.append(self.locadora.cars[i])
                del(self.locadora.cars[i])
            i = i + 1
        self.locadora.CriarLocacao(carros,self.nome.get(),self.data.get(),randint(0,1000000))
        self.mensagem2 = "Locacao Criada com Sucesso!"
        del (carros[:])
        self.Janela.destroy()

    
    def DevolverCarro(self): # Visao (V)
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label (self.Container2, text = "Escolha de qual locacao ira devolver o carro", font = ("Arial","15"), bg = "light blue")
        self.tituloContainer2.pack()

        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.opcao = IntVar()
        i = 0
        while (i < len(self.locadora.locacoes)):
            Radiobutton(self.Container3, text = self.locadora.locacoes[i].toString(), font = self.fontepadrao, variable = self.opcao, bg = "light blue", value = i + 1).pack()
            i = i + 1

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.decisao = Button (self.Container4)
        self.decisao["width"] = 8
        self.decisao["text"] = "Confirmar"
        self.decisao["font"] = self.fontepadrao
        self.decisao["command"] = self.verificaLocaDelCar
        self.decisao.pack()

    def verificaLocaDelCar(self):
        self.Container3.forget
        self.Container4.destroy()
        self.tituloContainer2 = Label(self.Container2, text = "Escolha quais carros ira deletar")
        self.tituloContainer2.pack()

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4["bg"] = "light blue"
        self.Container4.pack()
        self.opcao1 = []
        i = 0
        while (i < self.locadora.locacoes[self.opcao.get()-1].getTam()):
            self.opcao2 = IntVar()
            self.opcao1.append(self.opcao1)
            Checkbutton(self.Container4,text = self.locadora.locacoes[self.opcao.get()-1].getCarro(i).toString(),onvalue = 1, offvalue = 0, font = self.fontepadrao, variable = self.opcao1[i], bg = "light blue").pack()
            i = i + 1

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.decisao = Button(self.Container4)
        self.decisao["width"] = 8
        self.decisao["text"] = "Confirmar"
        self.decisao["font"] = self.fontepadrao
        self.decisao["command"] = self.DevolverCarros
        self.decisao.pack()
    
    def DevolverCarros(self):
        i = 0
        while (i < self.locadora.locacoes[self.opcao.get()-1].getTam()):
            if (self.opcao1[i].get() == 1):
                self.locadora.DevolverCarro(self.opcao.get()-1,i) 
            i = i + 1
        if (len(self.locadora.locacoes[self.opcao.get()-1] <= 0)):
            self.mensagem2 = "Carros devolvidos com sucesso e locacao apagada!"
        else:    
            self.mensagem2 = "Carros devolvidos com sucesso!"
        self.Janela.destroy()       

    def DevolverLocacao(self): # Visao (V)
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()
        
        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label (self.Container2, text = "Escolha locacao para devolver", font = ("Arial","15"), bg = "light blue")
        self.tituloContainer2.pack()

        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.opcao = IntVar()
        i = 0
        while (i < len(self.locadora.locacoes)):
            Radiobutton(self.Container3, text = self.locadora.locacoes[i].toString(), font = self.fontepadrao, bg = "light blue", variable = self.opcao, value = i + 1).pack()
            i = i + 1

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.decisao = Button(self.Container4)
        self.decisao["width"] = 8
        self.decisao["text"] = "Confirmar"
        self.decisao["font"] = self.fontepadrao
        self.decisao["command"] = self.verificaDelLoca
        self.decisao.pack()


    def verificaDelLoca(self):
        self.locadora.DevolverLocacao(self.opcao.get()-1)
        self.mensagem2 = "Locacao devolvida com sucesso!"
        self.Janela.destroy()


    def decideLocacao(self): # Controle
        if (self.opcao.get() == "Voltar ao Menu Principal"):
            self.Janela.destroy()
            self.menuLoca = False
            
        elif (self.opcao.get() == "Visualizar uma Locacao"):
            self.VisualizarLocacao()
            
        elif (self.opcao.get() == "Criar uma nova Locacao"):
            self.CriarLocacao()
            
        elif (self.opcao.get() == "Devolver Carros da Locacao"):
            self.DevolverCarro()

        elif (self.opcao.get() == "Devolver uma Locacao Completa"):
            self.DevolverLocacao()