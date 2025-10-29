# 🎨 Diagramas Visuales del Sistema

## Diagrama 1: Arquitectura General del Sistema

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      SISTEMA DE CALIFICACIONES ESTUDIANTILES              ║
║                         Arquitectura Pipes and Filters                    ║
╚═══════════════════════════════════════════════════════════════════════════╝

                                 📥 ENTRADA
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
            ┌───────▼────────┐            ┌────────▼────────┐
            │  Datos Ejemplo │            │  Archivo JSON   │
            │   (hardcoded)  │            │ estudiantes.json│
            └───────┬────────┘            └────────┬────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    │
                        ┌───────────▼───────────┐
                        │  Lista[Estudiante]    │
                        │  - nombre: str        │
                        │  - asignatura: str    │
                        │  - nota1, nota2, nota3│
                        └───────────┬───────────┘
                                    │
╔═══════════════════════════════════▼═══════════════════════════════════════╗
║                              PIPELINE                                     ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────┐    ║
║  │                      FILTRO 1: VALIDACIÓN                        │    ║
║  ├─────────────────────────────────────────────────────────────────┤    ║
║  │  Entrada:  Lista[Estudiante] (sin validar)                      │    ║
║  │  Proceso:  • Verifica 0 ≤ nota ≤ 5 para cada nota               │    ║
║  │            • Marca estudiante.valido = True/False                │    ║
║  │            • Registra mensaje_error si hay problemas             │    ║
║  │  Salida:   Lista[Estudiante] (con flag de validación)           │    ║
║  └─────────────────────────────────────────────────────────────────┘    ║
║                                    │                                      ║
║                                    │ Stream                               ║
║                                    ▼                                      ║
║  ┌─────────────────────────────────────────────────────────────────┐    ║
║  │                 FILTRO 2: CÁLCULO DE PROMEDIO                    │    ║
║  ├─────────────────────────────────────────────────────────────────┤    ║
║  │  Entrada:  Lista[Estudiante] (validados)                        │    ║
║  │  Proceso:  • Si valido: promedio = (N1+N2+N3)/3                 │    ║
║  │            • Si no valido: promedio = 0.0                        │    ║
║  │            • Redondeo a 2 decimales                              │    ║
║  │  Salida:   Lista[Estudiante] (con promedios)                    │    ║
║  └─────────────────────────────────────────────────────────────────┘    ║
║                                    │                                      ║
║                                    │ Stream                               ║
║                                    ▼                                      ║
║  ┌─────────────────────────────────────────────────────────────────┐    ║
║  │                   FILTRO 3: CLASIFICACIÓN                        │    ║
║  ├─────────────────────────────────────────────────────────────────┤    ║
║  │  Entrada:  Lista[Estudiante] (con promedios)                    │    ║
║  │  Proceso:  • Si valido y promedio ≥ 3.0: "APROBADO"             │    ║
║  │            • Si valido y promedio < 3.0: "NO APROBADO"           │    ║
║  │            • Si no valido: "DATOS INVÁLIDOS"                     │    ║
║  │  Salida:   Lista[Estudiante] (clasificados)                     │    ║
║  └─────────────────────────────────────────────────────────────────┘    ║
║                                    │                                      ║
╚════════════════════════════════════▼══════════════════════════════════════╝
                                     │
                     ┌───────────────┴───────────────┐
                     │                               │
            ┌────────▼─────────┐          ┌─────────▼──────────┐
            │  Mostrar Consola │          │ Guardar Archivo    │
            │  • Tabla         │          │ resultados_*.json  │
            │  • Estadísticas  │          │ • Formato JSON     │
            │  • Emojis        │          │ • UTF-8            │
            └──────────────────┘          └────────────────────┘
                                 📤 SALIDA
