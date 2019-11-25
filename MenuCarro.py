from tkinter import *
import time

class MenuCarro:
    def __init__ (self): # Menu Inicial de Carro
        self.menucarro = True
        self.Janela = None
        self.fontePadrao = ("Arial", "10")   
        self.Container1 = None
        self.Container7 = None
        self.Container2 = None
        self.Container3 = None
        self.Container4 = None
        self.Container5 = None
        self.Container6 = None
        self.tituloContainer1 = None
        self.tituloContainer7 = None
        self.tituloContainer2 = None
        self.tituloContainer3 = None
        self.tituloContainer4 = None
        self.tituloContainer5 = None
        self.tituloContainer6 = None
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


    def Menucarro(self):
        while (self.menucarro):
            self.Janela = Tk()
            self.Janela.title("Menu Carro")
            self.Janela.geometry("500x300")
            self.Janela['bg'] = "light blue"
            self.Janela.resizable(0,0)

            self.Container1 = Frame(self.Janela)
            self.Container1["pady"] = 10 # Distancia do container no eixo y
            self.Container1['bg'] = "light blue"
            self.Container1.pack()

            self.tituloContainer1 = Label(self.Container1, text = "Menu Carro",bg = "light blue")
            self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
            self.tituloContainer1.pack()

            self.Container2 = Frame(self.Janela) # Mensagem para o usuario
            self.Container2["padx"] = 20 # Distancia do container no eixo x
            self.Container2['bg'] = "light blue"
            self.Container2.pack()

            self.tituloContainer2 = Label(self.Container2,bg = "light blue", text = "O que voce deseja fazer? \n[Pode digitar o indice ou a opcao]\n",font = self.fontePadrao)
            self.tituloContainer2["font"] = ("Arial", "12")
            self.tituloContainer2.pack(side=LEFT)

            self.Container3 = Frame(self.Janela) # Opcoes que o usuario pode fazer
            self.Container3["padx"] = 20 # Distancia do container no eixo x
            self.Container3['bg'] = "light blue"
            self.Container3.pack()

            self.opcao = IntVar()
            Radiobutton(self.Container3, text = "Voltar ao Menu Principal", variable = self.opcao, value = 1, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Cadastrar Carro", variable = self.opcao, value = 2, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Remover Carro", variable = self.opcao, value = 3, bg = "light blue", font = ("Arial", "12")).pack()
            Radiobutton(self.Container3, text = "Buscar Carro", variable = self.opcao, value = 4, bg = "light blue", font = ("Arial", "12")).pack()

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

            self.Janela.mainloop()    
    
    def CadastrarCarro(self): # Visao
        self.Janela = Tk()
        self.Janela.title("Cadastro do Carro")
        self.Janela.geometry("500x400")
        self.Janela['bg'] = "light blue"
        self.Janela.resizable(0,0)

        self.Container1 = Frame(self.Janela)
        self.Container1["pady"] = 10
        self.Container1['bg'] = "light blue"
        self.Container1.pack()

        self.tituloContainer1 = Label(self.Container1, text ="Cadastro de Carro",bg = "light blue")
        self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
        self.tituloContainer1.pack()

        self.Container7 = Frame(self.Janela)
        self.Container7["padx"] = 20
        self.Container7['bg'] = "light blue"
        self.Container7.pack()

        self.mensagem = Label(self.Container7, text = "Digite as informacoes do novo carro: \n",bg = "light blue")
        self.mensagem["font"] = ("Arial", "12")
        self.mensagem.pack()

        self.Container2 = Frame(self.Janela) # Placa
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label(self.Container2, text ="Placa     ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer2.pack(side=LEFT)

        self.placa = Entry(self.Container2)
        self.placa["width"] = 30
        self.placa["font"] = self.fontePadrao
        self.placa.pack(side=LEFT)

#        verifica = Button(self.Container2)
 #       verifica["text"] = "Verificar"
  #      verifica["font"] = self.fontePadrao
   #     verifica["width"] = 6
        #verifica["command"] = self.VerificaPlaca # Modelo (M)
    #    verifica.pack(side=LEFT)

        self.Container3 = Frame(self.Janela) # Marca
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.tituloContainer3 = Label(self.Container3, text ="Marca   ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer3.pack(side=LEFT)

        self.marca = Entry(self.Container3)
        self.marca["width"] = 30
        self.marca["font"] = self.fontePadrao
        self.marca.pack(side=LEFT)

        self.Container4 = Frame(self.Janela) # Cor
        self.Container4["padx"] = 20
        self.Container4['bg'] = "light blue"
        self.Container4.pack()

        self.tituloContainer4 = Label(self.Container4, text ="Cor       ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer4.pack(side=LEFT)

        self.cor = Entry(self.Container4)
        self.cor["width"] = 30
        self.cor["font"] = self.fontePadrao
        self.cor.pack(side=LEFT)

        self.Container5 = Frame(self.Janela) # Modelo
        self.Container5["padx"] = 20
        self.Container5['bg'] = "light blue"
        self.Container5.pack()

        self.tituloContainer5 = Label(self.Container5, text ="Modelo", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer5.pack(side=LEFT)
        
        self.modelo = Entry(self.Container5)
        self.modelo["width"] = 30
        self.modelo["font"] = self.fontePadrao
        self.modelo.pack(side=LEFT)    

        self.Container6 = Frame(self.Janela) # Ano
        self.Container6["padx"] = 20
        self.Container6['bg'] = "light blue"
        self.Container6.pack()

        self.tituloContainer6 = Label(self.Container6, text ="Ano       ", font = self.fontePadrao,bg = "light blue")
        self.tituloContainer6.pack(side=LEFT)

        self.ano = Entry(self.Container6)
        self.ano["width"] = 30
        self.ano["font"] = self.fontePadrao
        self.ano.pack(side=LEFT)

        self.Container7= Frame(self.Janela)
        self.Container7["padx"] = 20
        self.Container7['bg'] = "light blue"
        self.Container7.pack()
        
        self.Container8 = Frame(self.Janela)
        self.Container8["padx"] = 20
        self.Container8['bg'] = "light blue"
        self.Container8.pack()

        verifica = Button(self.Container7)
        verifica["text"] = "Verificar"
        verifica["font"] = self.fontePadrao
        verifica["width"] = 6
        #verifica["command"] = self.VerificaPlaca # Modelo (M)
        verifica.pack(side=LEFT)

        self.decisao = Button(self.Container7)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao["command"] = self.verificacaoCadastro
        self.decisao.pack(side=LEFT)


        self.Janela.mainloop()

    def verificacaoCadastro(self):
        verifica = 0
        if (self.placa.get() == ''):
            self.mensagem1 = Label(self.Container8,text ="*Digite uma Placa*", font =self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
            verifica = verifica + 1
        #elif (self.verificaPlaca(self.placa.get())):
          #  verifica = verifica + 1
           # self.mensagem1 = Label(self.Container8,text ="*Essa placa ja existe*", font =self.fontePadrao)
          #  self.mensagem1.pack(side=LEFT)
        if (self.marca.get() == ''):
            self.mensagem1 = Label(self.Container8,text ="*Digite uma Marca*", font =self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
            verifica = verifica + 1
        if (self.cor.get() == ''):
            self.mensagem1 = Label(self.Container8,text ="*Digite uma Cor*", font =self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
            verifica = verifica + 1
        if (self.modelo.get() == ''):
            self.mensagem1 = Label(self.Container8,text ="*Digite um Modelo*", font =self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
            verifica = verifica + 1
        if (self.ano.get() == ''):
            self.mensagem1 = Label(self.Container8,text ="*Digite o Ano*", font =self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
        if (verifica == 0):
            self.mensagem1 = Label(self.Container8,text="Carro Cadastrado com Sucesso!", font=self.fontePadrao,bg = "light blue")
            self.mensagem1.pack()
            self.Janela.destroy()
        
        
    def RemoverCarro(self): # Visao
        self.Janela = Tk()
        self.Janela.title("Remocao de Carro")
        self.Janela.geometry("500x300")
        self.Janela['bg'] = "light blue"

        self.Container1 = Frame(self.Janela)
        self.Container1["pady"] = 10
        self.Container1['bg'] = "light blue"
        self.Container1.pack()

        self.tituloContainer1 = Label (self.Container1, text = "Remocao de Carro",bg = "light blue")
        self.tituloContainer1["font"] = ("Arial", "30", "bold" , "underline")
        self.tituloContainer1.pack()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        self.mensagem1 = Label(self.Container2,text = "Escolha qual carro deseja remover: \n",bg = "light blue")
        self.mensagem1["font"] = ("Arial","15")
        self.mensagem1.pack()

        self.opcao = IntVar()
        Radiobutton(self.Container2, text = "Teste", variable = self.opcao, value = 1, bg = "light blue").pack()
        #while (i < len(locadora.cars)):
         #   Radiobutton(self.Container2,text = locadora.ListarCarrosParaAlugar(i).toString(), variable = self.opcao, value = i + 1).pack()

        self.Container3 = Frame (self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.decisao = Button(self.Container3)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao["command"] = self.RemoveCarro
        self.decisao.pack(side=LEFT)

        self.Janela.mainloop()

    def RemoveCarro(self):
        # del (locadora.cars[self.opcao.get()]
        self.Janela.destroy()
    
    def BuscarCarro(self):
        self.Janela = Tk()
        self.Janela.title("Buscar Carro")
        self.Janela.geometry("500x350")
        self.Janela['bg'] = "light blue"
        self.Janela.resizable(0,0)

        self.Container1 = Frame(self.Janela)
        self.Container1["pady"] = 10
        self.Container1['bg'] = "light blue"
        self.Container1.pack()


        self.tituloContainer1 = Label (self.Container1, text = "Buscar Carros",bg = "light blue")
        self.tituloContainer1["font"] = ("Arial", "30", "bold" , "underline")
        self.tituloContainer1.pack()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = "light blue"
        self.Container2.pack()

        

        self.mensagem = Label(self.Container2, text = "Marque o atributo que voce deseja verificar: ", bg = "light blue")
        self.mensagem["font"] = ("Arial", "11")
        self.mensagem.pack()
        
        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 20
        self.Container3['bg'] = "light blue"
        self.Container3.pack()

        self.opcao = IntVar()
        Radiobutton(self.Container3, text = "Marca", variable = self.opcao, value = 1, font = ("Arial", "12"), bg = "light blue").pack()
        Radiobutton(self.Container3, text = "Modelo", variable = self.opcao, value = 2, font = ("Arial", "12"), bg = "light blue").pack()
        Radiobutton(self.Container3, text = "Cor", variable = self.opcao, value = 3, font = ("Arial", "12"), bg = "light blue").pack()
        Radiobutton(self.Container3, text = "Ano", variable = self.opcao, value = 4, font = ("Arial", "12"), bg = "light blue").pack()
        Radiobutton(self.Container3, text = "Placa", variable = self.opcao, value = 5, font = ("Arial", "12"), bg = "light blue").pack()
        Radiobutton(self.Container3, text = "Id ", variable = self.opcao, value = 6, font = ("Arial", "12"), bg = "light blue").pack()

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

        self.Janela.mainloop()

    def BuscaCarros(self):
        self.decisao.forget()
        if (self.opcao.get() == 1):
            self.mensagem1 = Label (self.Container5, text = "Marca", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        elif (self.opcao.get() == 2):
            self.mensagem1 = Label (self.Container5, text = "Modelo", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        elif (self.opcao.get() == 3):
            self.mensagem1 = Label (self.Container5, text = "Cor", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        elif (self.opcao.get() == 4):
            self.mensagem1 = Label (self.Container5, text = "Ano", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        elif (self.opcao.get() == "Placa" or self.opcao.get() == '5'):
            self.mensagem1 = Label (self.Container5, text = "Placa", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        elif (self.opcao.get() == 6):
            self.mensagem1 = Label (self.Container5, text ="Id", bg = "light blue", font = self.fontePadrao)
            self.mensagem1.pack(side = LEFT)
            verifica = Entry(self.Container5)
            verifica["width"] = 30
            verifica["font"] = self.fontePadrao
            verifica.pack(side = LEFT)

        botao = Button(self.Container5)
        botao["text"] = ("Pesquisar")
        botao["width"] = 8
        botao["font"] = self.fontePadrao
        botao.pack(side = LEFT)

    def verificaOpcaoCarro(self): # Controle
        if (self.opcao.get() == 1):
            self.Janela.destroy()
            self.menucarro = False

        if (self.opcao.get() == 2):
            self.Janela.destroy()
            self.CadastrarCarro()

        if (self.opcao.get() == 3):
            self.Janela.destroy()
            self.RemoverCarro()

        if (self.opcao.get() == 4):
            self.Janela.destroy()
            self.BuscarCarro()