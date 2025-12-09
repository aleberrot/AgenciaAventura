from DTO.UsuarioDTO import UsuarioDTO
from  datetime import datime

class ReservaDTO:
	"""docstring for Reserva"""
	def __init__(self, id: int, usuario: UsuarioDTO, paquete: PaqueteTuristico, fecha_reserva: datetime, estado: str ):
		self.id = id
		self.usuario = usuario
		self.paquete = paquete
		self.fecha_reserva = fecha_reserva
		self.estado = estado

	def realizar_reserva() -> bool:
		...

	def obtener_detalles() -> dict:
		...

		