```

---

## Diagrama 2: Flujo de Datos Detallado

```
ESTUDIANTE: Ana García, Matemáticas, [4.5, 4.0, 4.8]
│
├─ FILTRO 1: Validación
│  ├─ Validar nota1: 4.5 ✓ (0 ≤ 4.5 ≤ 5)
│  ├─ Validar nota2: 4.0 ✓ (0 ≤ 4.0 ≤ 5)
│  ├─ Validar nota3: 4.8 ✓ (0 ≤ 4.8 ≤ 5)
│  └─ Resultado: valido = True ✅
│
├─ FILTRO 2: Cálculo
│  ├─ Es válido: Sí ✓
│  ├─ Calcular: (4.5 + 4.0 + 4.8) / 3
│  └─ Resultado: promedio = 4.43 📊
│
├─ FILTRO 3: Clasificación
│  ├─ Es válido: Sí ✓
│  ├─ Comparar: 4.43 >= 3.0 ✓
│  └─ Resultado: estado = "APROBADO" ✅
│
└─ SALIDA: Ana García | Matemáticas | 4.43 | APROBADO ✅


ESTUDIANTE: Sofia Torres, Arquitectura SW, [6.0, 4.5, 3.5]
│
├─ FILTRO 1: Validación
│  ├─ Validar nota1: 6.0 ✗ (6.0 > 5)
│  ├─ Validar nota2: 4.5 ✓ (0 ≤ 4.5 ≤ 5)
│  ├─ Validar nota3: 3.5 ✓ (0 ≤ 3.5 ≤ 5)
│  └─ Resultado: valido = False ❌
│     mensaje_error = "Notas fuera del rango [0-5]: [6.0]"
│
├─ FILTRO 2: Cálculo
│  ├─ Es válido: No ✗
│  └─ Resultado: promedio = 0.0 (sin calcular)
│
├─ FILTRO 3: Clasificación
│  ├─ Es válido: No ✗
│  └─ Resultado: estado = "DATOS INVÁLIDOS" ⚠️
│
└─ SALIDA: Sofia Torres | Arquitectura SW | N/A | DATOS INVÁLIDOS ⚠️
```

---

## Diagrama 3: Clase Pipeline

```
╔═══════════════════════════════════════════════════════════════╗
║                        CLASE PIPELINE                         ║
╠═══════════════════════════════════════════════════════════════╣
║  Atributos:                                                   ║
║  • filtros: List[Callable]                                    ║
╠═══════════════════════════════════════════════════════════════╣
║  Métodos:                                                     ║
║  • agregar_filtro(filtro: Callable) -> Pipeline               ║
║  • ejecutar(datos: List[Any]) -> List[Any]                    ║
╚═══════════════════════════════════════════════════════════════╝
                              │
                              │ usa
                              ▼
        ┌─────────────────────────────────────────┐
        │         LISTA DE FILTROS                │
        ├─────────────────────────────────────────┤
        │  [0] filtro_validacion                  │
        │  [1] filtro_calculo_promedio            │
        │  [2] filtro_clasificacion               │
        └─────────────────────────────────────────┘
                              │
                              │ ejecutar()
                              ▼
               ┌──────────────────────────┐
               │  for filtro in filtros:  │
               │    datos = filtro(datos) │
               └──────────────────────────┘
```

---

## Diagrama 4: Clase Estudiante

```
╔═══════════════════════════════════════════════════════════════╗
║                    @dataclass ESTUDIANTE                      ║
╠═══════════════════════════════════════════════════════════════╣
║  Atributos de Entrada:                                        ║
║  • nombre: str          (ej: "Ana García")                    ║
║  • asignatura: str      (ej: "Matemáticas")                   ║
║  • nota1: float         (rango: [0, 5])                       ║
║  • nota2: float         (rango: [0, 5])                       ║
║  • nota3: float         (rango: [0, 5])                       ║
╠═══════════════════════════════════════════════════════════════╣
║  Atributos Procesados:                                        ║
║  • promedio: float = 0.0        (calculado en Filtro 2)       ║
║  • estado: str = ""             (calculado en Filtro 3)       ║
║  • valido: bool = True          (validado en Filtro 1)        ║
║  • mensaje_error: str = ""      (validado en Filtro 1)        ║
╚═══════════════════════════════════════════════════════════════╝

Estado del Objeto en cada Filtro:
───────────────────────────────────────────────────────────────

Antes del Pipeline:
┌──────────────────────────────────────────────┐
│ nombre: "Ana García"                         │
│ asignatura: "Matemáticas"                    │
│ nota1: 4.5, nota2: 4.0, nota3: 4.8           │
│ promedio: 0.0                                │
│ estado: ""                                   │
│ valido: True                                 │
│ mensaje_error: ""                            │
└──────────────────────────────────────────────┘

