class SessionUsuarioDTO:
	def __init__(self, id_usuario, nombre, email, rol):
		self.id_usuario = id_usuario
		self.nombre = nombre
		self.email = email
		self.rol = rol

	def es_admin(self):
		return self.rol == 'ADMIN'

	def es_empleado(self):
		return self.rol == 'EMPLEADO'

	def puede_crear_empleado(self):
		return self.es_admin()