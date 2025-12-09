from DB.conexion import Conexion
from DTO.UsuarioDTO import UsuarioDTO
from typing import List

class UsuarioDAO:
	"""docstring for UsuarioDAO"""
	
	def crear(self, usuario: UsuarioDTO) -> int:
		conn = Conexion.obtener_conexion()

		try:

			with conn.cursor() as cursor:
				sql = "INSERT INTO usuarios(id_usuario, nombre, email, rol, password_hash) VALUES (%s, %s, %s, %s, %s);"
				values = (usuario.id_usuario, usuario.nombre, usuario.email, usuario.rol, usuario.password_hash)

				cursor.execute(sql, values)

				return cursor.lastrowid

		except Exception as e:
			print(f"Ha ocurrido un error: {e}")

		return 0

	def obtener_por_id(self, id_usuario: int) -> UsuarioDTO:
		conn = Conexion.obtener_conexion()

		try:
			with conn.cursor() as cursor:
				sql = "SELECT * FROM usuarios WHERE id_usuario = %s;"
				values = (id_usuario,)

				cursor.execute(sql, values)

				usuario_db = cursor.fetchone()

				if usuario:
					return UsuarioDTO(**usuario_db)
				else:
					raise Exception(f"Usuario con el ID {id_usuario} no ha sido encontrado")

		except Exception as e:
			print(f"Ha ocurrido un error: {e}")

		return None

	def obtener_por_email(self, email: str) -> UsuarioDTO:
		conn = Conexion.obtener_conexion()

		try: 
			with conn.cursor() as cursor:
				sql = "SELECT * FROM usuarios WHERE email = %s;"
				values = (email,)

				cursor.execute(sql, values)

				usuario_db = cursor.fetchone()

				if usuario:
					return UsuarioDTO(**usuario_db)
				else: 
					raise Exception(f"Usuario con el email {email} no ha sido encontrado")
		except Exception as e:
			print(f"Ha ocurrido un error: {e}")

		return None

	def obtener_todos(self) -> List[UsuarioDTO]:
		conn = Conexion.obtener_conexion()

		try:
			with conn.cursor() as cursor:
				sql = "SELECT * FROM usuarios;"
				usuarios_db = cursor.fetchall()

				for user in usuarios_db:
					print(user)
		except Exception as e:
			print(f"Ha ocurrido un error: {e}")
