import Carro as Carro
import time
from random import randint
from tkinter import *
import time

class MenuCarro:
    def __init__ (self): # Menu Inicial de Carro
        self.locadora = None
        self.menucarro = True
        self.Janela = None
        self.verifica = None
        self.fontePadrao = ("Arial", "10")   
        self.Container1 = None
        self.Container2 = None
        self.Container3 = None
        self.Container4 = None
        self.Container5 = None
        self.Container6 = None
        self.Container7 = None
        self.Container8 = None
        self.Container9 = None
        self.tituloContainer1 = None
        self.tituloContainer7 = None
        self.tituloContainer2 = None
        self.tituloContainer3 = None
        self.tituloContainer4 = None
        self.tituloContainer5 = None
        self.tituloContainer6 = None
        self.tituloContainer7 = None
        self.mensagem2 = ""
        self.opcao = None
        self.decisao = None
        self.Container8 = None
        self.mensagem = None
        self.placa = None
        self.marca = None
        self.cor = None
        self.modelo = None
        self.ano = None
        self.mensagem1 = None


    def Menucarro(self,locadora):
        self.locadora = locadora
        self.mensagem2 = ""
        while (self.menucarro):
            self.Janela = Tk()
            self.Janela.title("Menu Carro")
            self.Janela.geometry("500x400")
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
            self.decisao["command"] = self.verificaOpcaoCarro
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
        self.decisao["command"] = self.verificacaoCadastro
        self.decisao.pack(side=LEFT)

        self.Container9 = Frame(self.Janela)
        self.Container9["padx"] = 20
        self.Container9["bg"] = "light blue"
        self.Container9.pack()

        self.mensagem = Label(self.Container9, text = "", font = self.fontePadrao, bg = "light blue")

    def verificacaoCadastro(self): # Controle
        verifica = 0
        self.mensagem["text"] = ""
        if (self.placa.get() == ''):
            self.mensagem["text"] = "*Digite uma Placa"
            verifica = verifica + 1
        if (self.marca.get() == ''):
            self.mensagem["text"] = self.mensagem["text"] + "\n*Digite uma Marca"
            verifica = verifica + 1
        if (self.cor.get() == ''):
            self.mensagem["text"] = self.mensagem["text"] + "\n*Digite uma Cor*"
            verifica = verifica + 1
        if (self.modelo.get() == ''):
            self.mensagem["text"] = self.mensagem["text"] + "\n*Digite um Modelo*"
            verifica = verifica + 1
        if (self.ano.get() == ''):
            self.mensagem["text"] = self.mensagem["text"] + "\n*Digite o ano*"
        if (verifica == 0):
            self.CadastraCarro()
        else:
            self.mensagem.destroy()
            self.mensagem.pack()
        
        
    def CadastraCarro(self): # Modelo
        if(self.VerificaPlaca()):
            self.locadora.cars.append(Carro.Carro(str(self.marca.get()),str(self.placa.get()),str(self.cor.get()),str(self.modelo.get()),int(self.ano.get()),randint(0,1000000)))
            self.mensagem2 = "Carro Cadastrado com Sucesso!"
            self.Janela.destroy()
        else:
            self.mensagem2 = "Essa placa já existe no sistema."
            self.Janela.destroy()

    def VerificaPlaca(self):
        i = 0
        while(i < len(self.locadora.cars)):
            if (self.locadora.cars[i].getPlaca() == self.placa.get()):
                return False
            i = i + 1
        return True
                

    def RemoverCarro(self): # Visao
        if (len(self.locadora.cars) > 0):
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
            self.decisao["command"] = self.RemoveCarro # Modelo
            self.decisao.pack(side=LEFT)

        else:
            self.mensagem2 = "Não há carros na locadora!"
    def RemoveCarro(self): # Modelo
        del(self.locadora.cars[int(self.opcao.get()) - 1])
        self.mensagem2 = "Carro removido com sucesso!"
        self.Janela.destroy()



    def BuscarCarro(self):
        self.tituloContainer5.destroy()
        self.tituloContainer2.destroy()
        self.tituloContainer3.destroy()
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()

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
        self.decisao["command"] = self.BuscaCarros
        self.decisao.pack(side=LEFT)

        self.Container5 = Frame(self.Janela)
        self.Container5["padx"] = 20
        self.Container5['bg'] = "light blue"
        self.Container5.pack()

        self.Container6 = Frame(self.Janela)
        self.Container6["padx"] = 20
        self.Container6['bg'] = "light blue"
        self.Container6.pack()


    def BuscaCarros(self): # Controle
        self.decisao.destroy()
        self.Container3.destroy()
        self.mensagem.destroy()
        if (self.opcao.get() == "Marca"):
            self.mensagem1 = Label (self.Container5, text = "Marca", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Modelo"):
            self.mensagem1 = Label (self.Container5, text = "Modelo", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Cor"):
            self.mensagem1 = Label (self.Container5, text = "Cor", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Ano"):
            self.mensagem1 = Label (self.Container5, text = "Ano", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Placa"):
            self.mensagem1 = Label (self.Container5, text = "Placa", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            self.verifica = Entry(self.Container5)
            self.verifica["width"] = 30
            self.verifica["font"] = self.fontePadrao
            self.verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Id"):
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
        botao["command"] = self.MostraCarros
        botao.pack(side = LEFT)

    def MostraCarros(self):
        if (self.opcao.get() == "Id" or self.opcao.get() == "Ano"):
            especificidade = self.locadora.BuscarCarro(self.opcao.get(),int(self.verifica.get()))
        else:
            especificidade = self.locadora.BuscarCarro(self.opcao.get(),self.verifica.get())
        if (len(especificidade) == 0):
            self.mensagem2 = "Nao exisite nenhum carro com essa especificacao."
        else:
            i = 0
            self.mensagem2 = ""
            while(i < len(especificidade)):
                self.mensagem2 = self.mensagem2 + especificidade[i].toString() + "\n"
                i = i + 1
            del (especificidade[:])
        self.Janela.destroy()

    def verificaOpcaoCarro(self): # Controle
        if (self.opcao.get() == "Voltar para o Menu Principal"):
            self.Janela.destroy()
            self.menucarro = False

        if (self.opcao.get() == "Cadastrar Carro"):
            self.CadastrarCarro()

        if (self.opcao.get() == "Remover Carro"):
            self.RemoverCarro()

        if (self.opcao.get() == "Buscar Carro"):
            self.BuscarCarro()
