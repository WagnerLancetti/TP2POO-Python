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
    def Create_Modelo(self,opcao):
        pass
    @abstractmethod
    def Controle(self,opcao):
        pass

class ConcreteFactoryLocacao(Factory):
    def Create_Menu(self):
        return ConcreteMenuLocacao().Criar_Menu_Locacao()
    def Create_Modelo(self,opcao):
        pass
    def Controle(self):
        pass

class ConcreteFactoryCarro(Factory):
    def Create_Menu(self):
        return ConcreteMenuCarro().Criar_Menu_Carro()

    def Create_Modelo(self,opcao):
        pass

    def Controle(self,opcao):
        pass


class AbstractMenuCarro(ABC):
    @abstractmethod
    def Criar_Menu_Carro(self):
        pass

class AbstractMenuLocacao(ABC):
    @abstractmethod
    def Criar_Menu_Locacao(self):
        pass


class ConcreteMenuCarro(AbstractMenuCarro):
    def Criar_Menu_Carro(self):
        return MenuCarro.MenuCarro()

class ConcreteMenuLocacao(AbstractMenuLocacao):
    def Criar_Menu_Locacao(self):
        return MenuLocacao.MenuLocacao()
