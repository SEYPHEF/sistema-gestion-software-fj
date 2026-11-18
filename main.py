import logging
import os
from excepciones import SoftwareFJError
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva

# ==========================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ==========================================
LOG_FILE = "sistema_fj.log"
if os.path.exists(LOG_FILE):
  os.remove(LOG_FILE)  # Limpia logs anteriores

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    encoding="utf-8",
)


# ==========================================
# MOTOR DE SIMULACIÓN DE 10 OPERACIONES
# ==========================================
def ejecutar_simulaciones():
  print("=== INICIANDO SIMULACIONES DE SOFTWARE FJ ===\n")
  
  sala_vip = ReservaSala("SALA-01", 50000, 10)
  equipo_laptop = AlquilerEquipo("EQ-01", 35000, 2)
  asesoria_ti = AsesoriaEspecializada("ASES-01", 120000, "Senior")
  
  operaciones = [
      # 1. Válida: Registro de cliente y reserva de sala exitosa[cite: 3]
      lambda: (c := Cliente("C001", "Álvaro Rubio", "alvaro@gmail.com"),
               r := Reserva("RES-001", c, sala_vip),
               r.procesar_reserva(horas=3, descuento=0.1, impuesto=0.19)),
      
      # 2. Inválida: Cliente con nombre corto (ClienteInvalidoError)[cite: 2, 9]
      lambda: Cliente("C002", "Al", "al@gmail.com"),
      
      # 3. Inválida: Cliente con email incorrecto (ClienteInvalidoError)[cite: 2, 9]
      lambda: Cliente("C003", "Carlos Pérez", "carlos-correo-malo"),
      
      # 4. Válida: Alquiler de equipo exitoso[cite: 3]
      lambda: (c := Cliente("C004", "Loraine Gomez", "loraine@gmail.com"),
               r := Reserva("RES-004", c, equipo_laptop),
               r.procesar_reserva(dias=4, seguro_adicional=10000)),
      
      # 5. Inválida: Sala con capacidad cero (ServicioNoDisponibleError)[cite: 2, 9]
      lambda: (sala_rota := ReservaSala("SALA-ERR", 40000, 0),
               sala_rota.validar_parametros()),
      
      # 6. Válida: Asesoría especializada con bono[cite: 3]
      lambda: (c := Cliente("C005", "Sofía Mendoza", "sofia@gmail.com"),
               r := Reserva("RES-006", c, asesoria_ti),
               r.procesar_reserva(sesiones=2, aplicar_bono_corporativo=True)),
      
      # 7. Inválida: Reserva con horas negativas[cite: 2, 3]
      lambda: (c := Cliente("C006", "David Ruiz", "david@gmail.com"),
               r := Reserva("RES-007", c, sala_vip),
               r.procesar_reserva(horas=-2)),
      
      # 8. Inválida: Asesoría con nivel de experticia erróneo[cite: 2, 9]
      lambda: (asesoria_mala := AsesoriaEspecializada("ASES-ERR", 90000, "ExpertoExtremo"),
               asesoria_mala.validar_parametros()),
      
      # 9. Válida: Reserva de sala adicional estándar[cite: 3]
      lambda: (c := Cliente("C007", "Valentina Torres", "valentina@gmail.com"),
               r := Reserva("RES-009", c, sala_vip),
               r.procesar_reserva(horas=5)),
      
      # 10. Inválida: Alquiler de equipo con días en cero[cite: 2, 3]
      lambda: (c := Cliente("C008", "Andrés Parra", "andres@gmail.com"),
               r := Reserva("RES-010", c, equipo_laptop),
               r.procesar_reserva(dias=0))
  ]

  for idx, op in enumerate(operaciones, start=1):
    print(f"--- Ejecutando Operación #{idx} ---")
    try:
      op()
      print(f"Resultado Operación #{idx}: ÉXITO (Procesada correctamente)\n")
    except SoftwareFJError as err:
      print(f"Resultado Operación #{idx}: CONTROLADO (Excepción capturada: {err})\n")
    except Exception as err:
      print(f"Resultado Operación #{idx}: ERROR NO ESPERADO ({err})\n")

  print("=== SIMULACIONES FINALIZADAS. Revise el archivo 'sistema_fj.log' para auditoría. ===")


if __name__ == "__main__":
  ejecutar_simulaciones()
