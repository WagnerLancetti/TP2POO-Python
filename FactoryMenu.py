from abc import ABC, abstractmethod

class FactoryMenu(ABC):
    @abstractmethod
    def Create_MCarro(self):
        pass

    def Create_MLocacao(self):
        pass

    def Create_Locadora(self):
        pass

class ConcreteFactoryMenu(FactoryMenu):
    def Create_MCarro(self):
        return ConcreteMenuCarro()

    def Create_MLocacao(self):
        return ConcreteMenuLocacao()

    def Create_Locadora(self):
        return ConcreteLocadora()

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

class ConcreteMenuCarro(AbstractMenuCarro):
    def Criar_Menu_Carro(self):
        return MenuCarro.MenuCarro()

class ConcreteMenuLocacao(AbstractMenuLocacao):
    def Criar_Menu_Locacao(self):
        return Menulocacao.MenuLocacao()

class ConcreteLocadora(AbstractLocadora):
    def Criar_Locadora(self):
        return Locadora.Locadora()
