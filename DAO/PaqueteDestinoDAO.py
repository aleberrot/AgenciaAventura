from DB.conexion import Conexion
from DTO.PaqueteDestinoDTO import PaqueteDestinoDTO


# TODO: Implementar BaseDAO para heredar
class PaqueteDestionDAO:
    """Docstring for PaqueteDestinoDAO"""
    # TODO implementar operaciones CRUD para PaqueteTuristicoDAO
    
    def crear(self, paquete: PaqueteDestinoDTO) -> int:
        """
        Implementar la creación de un nuevo paquete turístico en la base de datos.
        
        Parametros:
        - paquete (PaqueteTuristicoDTO): Objeto que contiene los datos del paquete turístico a crear.
        Retorna: 
        - int: ID del paquete turístico creado o 0 en  caso de error.
        
        """
        # TODO implementar metodo para crear paquete
        conn = Conexion.obtener_conexion()
        
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO paquetes_destinos(id_paquete, id_destino) VALUES(%s, %s);"
                values = (paquete.id_paquete, paquete.id_destino)
                
                cursor.execute(sql, values)
                
                return cursor.lastrowid
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            conn.rollback()
            return 0