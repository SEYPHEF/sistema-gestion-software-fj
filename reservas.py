import logging
from modelos import Cliente, Servicio
from excepciones import ServicioNoDisponibleError, ReservaInvalidaError


class Reserva:

  def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio):
    self.id_reserva = id_reserva
    self.cliente = cliente
    self.servicio = servicio
    self.estado = "Pendiente"
    self.costo_calculado = 0.0

  def procesar_reserva(self, *args, **kwargs):
    """Procesa la reserva utilizando bloques try/except/else/finally y encadenamiento."""
    logging.info(f"Iniciando procesamiento de reserva {self.id_reserva} para cliente {self.cliente.identificador}.")
    try:
      self.servicio.validar_parametros()
      self.costo_calculado = self.servicio.calcular_costo(*args, **kwargs)
      
    except ServicioNoDisponibleError as e:
      self.estado = "Fallida"
      logging.error(f"Error de disponibilidad en reserva {self.id_reserva}: {e}")
      raise ReservaInvalidaError(f"No se pudo completar la reserva {self.id_reserva} debido a un problema con el servicio.") from e
    
    except Exception as e:
      self.estado = "Fallida"
      logging.error(f"Error inesperado procesando reserva {self.id_reserva}: {e}")
      raise ReservaInvalidaError(f"Falla crítica en reserva {self.id_reserva}.") from e
    
    else:
      self.estado = "Confirmada"
      logging.info(f"Reserva {self.id_reserva} confirmada exitosamente. Costo total: ${self.costo_calculado}")
    
    finally:
      logging.info(f"Finalizó el ciclo de procesamiento para la reserva {self.id_reserva}. Estado actual: {self.estado}\n")
