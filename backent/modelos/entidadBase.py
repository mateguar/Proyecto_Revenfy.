from abc import ABC, abstractmethod

class EntidadBase(ABC):
    @abstractmethod
    def guardarEnBase(self, conexion):
        """Método abstracto que obliga a las clases hijas a definir cómo guardarse."""
        pass