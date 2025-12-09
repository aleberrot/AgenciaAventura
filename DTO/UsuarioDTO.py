class UsuarioDTO:
	"""docstring for Usuario"""
	def __init__(self, id_usuario: int, nombre: str, email: str, rol: str, password_hash: str):
		self.id_usuario = id_usuario
		self.nombre = nombre
		self.email = email
		self.rol = rol
		self.password_hash = password_hash


	def __repr__(self):
		return f"Usuario(id={self.id_usuario}, nombre={self.nombre}, email={self.email}, rol={self.rol})"
	def autenticar(email: str, password_hash: str) -> bool:
		...

	def registrar() -> bool:
		...



		
		