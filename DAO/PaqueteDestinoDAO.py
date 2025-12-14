from typing import List
from DAO.BaseDAO import BaseDAO 
from DTO.PaqueteDestinoDTO import PaqueteDestinoDTO 


class PaqueteDestinoDAO(BaseDAO): 
    """DAO for the relationship between Paquete and Destino (paquetes_destinos table)."""
    
    def __init__(self):
        super().__init__(PaqueteDestinoDTO) 

    def crear(self, paquete_destino: PaqueteDestinoDTO) -> int:
        """
        Creates a new record in paquetes_destinos. Returns the inserted ID.
        """
        sql = "INSERT INTO paquetes_destinos(id_paquete, id_destino) VALUES(%s, %s);"
        values = (paquete_destino.id_paquete, paquete_destino.id_destino)
                
        return self._ejecutar_consulta(sql, values)
        
    def obtener_destinos_por_paquete(self, id_paquete: int) -> List[PaqueteDestinoDTO]:
        """
        Obtiene todos los IDs de destino asociados a un paquete.
        """
        sql = "SELECT id_paquete, id_destino FROM paquetes_destinos WHERE id_paquete = %s;"
        
        return self._ejecutar_consulta(sql, (id_paquete,), fetch_one=False)

    def eliminar_por_paquete(self, id_paquete: int) -> int:
        """
        Elimina todos los destinos asociados a un paquete específico.
        """
        sql = "DELETE FROM paquetes_destinos WHERE id_paquete = %s;"
        
        return self._ejecutar_consulta(sql, (id_paquete,))
    
    def eliminar_vinculo(self, id_paquete: int, id_destino: int) -> int:
        """
        Elimina un vínculo específico entre un paquete y un destino.
        """
        sql = "DELETE FROM paquetes_destinos WHERE id_paquete = %s AND id_destino = %s;"
        
        return self._ejecutar_consulta(sql, (id_paquete, id_destino))