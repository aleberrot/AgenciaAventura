
from AUTH.auth_service import AuthService
from UI.MenuCliente import MenuCliente
from UI.MenuAdmin import MenuAdmin
from DTO.SessionUsuarioDTO import SessionUsuarioDTO
from getpass import getpass
from typing import List, Optional


class MenuPrincipal:
    def __init__(self):
        self.usuario_actual: Optional[SessionUsuarioDTO] = None

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

            try:
                user_option = int(input("Ingrese su opcion -> "))
                match user_option:
                    case 1:
                        self.login()
                    case 2:
                        self.registrar()
                    case 0:
                        print("Saliendo de la aplicación. ¡Gracias por usar Viaje Aventura!")
                        break
                    case _:
                        print("Opcion inválida.")
                        continue
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def login(self):
        print("\n--- INICIO DE SESIÓN ---")
        email = input("Ingrese su email -> ")
        password = input("Ingrese su contraseña -> ")
        # En el IDE getpass no funciona
        #password = getpass.getpass("Ingrese su contraseña ->")

        # 1. Autenticar usando el servicio
        usuario_sesion = AuthService.login(email, password)

        if usuario_sesion:
            self.usuario_actual = usuario_sesion
            print(f"\n¡Bienvenido, {self.usuario_actual.nombre} ({self.usuario_actual.rol})!")
            self.mostrar_menu_rol()
        else:
            print("\nCredenciales incorrectas.")

    def registrar(self):
        # El Auth maneja la lógica de registro
        usuario_dto = AuthService.registrar_usuario()

        # Si el registro fue exitoso, el DTO retornado se usa para la sesión
        if usuario_dto:
            # Se convierte el DTO de creación en DTO de sesión para mantener la consistencia
            usuario_actual = SessionUsuarioDTO(usuario_dto.id_usuario,usuario_dto.nombre, usuario_dto.email, usuario_dto.rol )
            self.usuario_actual = usuario_actual
            #self.usuario_actual = SessionUsuarioDTO(**usuario_dto.__dict__)
            self.mostrar_menu_rol()

    def mostrar_menu_rol(self):
        """Redirige al usuario al menú correspondiente a su rol."""
        if self.usuario_actual is None:
            return

        if self.usuario_actual.rol == 'ADMIN':
            MenuAdmin(self.usuario_actual).mostrar()
        elif self.usuario_actual.rol == 'CLIENTE':
            MenuCliente(self.usuario_actual).mostrar()

        # Si el menú de rol termina (por opción 'Cerrar Sesión'), se limpia la sesión
        self.usuario_actual = None