from typing import List


class DestinoDTO:
	"""docstring for Destino"""
	def __init__(self, id_destino: int, nombre: str, descripcion: str, actividades: List[str], costo: float):
		self.id_destino = id_destino
		self.nombre = nombre
		self.descripcion = descripcion
		self.actividades = actividades
		self.costo = costo

	def crear() -> bool:
		...

	def actualizar() -> bool:
		...

	def eliminar() -> bool:
		...

	def obtener_todos() -> List['DestinoDTO']:
		... 
		