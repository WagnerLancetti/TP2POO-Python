from random import randint
import Carro as Carro

class ModeloMenuCarro:

    def CadastraCarro(self,marca,placa,cor,modelo,ano,locadora): # Modelo
        if(self.VerificaPlaca(locadora,placa)): # Controle
            locadora.cars.append(Carro.Carro(str(marca),str(placa),str(cor),str(modelo),ano,randint(0,1000000)))
            return True
        else:
            return False
    def VerificaPlaca(self,locadora,placa): # Modelo
        i = 0
        while(i < len(locadora.cars)):
            if (locadora.cars[i].getPlaca() == placa):
                return False
            i = i + 1
        return True
    
    def RemoverCarro(self,indice,locadora):
        del(locadora.cars[indice])
    
    def BuscarCarros(self,locadora,opcao,verifica):
        return locadora.BuscarCarro(opcao,verifica) # Modelo