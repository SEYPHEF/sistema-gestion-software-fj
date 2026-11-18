class SoftwareFJError(Exception):
  """Excepción base para todos los errores del sistema Software FJ."""
  pass


class ClienteInvalidoError(SoftwareFJError):
  """Lanzada cuando los datos del cliente no cumplen con las validaciones."""
  pass


class ServicioNoDisponibleError(SoftwareFJError):
  """Lanzada cuando un servicio no está disponible o sus parámetros son erróneos."""
  pass


class ReservaInvalidaError(SoftwareFJError):
  """Lanzada cuando ocurre un fallo al intentar procesar una reserva."""
  pass
