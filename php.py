import abc


class BaseCar(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def drive(self):
        pass
    
    @abc.abstractmethod
    def __add__(self, obj):
        pass