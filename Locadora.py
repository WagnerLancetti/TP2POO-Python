import Carro
import Locacao as Locacao
import Entidade

class Locadora(Entidade.Entidade):
    # ATRIBUTOS DECLARADOS
    def __init__(self):
        super().__init__()
        self.cars = [] # Ira guardar os carros que podem ser alugados
        self.carsAlugados = [] # Ira guardar os carros que foram alugados nas locacoes
        self.locacoes = [] # Ira guardar todoas as locacoes que existem na locadora

    # METODOS 
    def ListarCarrosParaAlugar(self, i): # Retorna para o usuario cada carro que pode ser alugado na locadora
        return self.cars[i]


    def CriarLocacao(self,carros,nome,data,num):
        locacao = Locacao.Locacao(nome,data,num) # Cria uma nova locacao com os dados do cliente
        i = 0
        while (i < len(carros)): # Adiciona todos os carros que o usuario queria alugar
            locacao.addCarros(carros[i])
            i = i + 1
        self.locacoes.append(locacao)


    def DevolverCarro(self,entrada,entrada2):
        self.locacoes[entrada].getCarro(entrada2).setAlugado(False) # Muda o status do carro para desalugado
        j = 0
        while (j < len(self.carsAlugados)): # Acha e apaga o carro no vetor que possui os carros alugados
            if (self.locacoes[entrada].getCarro(entrada2).getPlaca() == self.carsAlugados[j].getPlaca()):
                self.carsAlugados[j].setAlugado(False) 
                self.cars.append(self.carsAlugados[j]) # Volta o carro para o vetor de carros nao alugados
                del(self.carsAlugados[j]) # Apaga o carro do vetor de carros alugados
                j = len(self.carsAlugados)
            j = j + 1
        self.locacoes[entrada].DelCarro(entrada2) # Apaga o carros da locacao


    def DevolverLocacao(self,entrada):
        i = 0
        # Antes de apagar a locacao, e necessario voltar todos os carros que existiam la antes para o vetor de carros para alugar na locadora
        while (i < self.locacoes[entrada].getTam()):
            j = 0
            while (j < len(self.carsAlugados)):
                if (self.carsAlugados[j].getPlaca() == self.locacoes[entrada].getCarro(i).getPlaca()): # Apaga o carro no vetor de carros Alugados
                    self.locacoes[entrada].getCarro(i).setAlugado(False)
                    self.cars.append(self.locacoes[entrada].getCarro(i) ) # Guarda o carro no vetor de carros para alugar
                    del(self.carsAlugados[j]) # Apaga o carro no vetor de carros alugados
                    j = j + len(self.carsAlugados)
                j = j + 1 # Percorre todos os carros que existem no vetor de carros Alugados
            i = i + 1 # Percorre todos os carros que existem na locacao
        del(self.locacoes[entrada]) # Apaga a locacao


    def BuscarCarro(self,entrada,valor): # Busca carros com caracteristicas iguais as que o usuario escolheu no Menu
        especificidade = []
        Carro0 = Carro.Carro()
        if (entrada == 'Marca'): # MARCA
            i = 0
            while (i < len(self.cars)): # Busca carros em carros nao alugados
                Carro0 = self.cars[i]
                if (Carro0.getMarca() == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while(i < len(self.carsAlugados)): # Busca carros em carros alugados
                Carro0 = self.carsAlugados[i]
                if (Carro0.getMarca() == valor):
                    especificidade.append(Carro0)
                i = i + 1

        elif (entrada == 'Modelo'): # MODELO
            i = 0
            while (i < len(self.cars)):
                Carro0 = self.cars[i]
                if (Carro0.getModelo() == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while(i < len(self.carsAlugados)):
                Carro0 = self.carsAlugados[i]
                if (Carro0.getModelo() == valor):
                    especificidade.append(Carro0)
                i = i + 1

        elif (entrada == 'Cor'): # COR
            i = 0
            while (i < len(self.cars)):
                Carro0 = self.cars[i]
                if (Carro0.getCor() == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while (i < len(self.carsAlugados)):
                Carro0 = self.carsAlugados[i]
                if (Carro0.getCor() == valor):
                    especificidade.append(Carro0)
                i = i + 1

        elif (entrada == 'Ano'): # ANO
            i = 0
            while (i < len(self.cars)):
                Carro0 = self.cars[i]
                if (Carro0.getAno() == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while (i < len(self.carsAlugados)):
                Carro0 = self.carsAlugados[i]
                if (Carro0.getAno() == valor):
                    especificidade.append(Carro0)
                i = i + 1

        elif (entrada == 'Placa'): # PLACA
            i = 0
            while (i < len(self.cars)):
                Carro0 = self.cars[i]
                if (Carro0.getPlaca() == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while (i < len(self.carsAlugados)):
                Carro0 = self.carsAlugados[i]
                if (Carro0.getPlaca() == valor):
                    especificidade.append(Carro0)
                i = i + 1

        elif (entrada == 'Id'): # ID
            i = 0
            while (i < len(self.cars)):
                Carro0 = self.cars[i]
                if (Carro0.identificador == valor):
                    especificidade.append(Carro0)
                i = i + 1
            i = 0
            while (i < len(self.carsAlugados)):
                Carro0 = self.carsAlugados[i]
                if (Carro0.identificador == valor):
                    especificidade.append(Carro0)
                i = i + 1

        return especificidade # Retorna para o Menu a lista de carros iguais