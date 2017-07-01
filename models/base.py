from abc import ABCMeta, abstractmethod


class GAN(metaclass=ABCMeta):
    @abstractmethod
    def build(self):
        pass
