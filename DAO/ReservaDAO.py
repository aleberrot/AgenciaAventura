from DTO.ReservaDTO import ReservaDTO
from typing import List, Optional
from DAO.BaseDAO import BaseDAO

class ReservaDAO(BaseDAO):
    """
    DAO for Reserva entity, managing the 'reservas' table.
    """
    def __init__(self):
        super().__init__(ReservaDTO)

    def crear(self, reserva: ReservaDTO) -> int:
        """
        Create a new reserva record.
        """
        # Excluimos fecha_reserva (usa DEFAULT CURRENT_TIMESTAMP)
        sql = "INSERT INTO reservas (id_usuario, id_paquete, estado) VALUES (%s, %s, %s);"
        values = (reserva.id_usuario, reserva.id_paquete, reserva.estado)
        
        return self._ejecutar_consulta(sql, values)

    def obtener_por_id(self, id_reserva: int) -> Optional[ReservaDTO]:
        """
        Retrieve a reserva by its ID.
        """
        sql = "SELECT * FROM reservas WHERE id_reserva = %s;"
        
        return self._ejecutar_consulta(sql, (id_reserva,), fetch_one=True)

    def obtener_por_usuario(self, id_usuario: int) -> List[ReservaDTO]:
        """
        Retrieve all reservas for a specific user.
        """
        sql = "SELECT * FROM reservas WHERE id_usuario = %s;"
        
        return self._ejecutar_consulta(sql, (id_usuario,))

    def obtener_todos(self) -> List[ReservaDTO]:
        """
        Retrieve all reservas.
        """
        sql = "SELECT * FROM reservas;"
        
        return self._ejecutar_consulta(sql)

    def actualizar(self, reserva: ReservaDTO) -> int:
        """
        Update an existing reserva record (permite cambiar paquete, usuario o estado).
        """
        sql = """
            UPDATE reservas 
            SET id_usuario = %s, id_paquete = %s, estado = %s 
            WHERE id_reserva = %s;
        """
        values = (
            reserva.id_usuario, 
            reserva.id_paquete, 
            reserva.estado, 
            reserva.id_reserva
        )
        
        return self._ejecutar_consulta(sql, values)
    
    def actualizar_estado(self, id_reserva: int, nuevo_estado: str) -> int:
        """
        Specific method to update only the state of a reservation.
        """
        sql = "UPDATE reservas SET estado = %s WHERE id_reserva = %s;"
        values = (nuevo_estado, id_reserva)
        
        return self._ejecutar_consulta(sql, values)

    def eliminar(self, id_reserva: int) -> int:
        """
        Delete a reserva by its ID.
        """
        sql = "DELETE FROM reservas WHERE id_reserva = %s;"
        
        return self._ejecutar_consulta(sql, (id_reserva,))