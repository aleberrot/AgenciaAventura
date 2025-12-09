class UsuarioDTO:
	"""docstring for Usuario"""
	def __init__(self, id: int, nombre: str, email: str, password_hash: str):
		self.id = id
		self.nombre = nombre
		self.email = email
		self.password_hash = password_hash

	def autenticar(email: str, password_hash: str) -> bool:
		...

	def registrar() -> bool:
		...


		
		