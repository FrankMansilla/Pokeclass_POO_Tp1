from abc import ABCMeta, abstractmethod


class Stats(metaclass=ABCMeta):

    @abstractmethod
    def HP(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defence(self):
        pass

    @abstractmethod
    def velocity(self):
        pass
