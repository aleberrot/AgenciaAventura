# MenuCliente.py
from typing import Optional
from DTO.SessionUsuarioDTO import SessionUsuarioDTO
from AUTH.auth_service import AuthService


class MenuCliente:

    def __init__(self, usuario: SessionUsuarioDTO):
        self.usuario = usuario

    def mostrar(self):
        while True:
            print(f"\n===== Menú Cliente: {self.usuario.nombre} =====")
            print("1. Ver Paquetes Disponibles")
            print("2. Ver Mis Reservas")
            print("3. Realizar Nueva Reserva")
            print("0. Cerrar Sesión")

            try:
                opcion = int(input("Ingrese su opción -> "))
                match opcion:
                    case 1:
                        self.ver_paquetes()
                    case 2:
                        self.ver_reservas()
                    case 3:
                        self.realizar_reserva()
                    case 0:
                        break
                    case _:
                        print("Opción inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def ver_paquetes(self):
        print("\n--- Paquetes Disponibles ---")
        paquetes = AuthService.obtener_paquetes_disponibles()
        if not paquetes:
            print("No hay paquetes disponibles en este momento.")
            return

        for p in paquetes:
            print(
                f"ID: {p.id_paquete} | Nombre: {p.nombre} | Precio: ${p.precio_total} | Inicio: {p.fecha_inicio} | Fin: {p.fecha_fin}")
            # Aquí podrías llamar a un servicio para mostrar los destinos asociados (JOIN)

    def ver_reservas(self):
        print("\n--- Mis Reservas ---")
        reservas = AuthService.obtener_reservas_usuario(self.usuario.id_usuario)
        if not reservas:
            print("Usted no tiene reservas activas.")
            return

        for r in reservas:
            paquete = AuthService.obtener_paquete_por_id(r.id_paquete)
            nombre_paquete = paquete.nombre if paquete else "Paquete Desconocido"
            print(
                f"ID Reserva: {r.id_reserva} | Paquete: {nombre_paquete} | Estado: {r.estado.upper()} | Fecha: {r.fecha_reserva}")

    def realizar_reserva(self):
        self.ver_paquetes()
        if not AuthService.obtener_paquetes_disponibles():
            return

        try:
            id_paquete = int(input("Ingrese el ID del paquete que desea reservar -> "))
            if AuthService.crear_reserva(self.usuario.id_usuario, id_paquete):
                print(f"\n¡Reserva realizada! ID de paquete {id_paquete}. Estado: PENDIENTE.")
            else:
                print("\nNo se pudo crear la reserva. Verifique el ID del paquete.")
        except ValueError:
            print("ID de paquete inválido.")