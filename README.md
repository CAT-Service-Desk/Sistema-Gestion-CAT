# Sistema de Gestión de Servicios CAT

Este proyecto tiene como objetivo modernizar el proceso de gestión de solicitudes de soporte técnico del Centro de Atención Tecnológica (CAT).

## Requerimientos Funcionales
1. **Gestión de Tickets:** Creación de solicitudes con evidencia adjunta.
2. **Asignación:** El administrador puede asignar tickets a técnicos específicos.
3. **Trazabilidad:** Cambio de estados (Abierto, En Progreso, Resuelto) y notificaciones.
4. **Historial:** Los usuarios pueden ver sus solicitudes pasadas.
5. **Reportes:** Generación de métricas de desempeño mensual.

## Requerimientos No Funcionales
1. **Seguridad:** Encriptación de contraseñas (bcrypt).
2. **Disponibilidad:** 99.9% en horario académico.
3. **Usabilidad:** Diseño Responsive (móvil y escritorio).
4. **Rendimiento:** Carga menor a 2 segundos.
5. **Escalabilidad:** Soporte hasta 10,000 tickets anuales.

## Metodología de Estimación: Poker Planning

Para la gestión del esfuerzo y la complejidad de las tareas, utilizamos la técnica de Poker Planning basada en la serie de Fibonacci. 

Hemos clasificado la complejidad mediante Etiquetas (Labels) en GitHub para visualizar rápidamente la carga de trabajo en el tablero Kanban.

## Metodología de Estimación: Poker Planning

Para la gestión del esfuerzo y la complejidad de las tareas, utilizamos la técnica de Poker Planning basada en la serie de Fibonacci.

Hemos clasificado la complejidad mediante Etiquetas (Labels) en GitHub para visualizar rápidamente la carga de trabajo en el tablero Kanban.

### Clasificación de Puntos
| Etiqueta | Puntos | Definición de Complejidad |
| :--- | :---: | :--- |
| `Puntos: 1` | **1** | **Trivial:** Cambios de texto, configuración básica, documentación. |
| `Puntos: 2` | **2** | **Fácil:** Tareas pequeñas con poca lógica de negocio. |
| `Puntos: 3` | **3** | **Media:** Funcionalidades estándar que requieren lógica simple (Frontend + Backend). |
| `Puntos: 5` | **5** | **Compleja:** Tareas que implican lógica avanzada, validaciones múltiples o conexiones externas. |
| `Puntos: 8` | **8** | **Muy Compleja:** Arquitectura base, cambios estructurales o tareas con alta incertidumbre. |

### Justificación
Se eligió esta metodología porque:
1.  **Evita el Sesgo:** Al votar en equipo, se evita que la persona más senior imponga los tiempos.
2.  **Visualización:** El uso de etiquetas permite al *Product Owner* y al *Scrum Master* calcular la "Velocidad del Equipo" (Velocity) sumando los puntos de la columna "Done" al final del Sprint.
3.  **Relatividad:** No estimamos en horas exactas (que suelen fallar), sino en complejidad relativa comparada con otras tareas.
