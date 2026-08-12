from abc import ABC, abstractmethod

class ExportStrategy(ABC):
    @abstractmethod
    def export(self, invoices):
        ...