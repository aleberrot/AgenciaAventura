from DTO.UsuarioDTO import UsuarioDTO
from datetime import datetime
from DTO.PaqueteDestinoDTO import PaqueteDestinoDTO

class ReservaDTO:
	"""docstring for Reserva"""
	def __init__(self, id_reserva: int, id_usuario: UsuarioDTO, id_paquete: PaqueteDestinoDTO, fecha_reserva: datetime, estado: str ):
		self.id_reserva = id_reserva
		self.id_usuario = id_usuario
		self.id_paquete = id_paquete
		self.fecha_reserva = fecha_reserva
		self.estado = estado

	def realizar_reserva() -> bool:
		...

	def obtener_detalles() -> dict:
		...

		