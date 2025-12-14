from DB.conexion import Conexion
from DTO.DestinoDTO import DestinoDTO
from typing import List

class DestinoDAO:
    """docstring for DestinoDAO"""
    def crear(self, destino: DestinoDTO) -> int:
        conn = Conexion.obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO destinos(id_destino, nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s, %s);"
                values = (destino.id_destino, destino.nombre, destino.descripcion, destino.actividades, destino.costo)
                cursor.execute(sql, values)
                
                return cursor.lastrowid
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return 0
    
    def obtener_todos(self) -> List['DestinoDTO']:
        conn = Conexion.obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM destinos;"
                cursor.execute(sql)
                
                destinos_db = cursor.fetchall()
                
                if destinos_db:
                    return [DestinoDTO(**destino) for destino in destinos_db]
                else:
                    return []
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return []
    
    
    
    