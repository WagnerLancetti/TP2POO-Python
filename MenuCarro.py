import Carro as Carro
from random import randint
from tkinter import *
import Factory as Factory
import ControleCarro as ControleCarro

class MenuCarro:
    Fabrica1 = Factory.ConcreteFactoryLocacao()
    Fabrica2 = Factory.ConcreteFactoryCarro
    Controle = ControleCarro.ControleMenuCarro()
    def Menucarro(self,locadora):
        self.fontePadrao = ("Arial", "10")
        self.locadora = locadora
        self.mensagem2 = ""
        self.menucarro = True
        while (self.menucarro): # Visao
            self.Janela = Tk()
            self.Janela.title("Menu Carro")
            self.Janela.geometry("700x400")
            self.Janela['bg'] = "light blue"

            self.Container1 = Frame(self.Janela)
            self.Container1["pady"] = 10 # Distancia do container no eixo y
            self.Container1['bg'] = "light blue"
            self.Container1.pack()

            self.tituloContainer1 = Label(self.Container1, text = "Menu Carro",bg = "light blue")
            self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
            self.tituloContainer1.pack()

            self.Container2 = Frame(self.Janela) # Mensagem para o usuário
            self.Container2["padx"] = 20 # Distancia do container no eixo x
            self.Container2['bg'] = "light blue"
            self.Container2.pack()

            self.tituloContainer2 = Label(self.Container2,bg = "light blue", text = "O que voce deseja fazer?",font = self.fontePadrao)
            self.tituloContainer2["font"] = ("Arial", "12")
            self.tituloContainer2.pack(side=LEFT)

            self.Container3 = Frame(self.Janela) # Opcoes que o usuario pode fazer
            self.Container3["padx"] = 20 # Distancia do container no eixo x
            self.Container3['bg'] = "light blue"
            self.Container3.pack()

            self.opcao = StringVar()
            self.opcao1 = ["Voltar para o Menu Principal","Cadastrar Carro", "Remover Carro", "Buscar Carro"]
            self.opcao.set(self.opcao1[0])

            OptionMenu(self.Container3, self.opcao,*self.opcao1).pack()

            self.Container4 = Frame(self.Janela) # Botao de escolha
            self.Container4["padx"] = 20 # Distancia do container no eixo x
            self.Container4['bg'] = "light blue"
            self.Container4.pack()

            self.decisao = Button(self.Container4)
            self.decisao["text"] = "Confirmar"
            self.decisao["font"] = self.fontePadrao
            self.decisao["width"] = 8
            self.decisao.bind("<Button-1>",self.verificaOpcaoCarro)
            self.decisao.pack(side=LEFT)

            self.Container5 = Frame(self.Janela)
            self.Container5["padx"] = 20
            self.Container5["bg"] = "light blue"
            self.Container5.pack()

            self.tituloContainer5 = Label(self.Container5, text = self.mensagem2,bg = "light blue", font = self.fontePadrao)
            self.tituloContainer5.pack()


            self.Janela.mainloop()

    def CadastrarCarro(self): # Visao
        self.tituloContainer5.destroy()
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label(self.Container2, text = "Digite as informacoes do novo carro: \n",bg = "light blue")
        self.tituloContainer2["font"] = ("Arial", "12")
        self.tituloContainer2.pack()

        self.Container3 = Frame(self.Janela) # Placa
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.tituloContainer3 = Label(self.Container3, text ="Placa     ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer3.pack(side=LEFT)

        self.placa = Entry(self.Container3)
        self.placa["width"] = 30
        self.placa["font"] = self.fontePadrao
        self.placa.pack(side=LEFT)

        self.Container4 = Frame(self.Janela) # Marca
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.tituloContainer4 = Label(self.Container4, text ="Marca   ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer4.pack(side=LEFT)

        self.marca = Entry(self.Container4)
        self.marca["width"] = 30
        self.marca["font"] = self.fontePadrao
        self.marca.pack(side=LEFT)

        self.Container5 = Frame(self.Janela) # Cor
        self.Container5["padx"] = 20
        self.Container5['bg'] = "light blue"
        self.Container5.pack()

        self.tituloContainer5 = Label(self.Container5, text ="Cor       ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer5.pack(side=LEFT)

        self.cor = Entry(self.Container5)
        self.cor["width"] = 30
        self.cor["font"] = self.fontePadrao
        self.cor.pack(side=LEFT)

        self.Container6 = Frame(self.Janela) # Modelo
        self.Container6["padx"] = 20
        self.Container6['bg'] = "light blue"
        self.Container6.pack()

        self.tituloContainer6 = Label(self.Container6, text ="Modelo   ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer6.pack(side=LEFT)

        self.modelo = Entry(self.Container6)
        self.modelo["width"] = 30
        self.modelo["font"] = self.fontePadrao
        self.modelo.pack(side=LEFT)

        self.Container7 = Frame(self.Janela) # Ano
        self.Container7["padx"] = 20
        self.Container7['bg'] = "light blue"
        self.Container7.pack()

        self.tituloContainer7 = Label(self.Container7, text ="Ano       ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer7.pack(side=LEFT)

        self.ano = Entry(self.Container7)
        self.ano["width"] = 30
        self.ano["font"] = self.fontePadrao
        self.ano.pack(side=LEFT)

        self.Container8= Frame(self.Janela)
        self.Container8["padx"] = 20
        self.Container8['bg'] = "light blue"
        self.Container8.pack()

        self.decisao = Button(self.Container8)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao.bind("<Button-1>",self.VerificaCadastro)
        self.decisao.pack(side=LEFT)

    def VerificaCadastro(self,event):
        self.decisao.destroy()
        self.mensagem2 = self.Controle.verificacaoCadastro(self.placa.get(),self.marca.get(),self.cor.get(),self.modelo.get(),self.ano,self.locadora)
        self.Janela.destroy()

    def RemoverCarro(self): # Visao
        self.tituloContainer5.destroy()
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.mensagem1 = Label(self.Container2,text = "Escolha qual carro deseja remover",bg = "light blue")
        self.mensagem1["font"] = ("Arial","15")
        self.mensagem1.pack()

        self.opcao = IntVar()
        i = 0
        while (i < len(self.locadora.cars)):
            Radiobutton(self.Container2,text = self.locadora.ListarCarrosParaAlugar(i).toString(), variable = self.opcao, value = i + 1, bg = "light blue").pack()
            i = i + 1

        self.Container3 = Frame (self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.decisao = Button(self.Container3)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao.bind("<Button-1>",self.RemoveCarro)
        self.decisao["command"] = self.RemoveCarro # Modelo
        self.decisao.pack(side=LEFT)

    def RemoveCarro(self,event): # Modelo
        self.decisao.destroy()
        self.mensagem2 = self.Controle.RemoveCarro(self.opcao.get()-1,self.mensagem2,self.locadora)
        self.Janela.destroy()

    def BuscarCarro(self): # Visao
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.mensagem = Label(self.Container2, text = "Qual atributo deseja verificar?: ", bg = "light blue")
        self.mensagem["font"] = ("Arial", "11")
        self.mensagem.pack()

        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.opcao = StringVar()
        self.opcao1 = ["Marca","Modelo","Cor","Ano","Placa","Id"]
        self.opcao.set(self.opcao1[0])
        OptionMenu(self.Container3,self.opcao,*self.opcao1).pack()

        self.Container4 = Frame(self.Janela)
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.decisao = Button(self.Container4)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao["command"] = self.BuscaCarros # Controle
        self.decisao.pack(side=LEFT)

        self.Container5 = Frame(self.Janela)
        self.Container5["padx"] = 20
        self.Container5['bg'] = "light blue"
        self.Container5.pack()

    def BuscaCarros(self): # Visao
        self.decisao.destroy()
        self.Container3.destroy()
        self.mensagem.destroy()
        if (self.opcao.get() == "Marca"): # Visao
            self.mensagem1 = Label (self.Container5, text = "Marca", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Modelo"): # Visao
            self.mensagem1 = Label (self.Container5, text = "Modelo", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Cor"): # Visao
            self.mensagem1 = Label (self.Container5, text = "Cor", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Ano"): # Visao
            self.mensagem1 = Label (self.Container5, text = "Ano", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Placa"): # Visao
            self.mensagem1 = Label (self.Container5, text = "Placa", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Id"): # Visao
            self.mensagem1 = Label (self.Container5, text ="Id", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        botao = Button(self.Container5)
        botao["text"] = ("Pesquisar")
        botao["width"] = 8
        botao["font"] = self.fontePadrao
        botao.bind("<Button-1>",self.MostraCarros)
        botao.pack(side = LEFT)

    def MostraCarros(self,event): # Controle
        self.mensagem2 = self.Controle.BuscarCarros(self.opcao.get(),self.locadora,self.verifica.get())
        self.Janela.destroy()

    def verificaOpcaoCarro(self,evet): # Controle
        if (self.opcao.get() == "Voltar para o Menu Principal"):
            self.Janela.destroy() # Visao
            self.menucarro = False

        elif (self.opcao.get() == "Cadastrar Carro"):
            self.CadastrarCarro()

        elif (self.opcao.get() == "Remover Carro" and (len(self.locadora.cars) > 0)):
            self.RemoverCarro()

        elif (self.opcao.get() == "Buscar Carro" and ((len(self.locadora.cars) > 0 or len(self.locadora.carsAlugados) > 0))):
            self.BuscarCarro()
        else:
            self.mensagem2 = "Nao existem carros na locadora para serem removidos, ou para serem mostrados!"
