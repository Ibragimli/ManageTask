from abc import abstractmethod,ABC
from Domain.Entities import Task



class IRepository(ABC):
    @abstractmethod
    # def __init__(self):
    def Get(self,id):
        pass
    def GetAll(self):
        pass
    def Create(self,task:Task):
        pass
    def Update(self,task:Task):
        pass
    def Delete(self,id):
        pass

