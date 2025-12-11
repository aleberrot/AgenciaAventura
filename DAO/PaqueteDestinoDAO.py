from DB.conexion import Conexion
from DTO.PaqueteDestinoDTO import PaqueteDestinoDTO

class PaqueteTuristicoDAO:
    """Docstring for PaqueteTuristicoDAO"""
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
                sql = "INSERT INTO p"
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            conn.rollback()
            return 0