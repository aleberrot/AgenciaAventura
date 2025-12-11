from datetime import datetime

class PaqueteDTO:
    """Docstring for PaqueteDTO"""
    def __init__(self, id_paquete: int, nombre: str, fecha_inicio: datetime, fecha_fin: datetime, precio_total: float):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total
    

