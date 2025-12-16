from DAO.DestinoDAO import DestinoDAO
from DAO.PaqueteDAO import PaqueteDAO
from DAO.PaqueteDestinoDAO import PaqueteDestinoDAO
from DTO.DestinoDTO import DestinoDTO
from DTO.PaqueteDTO import  PaqueteDTO
from DTO.PaqueteDestinoDTO import PaqueteDestinoDTO
from DTO.SessionUsuarioDTO import SessionUsuarioDTO
from AUTH.auth_service import AuthService
from DAO.ReservaDAO import ReservaDAO


class MenuAdmin:

    def __init__(self, usuario: SessionUsuarioDTO):
        self.usuario = usuario
        self.paquete_dao = PaqueteDAO()
        self.destino_dao = DestinoDAO()
        self.pd_dao = PaqueteDestinoDAO()

    def mostrar(self):
        while True:
            print(f"\n===== 👑 Menú Administrador: {self.usuario.nombre} =====")
            print("1. Ver Todas las Reservas (Gestión)")
            print("2. Gestionar Paquetes (Crear/Editar/Eliminar)")
            print("3. Gestionar Destinos (Crear/Editar/Eliminar")
            print("0. Cerrar Sesión")

            try:
                opcion = int(input("Ingrese su opción -> "))
                match opcion:
                    case 1:
                        self.gestionar_reservas()
                    case 2:
                        self.menu_gestion_paquetes()
                    case 3:
                        self.menu_gestion_destinos()
                    case 0:
                        break
                    case _:
                        print("Opción inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def gestionar_reservas(self):
        print("\n--- Gestión de Todas las Reservas ---")
        reservas = ReservaDAO().obtener_todos()

        if not reservas:
            print("No hay reservas en el sistema.")
            return

        for r in reservas:
            print(
                f"ID: {r.id_reserva} | Usuario ID: {r.id_usuario} | Paquete ID: {r.id_paquete} | Estado: {r.estado.upper()}")

        try:
            id_reserva = input("\nIngrese el ID de la reserva a modificar (o Enter para salir) -> ")
            if not id_reserva:
                return

            id_reserva = int(id_reserva)
            nuevo_estado = input("Ingrese el nuevo estado (CONFIRMADA/CANCELADA) -> ").lower()

            if nuevo_estado not in ['confirmada', 'cancelada']:
                print("Estado inválido.")
                return

            if AuthService.cambiar_estado_reserva(id_reserva, nuevo_estado):
                print(f"Estado de la reserva {id_reserva} actualizado a {nuevo_estado.upper()}.")
            else:
                print(f"No se pudo actualizar la reserva {id_reserva}.")

        except ValueError:
            print("ID de reserva inválido.")
        except Exception as e:
            print(f"Error: {e}")

    def menu_gestion_paquetes(self):
        while True:
            print("\n===== Gestión de Paquetes =====")
            print("1. Ver todos los paquetes")
            print("2. Crear nuevo paquete")
            print("3. Modificar paquete existente")
            print("4. Eliminar paquete")
            print("0. Volver al Menú Principal")

            try:
                opcion = int(input("Ingrese su opción -> "))
                match opcion:
                    case 1:
                        self._ver_todos_paquetes()
                    case 2:
                        self._crear_paquete()
                    case 3:
                        self._modificar_paquete()
                    case 4:
                        self._eliminar_paquete()
                    case 0:
                        break
                    case _:
                        print("Opción inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def _ver_todos_paquetes(self):
        """Muestra todos los paquetes con sus IDs."""
        print("\n--- Listado de Paquetes ---")
        paquetes = self.paquete_dao.obtener_todos()
        if not paquetes:
            print("No hay paquetes registrados.")
            return

        for p in paquetes:
            print(
                f"ID: {p.id_paquete} | Nombre: {p.nombre} | Precio: ${p.precio_total} | Inicio: {p.fecha_inicio} | Fin: {p.fecha_fin}")

    def _crear_paquete(self):
        """Pide datos para un nuevo paquete y permite vincular destinos."""
        print("\n--- CREAR NUEVO PAQUETE ---")
        try:
            nombre = input("Nombre del paquete: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            precio_total = float(input("Precio total: "))

            nuevo_paquete_dto = PaqueteDTO(
                id_paquete=None,
                nombre=nombre,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                precio_total=precio_total
            )

            id_paquete = self.paquete_dao.crear(nuevo_paquete_dto)

            if id_paquete > 0:
                print(f"Paquete '{nombre}' creado con ID: {id_paquete}")

                self._vincular_destinos(id_paquete)
            else:
                print(" Error al crear el paquete.")

        except ValueError:
            print(
                "Entrada inválida. Asegúrese de ingresar números para el precio y el formato correcto para las fechas (YYYY-MM-DD).")
        except Exception as e:
            print(f"Error desconocido al crear el paquete: {e}")

    def _modificar_paquete(self):
        """Permite modificar campos de un paquete y sus destinos."""
        self._ver_todos_paquetes()
        if not self.paquete_dao.obtener_todos(): return

        try:
            id_paquete = int(input("\nIngrese el ID del paquete a modificar -> "))
            paquete_actual = self.paquete_dao.obtener_por_id(id_paquete)

            if not paquete_actual:
                print("Paquete no encontrado.")
                return

            print(f"\n--- MODIFICAR PAQUETE ID {id_paquete} ({paquete_actual.nombre}) ---")

            # Recopilar nuevos datos (permitiendo dejar en blanco para no modificar)
            paquete_actual.nombre = input(f"Nombre actual ({paquete_actual.nombre}): ") or paquete_actual.nombre
            paquete_actual.fecha_inicio = input(
                f"Fecha inicio actual ({paquete_actual.fecha_inicio}): ") or paquete_actual.fecha_inicio
            paquete_actual.fecha_fin = input(
                f"Fecha fin actual ({paquete_actual.fecha_fin}): ") or paquete_actual.fecha_fin

            nuevo_precio = input(f"Precio total actual (${paquete_actual.precio_total}): ")
            if nuevo_precio:
                paquete_actual.precio_total = float(nuevo_precio)

            if self.paquete_dao.actualizar(paquete_actual) > 0:
                print(" Paquete actualizado correctamente.")

                # Opcional: Modificar destinos
                self._vincular_destinos(id_paquete, modificar=True)
            else:
                print("⚠No se realizó ninguna modificación (o el paquete no existe).")

        except ValueError:
            print("Entrada inválida (ID o Precio).")
        except Exception as e:
            print(f"Error al modificar el paquete: {e}")

    def _eliminar_paquete(self):
        """Elimina un paquete por su ID."""
        self._ver_todos_paquetes()
        if not self.paquete_dao.obtener_todos(): return

        try:
            id_paquete = int(input("\nIngrese el ID del paquete a ELIMINAR -> "))
            if input("¿Confirmar eliminación? (S/N) -> ").upper() == 'S':
                # La eliminación en 'paquetes' debería CASCADE a 'paquetes_destinos' y 'reservas'
                if self.paquete_dao.eliminar(id_paquete) > 0:
                    print(f"Paquete ID {id_paquete} y sus vínculos/reservas eliminados.")
                else:
                    print("No se pudo eliminar el paquete. Verifique el ID.")
        except ValueError:
            print("ID de paquete inválido.")


    def _vincular_destinos(self, id_paquete: int, modificar: bool = False):
        """Permite al administrador agregar destinos a un paquete."""

        if modificar:
            op = input("¿Desea modificar los destinos vinculados a este paquete? (S/N) -> ").upper()
            if op != 'S': return

            self.pd_dao.eliminar_por_paquete(id_paquete)

        while True:
            print("\n--- Destinos Disponibles ---")
            destinos = self.destino_dao.obtener_todos()
            if not destinos:
                print("No hay destinos registrados para vincular.")
                return

            for d in destinos:
                print(f"ID: {d.id_destino} | Nombre: {d.nombre} | Costo: ${d.costo}")

            id_destino = input("Ingrese el ID del destino a agregar (o 'FIN' para terminar) -> ").upper()
            if id_destino == 'FIN':
                break

            try:
                id_destino = int(id_destino)

                pd_dto = PaqueteDestinoDTO(id_paquete=id_paquete, id_destino=id_destino)

                # values = (pd_dto.id_paquete, pd_dto.id_destino)

                if self.pd_dao.crear(pd_dto) > 0:
                    print(f" Destino ID {id_destino} vinculado correctamente.")
                else:
                    print("Error al vincular el destino (puede que ya esté vinculado o el ID no exista).")

            except ValueError:
                print("ID de destino inválido. Use solo números o 'FIN'.")
            except Exception as e:
                print(f"Error al vincular: {e}")

    def menu_gestion_destinos(self):
        while True:
            print("\n=====  Gestión de Destinos =====")
            print("1. Ver todos los destinos")
            print("2. Crear nuevo destino")
            print("3. Modificar destino existente")
            print("4. Eliminar destino")
            print("0. Volver al Menú Principal")

            try:
                opcion = int(input("Ingrese su opción -> "))
                match opcion:
                    case 1:
                        self._ver_todos_destinos()
                    case 2:
                        self._crear_destino()
                    case 3:
                        self._modificar_destino()
                    case 4:
                        self._eliminar_destino()
                    case 0:
                        break
                    case _:
                        print("Opción inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def _ver_todos_destinos(self):
        """Muestra todos los destinos con sus IDs y detalles."""
        print("\n--- Listado de Destinos ---")
        destinos = self.destino_dao.obtener_todos()
        if not destinos:
            print("No hay destinos registrados.")
            return

        for d in destinos:
            print(f"ID: {d.id_destino} | Nombre: {d.nombre} | Costo: ${d.costo}")
            print(f"  Descripción: {d.descripcion[:50]}...")
            print(f"  Actividades: {d.actividades[:50]}...")

    def _crear_destino(self):
        """Pide datos para un nuevo destino y lo guarda."""
        print("\n--- CREAR NUEVO DESTINO ---")
        try:
            nombre = input("Nombre del destino: ")
            descripcion = input("Descripción detallada: ")
            actividades = input("Lista de actividades (separadas por coma): ")
            costo = float(input("Costo asociado (solo número): "))

            nuevo_destino_dto = DestinoDTO(
                id_destino=None,
                nombre=nombre,
                descripcion=descripcion,
                actividades=actividades,
                costo=costo
            )

            id_destino = self.destino_dao.crear(nuevo_destino_dto)

            if id_destino > 0:
                print(f" Destino '{nombre}' creado con ID: {id_destino}")
            else:
                print(" Error al crear el destino.")

        except ValueError:
            print(" Entrada inválida. Asegúrese de ingresar un número para el costo.")
        except Exception as e:
            print(f" Error desconocido al crear el destino: {e}")

    def _modificar_destino(self):
        """Permite modificar campos de un destino existente."""
        self._ver_todos_destinos()
        destinos = self.destino_dao.obtener_todos()
        if not destinos: return

        try:
            id_destino = int(input("\nIngrese el ID del destino a modificar -> "))
            destino_actual = self.destino_dao.obtener_por_id(id_destino)

            if not destino_actual:
                print(" Destino no encontrado.")
                return

            print(f"\n--- MODIFICAR DESTINO ID {id_destino} ({destino_actual.nombre}) ---")

            # Recopilar nuevos datos (permitiendo dejar en blanco para no modificar)
            destino_actual.nombre = input(f"Nombre actual ({destino_actual.nombre}): ") or destino_actual.nombre
            destino_actual.descripcion = input(
                f"Descripción actual ({destino_actual.descripcion[:30]}...): ") or destino_actual.descripcion
            destino_actual.actividades = input(
                f"Actividades actuales ({destino_actual.actividades[:30]}...): ") or destino_actual.actividades

            nuevo_costo = input(f"Costo actual (${destino_actual.costo}): ")
            if nuevo_costo:
                destino_actual.costo = float(nuevo_costo)

            if self.destino_dao.actualizar(destino_actual) > 0:
                print("Destino actualizado correctamente.")
            else:
                print(" No se realizó ninguna modificación.")

        except ValueError:
            print("Entrada inválida (ID o Costo).")
        except Exception as e:
            print(f" Error al modificar el destino: {e}")

    def _eliminar_destino(self):
        """Elimina un destino por su ID."""
        self._ver_todos_destinos()
        destinos = self.destino_dao.obtener_todos()
        if not destinos: return

        try:
            id_destino = int(input("\nIngrese el ID del destino a ELIMINAR -> "))

            # Advertencia: La eliminación puede fallar si está vinculado a un paquete (a menos que uses ON DELETE CASCADE en la FK)
            if input(
                    "¿Confirmar eliminación? Esta acción puede afectar a paquetes vinculados. (S/N) -> ").upper() == 'S':

                if self.destino_dao.eliminar(id_destino) > 0:
                    print(f" Destino ID {id_destino} eliminado.")
                else:
                    print(
                        "No se pudo eliminar el destino. Verifique el ID o si está vinculado a un paquete que requiere eliminación manual primero.")
        except ValueError:
            print("ID de destino inválido.")