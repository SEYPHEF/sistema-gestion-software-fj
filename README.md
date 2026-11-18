# sistema-gestion-software-fj
Sistema integral de gestión de clientes, servicios y reservas para Software FJ (Fase 4 - UNAD).
# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ (Fase 4)

## 📌 Descripción del Proyecto
Componente práctico (Fase 4) del curso de **Programación (Código: 213023_16)** de la Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI) de la Universidad Nacional Abierta y a Distancia (**UNAD**). 

El proyecto implementa una aplicación orientada a objetos sin el uso de bases de datos, diseñada para gestionar clientes, servicios (reservas de salas, alquiler de equipos y asesorías especializadas) y reservas para la empresa simulada **Software FJ**. El sistema destaca por aplicar de forma rigurosa la abstracción, herencia, polimorfismo, encapsulamiento, un manejo avanzado de excepciones y un registro detallado de eventos en archivos de logs.

## 👥 Integrantes del Grupo
- Álvaro José Rubio Mejía
- [Nombre de Integrante 2 (si aplica)]
- [Nombre de Integrante 3 (si aplica)]
- [Nombre de Integrante 4 (si aplica)]
- [Nombre de Integrante 5 (si aplica)]

## 🛠️ Arquitectura y Características Técnicas
- **Programación Orientada a Objetos (POO):** Uso de clases abstractas (`EntidadSistema`, `Servicio`), herencia, polimorfismo en el cálculo de costos y encapsulamiento estricto mediante `@property` y `@setter`.
- **Manejo Robusto de Excepciones:** Clases personalizadas (`SoftwareFJError`, `ClienteInvalidoError`, `ServicioNoDisponibleError`, `ReservaInvalidaError`), bloques `try/except/else/finally` y encadenamiento de excepciones (`raise ... from e`).
- **Auditoría y Logs:** Generación automática de un archivo de registro (`sistema_fj.log`) que almacena la trazabilidad de eventos y errores críticos sin detener la aplicación.
- **Simulaciones:** Ejecución de **10 operaciones completas** que evalúan tanto escenarios válidos como casos inválidos de clientes, servicios y reservas.

## 📂 Estructura del Código Fuente
El proyecto se encuentra modularizado en los siguientes archivos:
- `excepciones.py`: Define la jerarquía de excepciones personalizadas del sistema.
- `modelos.py`: Contiene las clases abstractas, la validación de clientes y los servicios especializados (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`).
- `reservas.py`: Implementa la clase de control `Reserva` y la lógica avanzada de captura de excepciones y estados.
- `main.py`: Configura el sistema de `logging` y ejecuta el bloque secuencial de las 10 simulaciones.

## 🚀 Instrucciones de Ejecución
1. Asegúrate de tener instalado **Python 3** en tu equipo.
2. Clona este repositorio o descarga los archivos en una carpeta local.
3. Abre una terminal en la ruta del proyecto y ejecuta el archivo principal:
   ```bash
   python main.py