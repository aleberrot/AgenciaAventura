from typing import List, Optional
from DAO.BaseDAO import BaseDAO 
from DTO.DestinoDTO import DestinoDTO 

class DestinoDAO(BaseDAO):
    """DAO for Destino entity"""
    
    def __init__(self):

        super().__init__(DestinoDTO) 

    def crear(self, destino: DestinoDTO) -> int:
        """
        Crea un nuevo registro de destino. Retorna el ID insertado.
        """

        sql = "INSERT INTO destinos(nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s);"
        values = (destino.nombre, destino.descripcion, destino.actividades, destino.costo)
        
        # El método base maneja el INSERT, commit y retorna el lastrowid
        return self._ejecutar_consulta(sql, values)
    
    def obtener_todos(self) -> List[DestinoDTO]:
        """
        Recupera todos los destinos de la base de datos.
        """
        sql = "SELECT * FROM destinos;"
        
        # El método base ejecuta, obtiene todos los resultados y los mapea a List[DestinoDTO]
        return self._ejecutar_consulta(sql, fetch_one=False)
    
    def obtener_por_id(self, id_destino: int) -> Optional[DestinoDTO]:
        """
        Recupera un destino por su ID.
        """
        sql = "SELECT * FROM destinos WHERE id_destino = %s;"
        
        # El método base ejecuta y mapea el resultado único a DestinoDTO
        return self._ejecutar_consulta(sql, (id_destino,), fetch_one=True)
        
    def actualizar(self, destino: DestinoDTO) -> int:
        """
        Actualiza un destino existente. Retorna el número de filas afectadas.
        """
        sql = """
            UPDATE destinos 
            SET nombre = %s, descripcion = %s, actividades = %s, costo = %s 
            WHERE id_destino = %s;
        """
        values = (destino.nombre, destino.descripcion, destino.actividades, destino.costo, destino.id_destino)
        
        # El método base maneja el UPDATE, commit y retorna el rowcount
        return self._ejecutar_consulta(sql, values)

    def eliminar(self, id_destino: int) -> int:
        """
        Elimina un destino por su ID. Retorna el número de filas afectadas.
        """
        sql = "DELETE FROM destinos WHERE id_destino = %s;"
        
        # El método base maneja el DELETE, commit y retorna el rowcount
        return self._ejecutar_consulta(sql, (id_destino,))