Después del Filtro 1 (Validación):
┌──────────────────────────────────────────────┐
│ nombre: "Ana García"                         │
│ asignatura: "Matemáticas"                    │
│ nota1: 4.5, nota2: 4.0, nota3: 4.8           │
│ promedio: 0.0                                │
│ estado: ""                                   │
│ valido: True ✅                              │
│ mensaje_error: ""                            │
└──────────────────────────────────────────────┘

Después del Filtro 2 (Cálculo):
┌──────────────────────────────────────────────┐
│ nombre: "Ana García"                         │
│ asignatura: "Matemáticas"                    │
│ nota1: 4.5, nota2: 4.0, nota3: 4.8           │
│ promedio: 4.43 📊                            │
│ estado: ""                                   │
│ valido: True                                 │
│ mensaje_error: ""                            │
└──────────────────────────────────────────────┘

Después del Filtro 3 (Clasificación):
┌──────────────────────────────────────────────┐
│ nombre: "Ana García"                         │
│ asignatura: "Matemáticas"                    │
│ nota1: 4.5, nota2: 4.0, nota3: 4.8           │
│ promedio: 4.43                               │
│ estado: "APROBADO" ✅                        │
│ valido: True                                 │
│ mensaje_error: ""                            │
└──────────────────────────────────────────────┘
```

---

## Diagrama 5: Extensibilidad del Sistema

```
Pipeline Original (3 filtros):
════════════════════════════════════════════════════════
Datos → [Validación] → [Cálculo] → [Clasificación] → Salida


Pipeline Extendido (7 filtros):
════════════════════════════════════════════════════════════════════
Datos → [Validación] → [Cálculo] → [Clasificación] → [Ordenamiento]
          │              │             │                  │
          └──────────────┴─────────────┴──────────────────┘
                               │
                               ▼
        [Estadísticas] → [Alertas] → [Reconocimientos] → Salida

Nuevos filtros agregados SIN modificar el código original! ✨
```

---

## Diagrama 6: Casos de Uso

```
┌─────────────┐
│  Usuario    │
└──────┬──────┘
       │
       ├─────────────► Procesar calificaciones (sistema_calificaciones.py)
       │               │
       │               ├─ Validar notas
       │               ├─ Calcular promedios
       │               ├─ Clasificar estudiantes
       │               └─ Ver resultados
       │
       ├─────────────► Demostrar extensibilidad (ejemplo_extensibilidad.py)
       │               │
       │               ├─ Todos los filtros originales
       │               ├─ + Ordenamiento
       │               ├─ + Estadísticas
       │               ├─ + Detectar riesgo
       │               └─ + Reconocimientos
       │
       └─────────────► Ejecutar tests (test_sistema.py)
                       │
                       ├─ Tests unitarios de filtros
                       ├─ Tests del pipeline
                       └─ Tests de integración
```

---

## Diagrama 7: Comparación de Resultados

```
ENTRADA: 8 Estudiantes
┌────────────────────┬──────────────┬─────────────────────────┐
│     Estudiante     │  Promedio    │       Resultado         │
├────────────────────┼──────────────┼─────────────────────────┤
│ Ana García         │    4.43      │  ✅ APROBADO            │
│ Carlos Pérez       │    3.23      │  ✅ APROBADO            │
│ María López        │    2.53      │  ❌ NO APROBADO         │
│ Juan Martínez      │    4.97      │  ✅ APROBADO            │
│ Laura Rodríguez    │    3.00      │  ✅ APROBADO (límite)   │
│ Pedro Sánchez      │    1.77      │  ❌ NO APROBADO         │
│ Sofia Torres       │    N/A       │  ⚠️  DATOS INVÁLIDOS    │
│ Diego Ramírez      │    N/A       │  ⚠️  DATOS INVÁLIDOS    │
└────────────────────┴──────────────┴─────────────────────────┘

ESTADÍSTICAS:
─────────────────────────────────────────────────────
📊 Total:               8 estudiantes
✅ Aprobados:          4 estudiantes (50%)
❌ No Aprobados:       2 estudiantes (25%)
⚠️  Datos Inválidos:   2 estudiantes (25%)

📈 Promedio General:   3.32
🔝 Promedio Máximo:    4.97 (Juan Martínez)
🔻 Promedio Mínimo:    1.77 (Pedro Sánchez)
```


