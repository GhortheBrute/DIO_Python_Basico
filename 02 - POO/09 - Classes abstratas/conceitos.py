from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def desligar(self):
        print("Ligando TV")

    def ligar(self):
        print("Desligando TV")


class ControleArCondicioando(ControleRemoto):

    def ligar(self):
        pass

    def desligar(self):
        pass


controle = ControleTV()
controle.ligar()
controle.desligar()
