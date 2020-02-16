from abc import ABCMeta, abstractmethod


class DomainModel(metaclass=ABCMeta):
    # the metaclass attribute must always be set as a class variable

    def __init__(self):
        pass

    @abstractmethod
    def from_dict(self):
        pass
