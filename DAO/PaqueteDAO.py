from DTO.PaqueteDTO import PaqueteDTO
from typing import List
from DB.conexion import Conexion

# TODO: Implementar BaseDAO para heredar
class PaqueteDAO:
    """docstring for PaqueteDAO"""
    def crear(self, paquete: PaqueteDTO) -> int:
        conn = Conexion.obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO paquetes(id_paquete, nombre, fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s, %s, %s);"
                values = (paquete.id_paquete, paquete.nombre, paquete.fecha_inicio, paquete.fecha_fin, paquete.precio_total)
                cursor.execute(sql, values)
                
                return cursor.lastrowid
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return 0
        
    def obtener_todos(self) -> List['PaqueteDTO']:
        conn = Conexion.obtener_conexion()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM paquetes;"
                cursor.execute(sql)
                
                paquetes_db = cursor.fetchall()
                
                if paquetes_db:
                    return [PaqueteDTO(**paquete) for paquete in paquetes_db]
                else:
                    return []
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return []
    