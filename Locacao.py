import Entidade

class Locacao(Entidade.Entidade):
    # ATRIBUTOS DECLARADOS
    def __init__(self, cliente = None, data = None,num = 0):
        super().__init__()
        self.__cliente = cliente # Nome do cliente
        self.__data = data # Data que a locacao foi feita
        self.__carros = [] # Vetor que ira guardar quais carros pertence aquela locacao
        self.identificador = num
    
    # METODOS GETTERS E SETTERS 
    def getTam(self): # Retorna quantos carros existem na locacao
        return len(self.__carros)

    def getCarro(self,entrada): # Retorna um carro especifico da locacao
        return self.__carros[entrada]

    def getCliente(self):
        return self.__cliente

    def getData(self):
        return self.__data

    def setCliente(self,Cliente):
        self.__cliente = Cliente

    def setData(self,Data):
        self.__data = Data
        
    # METODOS 
    def toString(self):
        return "Locacao do cliente "+self.getCliente()+" que possue "+str(self.getTam())+" carro(s) alugado(s). A locacao possui ID "+str(self.identificador)+"."
    
    def addCarros(self,Carro): # Guarda um carro na locacao *addcarro*
        self.__carros.append(Carro)

    def DelCarro(self,entrada):
        del(self.__carros[entrada])