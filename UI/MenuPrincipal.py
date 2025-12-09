from AUTH.auth_service import AuthService

class MenuPrincipal:
	def __init__(self):
		self.usuario_actual = None
	def mostrar(self):
		while True:
			print("""
==============
Viaje Aventura
==============

1. Iniciar sesion
2. Registrarse
0. Salir
				""")

			user_option = int(input("Ingrese su opcion -> "))
			match user_option:
				case 1:
					self.login()
				case 2:
					self.registrar()
				case 0: 
					break
				case _:
					print("Opcion inválida.")
					continue

	def login(self):
		...

	def registrar(self):
		print("registro")