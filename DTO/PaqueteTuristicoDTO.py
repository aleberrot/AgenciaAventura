from typing import List
from DTO.DestinoDTO import DestinoDTO
from datetime import datetime

class PaqueteTuristicoDTO:
	"""docstring for PaqueteTuristico"""
	def __init__(self, id: int, nombre: str, destinos: List[DestinoDTO], fecha_inicio: datetime, fecha_fin: datetime, precio_total: float):
	
	def calcular_precio() -> float:
		...

	def verificar_disponibilidad(fecha: datetime) -> bool:
		...

	def crear() -> bool:
		...	