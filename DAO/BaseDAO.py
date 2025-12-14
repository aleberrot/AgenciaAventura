from DB.conexion import Conexion
from typing import List, Any, TypeVar, Type

# Define a generic type variable for DTOs
T = TypeVar('T')

class BaseDAO:
    """
    Base Data Access Object (DAO) class for common database operations.
    Attributes:
        tabla (str): The name of the database table.
    Methods:

    """
    def __init__(self, dto_clase: Type[T]):
        # The DTO class associated with this DAO
        self.dto_clase = dto_clase
    
    def _ejecutar_consulta(self, sql: str, values: tuple = (), fetch_one: bool = False) -> Any:
        conn = Conexion.obtener_conexion()
        
        # TODO determinar que operacion se esta realizando (SELECT, INSERT, UPDATE, DELETE)
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                
                # Filter write operations
                if sql.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    conn.commit()
                    # if INSERT, then return lastrowid otherwise rowcount (affected rows)
                    return cursor.lastrowid if sql.strip().upper().startswith("INSERT") else cursor.rowcount
                elif sql.strip().upper().startswith("SELECT"):
                    if fetch_one:
                        return cursor.fetchone()
                    else:
                        resultados_db = cursor.fetchall()
                        
                        # Map results to DTO instances
                        return [self.dto_clase(**data) for data in resultados_db]
                else:
                    raise Exception("Operación SQL inválida")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            conn.rollback()
            # Raise the exception to be handled by the calling method
            raise e
        finally:
            conn.cerrar_conexion()
        
               