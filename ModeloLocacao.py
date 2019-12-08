from random import randint

class ModeloMenuCarro:
    
    def VisualizarLocacao(self,locadora,mensagem,indice):
        mensagem = "Locacao do cliente "+locadora.locacoes[indice].getCliente() +" alugada em "+locadora.locacoes[indice].getData()+". "+"\n\nCarros na locacao: "
        i = 0
        while (i < locadora.locacoes[indice].getTam()):
            mensagem = mensagem + "\n"+locadora.locacoes[indice].getCarro(i).toString()
            i = i + 1
        return mensagem
    
    def CriaLoca(self,locadora,indices,carros,nome,data):
        i = 0
        while (i < len(indices)):
            j = 0
            while (j < len(locadora.cars)):
                if (indices[i] == locadora.cars[j].getPlaca()):
                    del(locadora.cars[j])
                j = j + 1
            i = i + 1
        locadora.CriarLocacao(carros,nome,data,randint(0,1000000))
        return 

    def DevolverCarro(self,locadora,ILoca,ICarro):
        locadora.DevolverCarro(ILoca, ICarro)
        if (locadora.locacoes[ILoca].getTam() <= 0):
            del(locadora.locacoes[ILoca])
            return "Carro devolvido com sucesso e locacao apagada!"
        else:
            return "Carro devolvido com sucesso!"

    def DevolverLoca(self,locadora,ILoca):
        locadora.DevolverLocacao(ILoca)
        return        