import Locadora as Locadora
import MenuCarro as MenuCarro
import MenuLocacao as MenuLocacao
import Arquivos as Arquivos
import Carro as Carro
import Locacao as Locacao
from abc import ABC, abstractmethod

class Factory(ABC):
    # Janela // Modelo // Controle
    # Concrete para cada um deles

    @abstractmethod
    def Create_Menu(self):
        pass
    @abstractmethod
    def Create_Modelo(self):
        pass
    @abstractmethod
    def Create_Controle(self):
        pass

class ConcreteFactoryLocacao(factory):


class ConcreteFactoryCarro(Factory):
    def Create_Menu(self):
        return ConcreteMenuCarro()

    def Create_MLocacao(self):
        return ConcreteMenuLocacao()

    def Create_Locadora(self):
        return ConcreteLocadora()

    def Create_Arquivos(self):
        return ConcreteArquivos()
    
    def Create_Carro(self):
        return ConcreteCarro()
    
    def Create_Locacao(self):
        return ConcreteLocacao()


class AbstractMenuCarro(ABC):
    @abstractmethod
    def Criar_Menu_Carro(self):
        pass

class AbstractMenuLocacao(ABC):
    @abstractmethod
    def Criar_Menu_Locacao(self):
        pass

class AbstractLocadora(ABC):
    @abstractmethod
    def Criar_Locadora(self):
        pass

class AbstractArquivos(ABC):
    @abstractmethod
    def Criar_Arquivos(self):
        pass

class AbstractCarro(ABC):
    @abstractmethod
    def Criar_Carro(self):
        pass

class AbstractLocacao(ABC):
    @abstractmethod
    def Criar_Locacao(self):
        pass


class ConcreteMenuCarro(AbstractMenuCarro):
    def Criar_Menu_Carro(self):
        return MenuCarro.MenuCarro()

class ConcreteMenuLocacao(AbstractMenuLocacao):
    def Criar_Menu_Locacao(self):
        return MenuLocacao.MenuLocacao()

class ConcreteLocadora(AbstractLocadora):
    def Criar_Locadora(self):
        return Locadora.Locadora()

class ConcreteArquivos(AbstractArquivos):
    def Criar_Arquivos(self):
        return Arquivos.Arquivos.instancias()

class ConcreteCarro(AbstractCarro):
    def Criar_Carro(self):
        return Carro.Carro()

class ConcreteLocacao(AbstractLocacao):
    def Criar_Locacao(self):
        return Locacao.Locacao()
