from abc import ABC, abstractmethod

class PreguntaRepository(ABC):
    @abstractmethod
    def obtener_todas(self):
        pass

    @abstractmethod
    def agregar(self, pregunta):
        pass

    @abstractmethod
    def eliminar(self, pregunta_id):
        pass