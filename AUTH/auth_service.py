import getpass
from DAO.UsuarioDAO import UsuarioDAO
from DTO.SessionUsuario import SessionUsuario
from DTO.UsuarioDTO import UsuarioDTO
import bcrypt


class Auth_Service:
	@staticmethod
	def login(email, password_hash) -> SessionUsuario:
		dao = UsuarioDAO()

		usuario_db = dao.obtener_usuario_por_email(email)

		if usuario_db and bcrypt.checkpw(password_hash.encode('utf-8'), usuario_db.password_hash.encode('utf-8')):
			return SessionUsuario(**usuario_db)
		else:
			return None
	@staticmethod
	def register(usuario: UsuarioDTO) -> SessionUsuario:
		nombre = input("Ingrese su nombre -> ")
		email = input("Ingrese su email -> ")


