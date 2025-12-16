from typing import List
from DTO.DestinoDTO import DestinoDTO
from datetime import datetime
from DTO.PaqueteDTO import PaqueteDTO
from DTO.DestinoDTO import DestinoDTO

class PaqueteDestinoDTO:
	"""docstring for PaqueteDestinoDTO"""
	
	def __init__(self, id_paquete: int, id_destino: int):
		self.id_paquete = id_paquete
		self.id_destino = id_destino

	def calcular_precio() -> float:
		...

	def verificar_disponibilidad(fecha: datetime) -> bool:
		...

	def crear() -> bool:
		...	
