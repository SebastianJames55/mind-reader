from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def train(self, data):
        pass
