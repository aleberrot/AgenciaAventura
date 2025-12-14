from DTO.PaqueteDTO import PaqueteDTO
from typing import List, Optional
from DAO.BaseDAO import BaseDAO

class PaqueteDAO(BaseDAO):
    """
    DAO for Paquete entity, managing the paquetes table.
    """
    def __init__(self):
        super().__init__(PaqueteDTO)

    def crear(self, paquete: PaqueteDTO) -> int:
        """
        Create a new paquete record.
        """
        sql = "INSERT INTO paquetes (nombre, fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s, %s);"
        values = (paquete.nombre, paquete.fecha_inicio, paquete.fecha_fin, paquete.precio_total)
        
        # El método base maneja el INSERT y retorna lastrowid
        return self._ejecutar_consulta(sql, values)

    def obtener_por_id(self, id_paquete: int) -> Optional[PaqueteDTO]:
        """
        Retrieve a paquete by its ID.
        """
        sql = "SELECT * FROM paquetes WHERE id_paquete = %s;"
        
        # El método base mapea el resultado a PaqueteDTO
        return self._ejecutar_consulta(sql, (id_paquete,), fetch_one=True)

    def obtener_todos(self) -> List[PaqueteDTO]:
        """
        Retrieve all paquetes.
        """
        sql = "SELECT * FROM paquetes;"
        
        # El método base mapea la lista de resultados a List[PaqueteDTO]
        return self._ejecutar_consulta(sql)

    def actualizar(self, paquete: PaqueteDTO) -> int:
        """
        Update an existing paquete record.
        """
        sql = """
            UPDATE paquetes 
            SET nombre = %s, fecha_inicio = %s, fecha_fin = %s, precio_total = %s 
            WHERE id_paquete = %s;
        """
        values = (
            paquete.nombre, 
            paquete.fecha_inicio, 
            paquete.fecha_fin, 
            paquete.precio_total, 
            paquete.id_paquete
        )
        
        # El método base maneja el UPDATE y retorna rowcount
        return self._ejecutar_consulta(sql, values)

    def eliminar(self, id_paquete: int) -> int:
        """
        Delete a paquete by its ID.
        """
        sql = "DELETE FROM paquetes WHERE id_paquete = %s;"
        
        # El método base maneja el DELETE y retorna rowcount
        return self._ejecutar_consulta(sql, (id_paquete,))