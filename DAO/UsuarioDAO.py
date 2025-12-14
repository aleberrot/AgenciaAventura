from DB.conexion import Conexion
from DTO.UsuarioDTO import UsuarioDTO
from typing import List
from DAO.BaseDAO import BaseDAO

# TODO: Implementar BaseDAO para heredar
class UsuarioDAO(BaseDAO):
	"""
	DAO for Usuario entity
	
	Methods:
	- crear(usuario: UsuarioDTO) -> int
	- obtener_por_id(id_usuario: int) -> UsuarioDTO
	- obtener_por_email(email: str) -> UsuarioDTO
	- obtener_todos() -> List[UsuarioDTO]
	- eliminar(id_usuario: int) -> int
	- actualizar(usuario: UsuarioDTO) -> int
	"""
	def __init__(self):
		super().__init__(UsuarioDTO)

	def crear(self, usuario: UsuarioDTO) -> int:
		"""
		Create a ner usuario record in the database.
		Args:
			usuario (UsuarioDTO): The usuario data to insert.	
		"""
  
		sql = "INSERT INTO usuario (nombre, email, rol, password_hash) VALUES (%s, %s, %s, %s);"
		values = (usuario.nombre, usuario.email, usuario.rol, usuario.password_hash)

		return self.ejecutar_insert(sql, values, fetch_one=False)

	def obtener_por_id(self, id_usuario: int) -> UsuarioDTO:
		"""
		Retrieve a usuario by its ID.
		Args:
			id_usuario (int): The ID of the usuario to retrieve.
		"""
		sql = "SELECT * FROM usuarios WHERE id_usuario = %s;"

		return self._ejecutar_consulta(sql, (id_usuario,), fetch_one=True)

	def obtener_por_email(self, email: str) -> UsuarioDTO:
		"""
		Retrieve a usuario by its email.
		Args:
			email (str): The email of the usuario to retrieve.
		"""
		sql = "SELECT * FROM usuarios WHERE email = %s;"

		return self._ejecutar_consulta(sql, (email,), fetch_one=True)
		

	def obtener_todos(self) -> List[UsuarioDTO]:
		"""
		Retrieve all usuarios from the database.
 		"""
		sql = "SELECT * FROM usuarios;"

		return self._ejecutar_consulta(sql, fetch_one=False)

	def eliminar(self, id_usuario: int) -> List[UsuarioDTO]:
		"""
		Delete a usuario by its ID.
		Args:
			id_usuario (int): The ID of the usuario to delete.
		"""
		sql = "DELETE FROM usuarios WHERE id_usuario = %s;"

		return self._ejecutar_consulta(sql, (id_usuario,), fetch_one=False)

	def actualizar(self, usuario: UsuarioDTO) -> int:
		"""
		Update an existing usuario record in the database.
		Args:
			usuario (UsuarioDTO): The usuario data to update.
		"""
		sql = "UPDATE usuarios SET nombre = %s, email = %s, rol = %s, password_hash = %s WHERE id_usuario = %s;"
		values = (usuario.nombre, usuario.email, usuario.rol, usuario.password_hash, usuario.id_usuario)
		return self._ejecutar_consulta(sql, values, fetch_one=False)
