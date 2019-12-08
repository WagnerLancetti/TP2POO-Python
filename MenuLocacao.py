from tkinter import *
from tkinter import ttk
import Carro as Carro
from random import randint
import ControleLocacao as ControleLocacao

class MenuLocacao:
    def __init__(self):
        self.Controle = ControleLocacao.ControleMenuLocacao()

    def Menulocacao(self,locadora): 
        self.fontepadrao = ("Arial","10")
        self.menuLoca = True
        self.locadora = locadora
        self.mensagem2 = ""
        while (self.menuLoca): # Visao
            self.Janela = Tk()
            self.Janela.title("Menu Locacao")
            self.Janela.geometry("700x400")
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
            self.opcao1 = ["Voltar ao Menu Principal", "Visualizar uma Locacao", "Criar uma nova Locacao", "Devolver um Carro da Locacao", "Devolver uma Locacao Completa","Exibir Tabela com Dados"]
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
            self.decisao["command"] = self.decideLocacao # Controle
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
        self.decisao.bind("<Button-1>",self.VisualizaLoca)
        self.decisao.pack(side=LEFT)

    def VisualizaLoca(self,event): # Controle
        self.mensagem2 = self.Controle.VisualizaLocacao(self.locadora,self.opcao.get()-1)
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
        self.decisao.bind("<Button-1>",self.verificaCriaLoca)
        self.decisao.pack()

    def verificaCriaLoca(self,event): # Controle
        self.mensagem2 = self.Controle.CriaLoca(self.locadora,self.opcao,self.nome.get(),self.data.get())
        self.Janela.destroy() # Visao


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

    def verificaLocaDelCar(self): # Visao
        self.Container2.destroy()
        self.Container3.destroy()
        self.decisao.destroy()

        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2["bg"] = "light blue"
        self.Container2.pack()

        self.tituloContainer2 = Label (self.Container2, text = "Escolha quais carros voce deseja excluir: ",bg = "light blue")
        self.tituloContainer2.pack()

        self.Container5 = Frame(self.Janela)
        self.Container5["padx"] = 20
        self.Container5["bg"] = "light blue"
        self.Container5.pack()
        self.opcao1 = IntVar()
        i = 0
        while (i < self.locadora.locacoes[self.opcao.get()-1].getTam()):
            Radiobutton(self.Container5,text = self.locadora.locacoes[self.opcao.get()-1].getCarro(i).toString(),font = self.fontepadrao, variable = self.opcao1, value = i + 1, bg = "light blue").pack()
            i = i + 1

        self.Container6 = Frame(self.Janela)
        self.Container6["padx"] = 20
        self.Container6['bg'] = "light blue"
        self.Container6.pack()

        self.decisao = Button(self.Container6)
        self.decisao["width"] = 8
        self.decisao["text"] = "Confirmar"
        self.decisao["font"] = self.fontepadrao
        self.decisao.bind("<Button-1>",self.DevolverCarros)
        self.decisao.pack()

    def DevolverCarros(self,event): # Controle
        self.mensagem2 = self.Controle.DevolverCarros(self.locadora,self.opcao.get()-1,self.opcao1.get()-1)
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
        self.decisao.bind("<Button-1>",self.verificaDelLoca)
        self.decisao.pack()


    def verificaDelLoca(self,event): # Controle
        self.mensagem2 = self.Controle.DevolverLoca(self.locadora,self.opcao.get()-1)
        self.Janela.destroy() # Visao

    def ExibirTabela(self):
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        self.Container5.destroy()
        self.Container2 = Frame(self.Janela)
        self.Container2.place(x = 20, y = 100, width = 750)

        self.dataCols = ('Locacoes', 'Cliente', 'Data','Quantidade de Carros Cadastrados')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.Container2)
        #self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        vsb = ttk.Scrollbar(orient="vertical",command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",command=self.tree.xview)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.Container2)
        hsb.grid(column=0, row=1, sticky='ew', in_=self.Container2)
        self.tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        self.data = []
        i = 0
        while (i < len(self.locadora.locacoes)):
            str1 = "Locacao "+str(i),self.locadora.locacoes[i].getCliente(),self.locadora.locacoes[i].getData(),self.locadora.locacoes[i].getTam()
            self.data.append(str1)
            i = i + 1
            
        for item in self.data:
            self.tree.insert('', 'end', values=item)
        
        self.Container3 = Frame(self.Janela)
        self.Container3["padx"] = 5
        self.Container3["bg"] = "light blue"
        self.Container3.place(x = 100, y = 370,width = 700)

        botao = Button(self.Container3)
        botao["width"] = 8
        botao["text"] = "Voltar"
        botao["command"] = self.Quit
        botao.pack()

    def Quit(self):
        self.Janela.destroy()

    def decideLocacao(self): # Controle
        if (self.opcao.get() == "Voltar ao Menu Principal"):
            self.Janela.destroy() # Visao
            self.menuLoca = False

        elif (self.opcao.get() == "Visualizar uma Locacao" and (len(self.locadora.locacoes)>0)):
            self.VisualizarLocacao()

        elif (self.opcao.get() == "Criar uma nova Locacao" and (len(self.locadora.cars)>0)):
            self.CriarLocacao()

        elif (self.opcao.get() == "Devolver um Carro da Locacao" and (len(self.locadora.locacoes)>0)):
            self.DevolverCarro()

        elif (self.opcao.get() == "Devolver uma Locacao Completa" and (len(self.locadora.locacoes)>0)):
            self.DevolverLocacao()

        elif (self.opcao.get() == "Exibir Tabela com Dados" and (len(self.locadora.locacoes)>0)):
            self.ExibirTabela()

        else:
            self.mensagem2 = "Nao existe locacoes para serem acessadas, ou carros para serem alugados na locadora."
