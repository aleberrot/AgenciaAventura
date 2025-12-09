from DTO.DestinoDTO import DestinoDTO
from DTO.PaqueteTuristicoDTO import PaqueteTuristicoDTO
from DTO.ReservaDTO import ReservaDTO
from typing import List

class AgenciaDTO:
	"""docstring for Agencia"""
	def __init__(self, destinos: List[DestinoDTO], paquetes: List[PaqueteTuristicoDTO], reservas: List[ReservaDTO]):
		self.destinos = destinos
		self.paquetes = paquetes
		self.reservas = reservas

		def gestionar_destinos():
			...

		def gestionar_paquetes():
			...

		def gestionar_reservas():
			...
			
		