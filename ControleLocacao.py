import ModeloLocacao as ModeloLocacao

class ControleMenuLocacao():
    def __init__(self):
        self.Modelo = ModeloLocacao.ModeloMenuCarro()

    def VisualizaLocacao(self,locadora,indice):
        mensagem = ""
        mensagem = self.Modelo.VisualizarLocacao(locadora,mensagem,indice)
        return mensagem
    
    def CriaLoca(self,locadora,indice,nome,data):
        carros = []
        indices = []
        i = 0
        while (i < len(indice)):
            if (indice[i].get() == 1):
                locadora.cars[i].setAlugado(True)
                locadora.carsAlugados.append(locadora.cars[i])
                carros.append(locadora.cars[i])
                indices.append(locadora.cars[i].getPlaca())
            i = i + 1
        self.Modelo.CriaLoca(locadora,indices,carros,nome,data)
        del(carros[:])
        return "Locacao Criada com Sucesso!"

    def DevolverCarros(self,locadora,ILocacao,ICarros):
        mensagem = ""
        mensagem = self.Modelo.DevolverCarro(locadora,ILocacao,ICarros)
        return mensagem
    
    def DevolverLoca(self,locadora,ILoca):
        self.Modelo.DevolverLoca(locadora,ILoca)
        return "Locacao devolvida com sucesso!"