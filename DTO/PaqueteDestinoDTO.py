from typing import List
from DTO.DestinoDTO import DestinoDTO
from datetime import datetime

class PaqueteDestinoDTO:
	"""docstring for PaqueteDestinoDTO"""
	def __init__(self, id_paquete: int, nombre: str, destinos: List[DestinoDTO], fecha_inicio: datetime, fecha_fin: datetime, precio_total: float):
		# TODO terminar constructor
		self.id_paquete = id_paquete
		self.nombre = nombre
		self.destinos = destinos
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		self.precio_total = precio_total
	def calcular_precio() -> float:
		...

	def verificar_disponibilidad(fecha: datetime) -> bool:
		...

	def crear() -> bool:
		...	