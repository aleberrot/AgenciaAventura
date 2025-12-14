from DB.conexion import Conexion
from DTO.ReservaDTO import ReservaDTO


# TODO: Implementar BaseDAO para heredar
class ReservaDAO:
    """docstring for ReservaDAO"""
    
    def crear(self, reserva: ReservaDTO) -> int:
        conn = Conexion.obtener_conexion()
        
        try:    
            with conn.cursor() as cursor:
                sql = "INSERT INTO reservas(id_reserva, id_usuario, id_paquete, fecha_reserva, estado) VALUES (%s, %s, %s, %s, %s);"
                values = (reserva.id_reserva, reserva.id_usuario, reserva.id_paquete, reserva.fecha_reserva, reserva.estado)
                
                cursor.execute(sql, values)
                return cursor.lastrowid
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            conn.rollback()
            return 0
        
    def obtener_por_id(self, id_reserva: int) -> ReservaDTO:
        conn = Conexion.obtener_conexion()
            
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM reservas WHERE id_reserva = %s;"
                values = (id_reserva,)
                
                cursor.execute(sql, values)
                reserva_db = cursor.fetchone()
                
                if reserva_db:
                    return ReservaDTO(**reserva_db)
                else:
                    raise Exception(f"Reserva con el ID {id_reserva} no ha sido encontrado")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return None

    def obtener_reservas_por_usuario(self, id_usuario: int) -> list[ReservaDTO]:
        conn = Conexion.obtener_conexion()
        
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM reservas WHERE id_usuario = %s;"
                values = (id_usuario,)
                
                cursor.execute(sql, values)
                reservas_db = cursor.fetchall()
                
                if reservas_db:
                    return [ReservaDTO(**reserva) for reserva in reservas_db]
                else:
                    raise Exception(f"No se encontraron reservas para el usuario con ID {id_usuario}")                
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return []
    