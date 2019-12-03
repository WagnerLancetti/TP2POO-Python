import Locadora
import Entidade

class Carro(Entidade.Entidade):
    # CONSTRUTOR
    def __init__(self,Marca=None,Placa=None,Cor=None,Modelo=None,Ano=-1,num=-1): # Construtor padrao e com parametros de entrada
        # Declaracao de todos os atributos privados
        super().__init__()
        self.__Marca = Marca
        self.__Placa = Placa
        self.__Cor = Cor
        self.__Modelo = Modelo
        self.__Ano = Ano
        self.__Alugado = False
        self.identificador = num

    # METODOS SETTERS E GETTERS
    def isAlugado(self):
        return self.__Alugado

    def setAlugado(self,Alugado):
        self.__Alugado = Alugado

    def getMarca(self):
        return self.__Marca

    def setMarca(self,Marca):
        self.__Marca = Marca

    def getPlaca(self):
        return self.__Placa

    def setPlaca(self,Placa):
        self.__Placa = Placa

    def getCor(self):
        return self.__Cor

    def setCor(self,Cor):
        self.__Cor = Cor

    def getModelo(self):
        return self.__Modelo

    def setModelo(self,Modelo):
        self.__Modelo = Modelo

    def getAno(self):
        return self.__Ano

    def setAno(self,Ano):
        self.__Ano = Ano

    # METODOS
    def toString(self): # Criacao do metodo que ira mostrar para o usuario as caracteristicas de cada carro cadastrado
        return "Carro: "+self.getMarca()+", "+self.getModelo()+", "+str(self.getAno())+", "+self.getCor()+", placa "+self.getPlaca()+", ID do carro "+str(self.identificador)+"."
