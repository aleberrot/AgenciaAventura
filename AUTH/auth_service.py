from getpass import getpass
from typing import List, Optional
from DAO.PaqueteDAO import PaqueteDAO
from DAO.ReservaDAO import ReservaDAO
from DAO.UsuarioDAO import UsuarioDAO
from DTO.PaqueteDTO import PaqueteDTO
from DTO.ReservaDTO import ReservaDTO
from DTO.SessionUsuarioDTO import SessionUsuarioDTO
from DTO.UsuarioDTO import UsuarioDTO
import bcrypt


class AuthService:
	@staticmethod
	def login(email, password_hash) -> SessionUsuarioDTO:
		dao = UsuarioDAO()

		usuario_db = dao.obtener_por_email(email)

		if usuario_db and bcrypt.checkpw(password_hash.encode('utf-8'), usuario_db.password_hash.encode('utf-8')):
			usuario_sesion = SessionUsuarioDTO(usuario_db.id_usuario, usuario_db.nombre, usuario_db.email, usuario_db.rol)
			return usuario_sesion
		else:
			return None
	@staticmethod
	def registrar_usuario() -> SessionUsuarioDTO:
		dao = UsuarioDAO()
		print("==== REGISTRO USUARIO ====")
		nombre = input("Ingrese su nombre -> ")
		email = input("Ingrese su email -> ")
		password = input("Ingrese su contraseña -> ")
		#password = getpass("Ingrese su contraseña ->")
		rol = input("Ingrese su rol (ADMIN/CLIENTE)-> ").upper()
		# Checkear que no exista ya ese usuario
		if dao.obtener_por_email(email):
			print("Error: Ya existe un usuario con ese email.")
			return None

		password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

		usuario_dto = UsuarioDTO(
			id_usuario=None,
			nombre=nombre,
			email=email,
			password_hash=password_hash,
			rol=rol
		)

		try:
			id_usuario = dao.crear(usuario_dto)
			if id_usuario:
				print("Registro exitoso. Iniciando sesión...")
				# Retornar el usuario recién creado para iniciar sesión
				usuario_dto.id_usuario = id_usuario
				return usuario_dto
			else:
				print("Error al guardar el usuario en la base de datos.")
				return None
		except Exception as e:
			print(f"Ocurrió un error en el registro: {e}")
			return None

	@staticmethod
	def obtener_paquetes_disponibles() -> List[PaqueteDTO]:
		"""Obtiene la lista de todos los paquetes turísticos."""
		return PaqueteDAO().obtener_todos()

	@staticmethod
	def crear_reserva(id_usuario: int, id_paquete: int) -> bool:
		"""Crea una reserva para un paquete, con estado 'pendiente'."""
		try:
			if not PaqueteDAO().obtener_por_id(id_paquete):
				print("Error: Paquete no encontrado.")
				return False

			reserva_dto = ReservaDTO(
				id_reserva=None,
				id_usuario=id_usuario,
				id_paquete=id_paquete,
				fecha_reserva=None,  # La DB asigna CURRENT_TIMESTAMP
				estado='pendiente'  # Estado inicial por defecto
			)

			id_reserva = ReservaDAO().crear(reserva_dto)
			return id_reserva > 0
		except Exception as e:
			print(f" Error al crear la reserva: {e}")
			return False

	@staticmethod
	def obtener_reservas_usuario(id_usuario: int) -> List[ReservaDTO]:
		"""Obtiene las reservas de un usuario específico."""
		return ReservaDAO().obtener_por_usuario(id_usuario)

	@staticmethod
	def obtener_paquete_por_id(id_paquete: int) -> Optional[PaqueteDTO]:
		"""Obtiene un paquete por su ID."""
		return PaqueteDAO().obtener_por_id(id_paquete)

	@staticmethod
	def cambiar_estado_reserva(id_reserva: int, nuevo_estado: str) -> bool:
		"""Actualiza el estado de una reserva. Requiere ser ADMIN."""
		try:
			filas = ReservaDAO().actualizar_estado(id_reserva, nuevo_estado)
			return filas > 0
		except Exception as e:
			print(f"Error al actualizar estado de reserva: {e}")
			return False

