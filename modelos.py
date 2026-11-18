from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError, ServicioNoDisponibleError


class EntidadSistema(ABC):
  """Clase abstracta general que representa entidades base del sistema."""

  def __init__(self, identificador: str):
    self._identificador = identificador

  @property
  def identificador(self):
    return self._identificador

  @abstractmethod
  def obtener_detalles(self) -> str:
    pass


class Cliente(EntidadSistema):

  def __init__(self, identificador: str, nombre: str, email: str):
    super().__init__(identificador)
    self.nombre = nombre
    self.email = email

  @property
  def nombre(self):
    return self.__nombre

  @nombre.setter
  def nombre(self, valor):
    if not valor or len(valor.strip()) < 3:
      raise ClienteInvalidoError(
          f"El nombre '{valor}' es inválido. Debe tener al menos 3 caracteres."
      )
    self.__nombre = valor.strip()

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, valor):
    if not valor or "@" not in valor or "." not in valor:
      raise ClienteInvalidoError(
          f"El correo electrónico '{valor}' tiene un formato inválido."
      )
    self.__email = valor.strip()

  def obtener_detalles(self) -> str:
    return f"Cliente [ID: {self.identificador}, Nombre: {self.nombre}, Email: {self.email}]"


class Servicio(EntidadSistema):

  def __init__(self, identificador: str, nombre_servicio: str, precio_base: float):
    super().__init__(identificador)
    self.nombre_servicio = nombre_servicio
    self.precio_base = precio_base

  @abstractmethod
  def calcular_costo(self, *args, **kwargs) -> float:
    """Método polimórfico para calcular costo."""
    pass

  @abstractmethod
  def validar_parametros(self) -> bool:
    """Valida la disponibilidad o parámetros del servicio."""
    pass


class ReservaSala(Servicio):

  def __init__(self, identificador: str, precio_base: float, capacidad: int):
    super().__init__(identificador, "Reserva de Sala", precio_base)
    self.capacidad = capacidad

  def validar_parametros(self) -> bool:
    if self.capacidad <= 0:
      raise ServicioNoDisponibleError(
          f"Sala {self.identificador}: La capacidad ({self.capacidad}) debe ser mayor a 0."
      )
    return True

  def calcular_costo(self, horas: int, descuento: float = 0.0, impuesto: float = 0.19) -> float:
    if horas <= 0:
      raise ServicioNoDisponibleError("El número de horas a reservar debe ser mayor a cero.")
    subtotal = self.precio_base * horas
    total_con_descuento = subtotal * (1 - descuento)
    total_final = total_con_descuento * (1 + impuesto)
    return round(total_final, 2)

  def obtener_detalles(self) -> str:
    return f"Servicio: {self.nombre_servicio} (Capacidad: {self.capacidad} pers., Base por hora: ${self.precio_base})"


class AlquilerEquipo(Servicio):

  def __init__(self, identificador: str, precio_base: float, stock: int):
    super().__init__(identificador, "Alquiler de Equipos", precio_base)
    self.stock = stock

  def validar_parametros(self) -> bool:
    if self.stock <= 0:
      raise ServicioNoDisponibleError(
          f"Equipo {self.identificador}: No hay stock disponible actualmente."
      )
    return True

  def calcular_costo(self, dias: int, seguro_adicional: float = 0.0) -> float:
    if dias <= 0:
      raise ServicioNoDisponibleError("Los días de alquiler deben ser mayores a cero.")
    total = (self.precio_base * dias) + seguro_adicional
    return round(total, 2)

  def obtener_detalles(self) -> str:
    return f"Servicio: {self.nombre_servicio} (Stock disponible: {self.stock}, Base diaria: ${self.precio_base})"


class AsesoriaEspecializada(Servicio):

  def __init__(self, identificador: str, precio_base: float, nivel_experticia: str):
    super().__init__(identificador, "Asesoría Especializada", precio_base)
    self.nivel_experticia = nivel_experticia

  def validar_parametros(self) -> bool:
    if self.nivel_experticia not in ["Junior", "Senior", "Master"]:
      raise ServicioNoDisponibleError(
          f"Asesoría {self.identificador}: Nivel de experticia '{self.nivel_experticia}' no válido."
      )
    return True

  def calcular_costo(self, sesiones: int, aplicar_bono_corporativo: bool = False) -> float:
    if sesiones <= 0:
      raise ServicioNoDisponibleError("El número de sesiones debe ser mayor a cero.")
    multiplicador = 0.85 if aplicar_bono_corporativo else 1.0
    total = self.precio_base * sesiones * multiplicador
    return round(total, 2)

  def obtener_detalles(self) -> str:
    return f"Servicio: {self.nombre_servicio} (Nivel: {self.nivel_experticia}, Base por sesión: ${self.precio_base})"
