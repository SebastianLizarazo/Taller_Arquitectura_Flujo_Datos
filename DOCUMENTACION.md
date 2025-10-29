# 📚 Documentación del Sistema de Procesamiento de Calificaciones Estudiantiles

## 🎯 Descripción General

Este sistema implementa el **patrón arquitectónico de Filtros y Tuberías (Pipes and Filters)** para procesar calificaciones estudiantiles de manera modular, escalable y mantenible.

---

## 🏗️ Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ENTRADA DE DATOS                                     │
│                                                                               │
│  ┌──────────────────┐              ┌──────────────────┐                     │
│  │  Datos Ejemplo   │              │  Archivo JSON    │                     │
│  │  (en código)     │              │  (estudiantes)   │                     │
│  └────────┬─────────┘              └────────┬─────────┘                     │
│           │                                  │                               │
│           └──────────────┬───────────────────┘                               │
│                          │                                                   │
│                          ▼                                                   │
│              ┌───────────────────────┐                                       │
│              │   Lista Estudiantes   │                                       │
│              │   (Datos sin procesar)│                                       │
│              └───────────┬───────────┘                                       │
│                          │                                                   │
└──────────────────────────┼───────────────────────────────────────────────────┘
                           │
                           │ FLUJO DE DATOS
                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TUBERÍA (PIPELINE)                                  │
│                                                                               │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         FILTRO 1                                       │  │
│  │                    Validación de Notas                                 │  │
│  │  ┌──────────────────────────────────────────────────────────────┐     │  │
│  │  │  • Recibe: Lista de estudiantes con notas                    │     │  │
│  │  │  • Procesa: Valida rango [0-5] para cada nota                │     │  │
│  │  │  • Marca: estudiante.valido = True/False                      │     │  │
│  │  │  • Emite: Lista de estudiantes validados                      │     │  │
│  │  └──────────────────────────────────────────────────────────────┘     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                           │                                                  │
│                           │ FLUJO DE DATOS (Stream)                          │
│                           ▼                                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         FILTRO 2                                       │  │
│  │                  Cálculo de Promedios                                  │  │
│  │  ┌──────────────────────────────────────────────────────────────┐     │  │
│  │  │  • Recibe: Lista de estudiantes validados                    │     │  │
│  │  │  • Procesa: Calcula promedio = (N1 + N2 + N3) / 3            │     │  │
│  │  │  • Asigna: estudiante.promedio                                │     │  │
│  │  │  • Emite: Lista de estudiantes con promedios                  │     │  │
│  │  └──────────────────────────────────────────────────────────────┘     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                           │                                                  │
│                           │ FLUJO DE DATOS (Stream)                          │
│                           ▼                                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         FILTRO 3                                       │  │
│  │                     Clasificación                                      │  │
│  │  ┌──────────────────────────────────────────────────────────────┐     │  │
│  │  │  • Recibe: Lista de estudiantes con promedios                │     │  │
│  │  │  • Procesa: Evalúa promedio >= 3.0                            │     │  │
│  │  │  • Clasifica: APROBADO / NO APROBADO / DATOS INVÁLIDOS        │     │  │
│  │  │  • Emite: Lista de estudiantes clasificados                   │     │  │
│  │  └──────────────────────────────────────────────────────────────┘     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                           │                                                  │
└───────────────────────────┼──────────────────────────────────────────────────┘
                            │
                            │ DATOS PROCESADOS
                            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SALIDA DE DATOS                                    │
│                                                                               │
│  ┌─────────────────────┐              ┌─────────────────────┐               │
│  │  Mostrar en Consola │              │  Guardar en Archivo │               │
│  │  (Formato Tabla)    │              │  JSON (Resultados)  │               │
│  └─────────────────────┘              └─────────────────────┘               │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Integración del Patrón Filtros y Tuberías

### 📖 ¿Qué es el Patrón Pipes and Filters?

El patrón **Pipes and Filters** es un estilo arquitectónico que organiza el procesamiento de datos como una secuencia de componentes de procesamiento (filtros) conectados por canales de comunicación (tuberías).

### 🎯 Características del Patrón en este Sistema

#### 1. **Filtros (Filters)**

Cada filtro es una función independiente y reutilizable que:

- **Recibe datos** de entrada
- **Transforma** los datos
- **Emite datos** de salida

**Filtros implementados:**

| Filtro       | Función                     | Entrada                           | Salida                                      |
| ------------ | --------------------------- | --------------------------------- | ------------------------------------------- |
| **Filtro 1** | `filtro_validacion()`       | Lista de estudiantes sin validar  | Lista de estudiantes con flag de validación |
| **Filtro 2** | `filtro_calculo_promedio()` | Lista de estudiantes validados    | Lista de estudiantes con promedio calculado |
| **Filtro 3** | `filtro_clasificacion()`    | Lista de estudiantes con promedio | Lista de estudiantes clasificados           |

#### 2. **Tuberías (Pipes)**

La clase `Pipeline` actúa como la tubería que:

- **Conecta** los filtros en secuencia
- **Gestiona** el flujo de datos entre filtros
- **Ejecuta** todos los filtros en orden

```python
class Pipeline:
    def __init__(self):
        self.filtros: List[Callable] = []

    def agregar_filtro(self, filtro: Callable):
        """Agrega un filtro a la tubería"""
        self.filtros.append(filtro)
        return self

    def ejecutar(self, datos: List[Any]) -> List[Any]:
        """Ejecuta todos los filtros en secuencia"""
        resultado = datos
        for filtro in self.filtros:
            resultado = filtro(resultado)
        return resultado
```

#### 3. **Flujo de Datos (Data Stream)**

Los datos fluyen de manera continua y unidireccional:

```
Datos Entrada → Filtro 1 → Filtro 2 → Filtro 3 → Datos Salida
```

**Sin archivos intermedios**: Los datos se mantienen en memoria y fluyen directamente entre filtros mediante el retorno de funciones.

### 🔄 Proceso de Ejecución

1. **Construcción del Pipeline**:

```python
pipeline = Pipeline()
pipeline.agregar_filtro(filtro_validacion)
pipeline.agregar_filtro(filtro_calculo_promedio)
pipeline.agregar_filtro(filtro_clasificacion)
```

2. **Ejecución del Flujo**:

```python
resultados = pipeline.ejecutar(estudiantes)
```

3. **Flujo Interno**:
   - Los datos entran al pipeline como una lista de objetos `Estudiante`
   - Pasan por el **Filtro 1** (validación)
   - El resultado fluye al **Filtro 2** (cálculo)
   - El resultado fluye al **Filtro 3** (clasificación)
   - Se obtienen los datos procesados finales

---

## 🎨 Ventajas de la Arquitectura Implementada

### ✅ Modularidad

- Cada filtro es independiente y puede modificarse sin afectar a los demás
- Fácil agregar nuevos filtros (ej: filtro de estadísticas, filtro de notificaciones)

### ✅ Reutilización

- Los filtros pueden usarse en diferentes pipelines
- Código limpio y sin duplicación

### ✅ Mantenibilidad

- Fácil identificar y corregir errores en filtros específicos
- Código organizado y legible

### ✅ Escalabilidad

- Fácil agregar nuevos filtros al pipeline
- Posibilidad de paralelizar filtros independientes en el futuro

### ✅ Testabilidad

- Cada filtro puede probarse de forma aislada
- Fácil crear pruebas unitarias para cada componente

---

## 🚀 Características del Sistema

### Funcionalidades Principales

1. **Validación de Notas**

   - Verifica que todas las notas estén en el rango [0, 5]
   - Marca estudiantes con datos inválidos
   - Reporta errores específicos

2. **Cálculo de Promedio**

   - Calcula el promedio aritmético: `(Nota1 + Nota2 + Nota3) / 3`
   - Solo procesa estudiantes con datos válidos
   - Redondea a 2 decimales

3. **Clasificación**

   - **APROBADO**: Promedio >= 3.0
   - **NO APROBADO**: Promedio < 3.0
   - **DATOS INVÁLIDOS**: Notas fuera del rango permitido

4. **Visualización de Resultados**

   - Muestra tabla formateada en consola
   - Incluye estadísticas generales
   - Identifica errores claramente

5. **Persistencia de Datos**
   - Guarda resultados en formato JSON
   - Conserva toda la información procesada
   - Facilita auditoría y análisis posterior

---

## 📊 Estructura de Datos

### Clase Estudiante

```python
@dataclass
class Estudiante:
    nombre: str              # Nombre del estudiante
    asignatura: str          # Asignatura cursada
    nota1: float            # Primera nota [0-5]
    nota2: float            # Segunda nota [0-5]
    nota3: float            # Tercera nota [0-5]
    promedio: float = 0.0   # Promedio calculado
    estado: str = ""        # APROBADO / NO APROBADO / DATOS INVÁLIDOS
    valido: bool = True     # Flag de validación
    mensaje_error: str = "" # Descripción del error (si aplica)
```

---

## 💻 Uso del Sistema

### Opción 1: Datos de Ejemplo (Predeterminado)

```python
# En main(), esta línea está activa por defecto:
estudiantes = crear_estudiantes_ejemplo()
```

### Opción 2: Cargar desde Archivo JSON

1. Crea un archivo `estudiantes.json` con el formato:

```json
[
  {
    "nombre": "Ana García",
    "asignatura": "Matemáticas",
    "nota1": 4.5,
    "nota2": 4.0,
    "nota3": 4.8
  }
]
```

2. Modifica la función `main()`:

```python
# Comenta esta línea:
# estudiantes = crear_estudiantes_ejemplo()

# Descomenta esta línea:
estudiantes = cargar_estudiantes_desde_archivo('estudiantes.json')
```

### Ejecución

```bash
python sistema_calificaciones.py
```

### Salida Esperada

```
================================================================================
      🎓 SISTEMA DE PROCESAMIENTO DE CALIFICACIONES ESTUDIANTILES
              Patrón: Filtros y Tuberías (Pipes and Filters)
================================================================================

📝 Cargando datos de estudiantes...
✓ Se cargaron 8 estudiantes

🔧 Construyendo la tubería de procesamiento...
✓ Tubería construida con 3 filtros

🚀 Iniciando procesamiento a través de la tubería...
--------------------------------------------------------------------------------

🔍 FILTRO 1: Validando notas...
   ✓ Ana García - Matemáticas: Notas válidas
   ...

📊 FILTRO 2: Calculando promedios...
   📈 Ana García - Matemáticas: Promedio = 4.43
   ...

🎯 FILTRO 3: Clasificando estudiantes...
   ✅ Ana García - Matemáticas: APROBADO (4.43)
   ...

================================================================================
                   📋 RESULTADOS FINALES DEL PROCESAMIENTO
================================================================================

📊 ESTADÍSTICAS:
   Total de estudiantes: 8
   ✅ Aprobados: 4
   ❌ No Aprobados: 2
   ⚠️  Datos Inválidos: 2

[Tabla de resultados...]

💾 Resultados guardados en: resultados_calificaciones.json

================================================================================
                    ✅ Procesamiento completado exitosamente
================================================================================
```

---

## 🔮 Extensibilidad del Sistema

### Agregar Nuevos Filtros

Es muy fácil agregar nuevos filtros al pipeline:

```python
def filtro_estadisticas(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """Filtro adicional para calcular estadísticas"""
    # Lógica del filtro
    return estudiantes

# Agregar al pipeline:
pipeline.agregar_filtro(filtro_estadisticas)
```

### Ejemplos de Filtros Adicionales

1. **Filtro de Ordenamiento**: Ordenar por promedio
2. **Filtro de Estadísticas**: Calcular media, mediana, desviación estándar
3. **Filtro de Notificaciones**: Enviar emails a estudiantes
4. **Filtro de Reportes**: Generar PDF con resultados
5. **Filtro de Alertas**: Detectar estudiantes en riesgo

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.7+
- **Librerías estándar**:
  - `typing`: Para type hints y mejor documentación
  - `dataclasses`: Para definir clases de datos
  - `json`: Para manejo de archivos JSON

---

## 📝 Conclusiones

Este sistema demuestra efectivamente la implementación del patrón **Pipes and Filters** con:

✅ **Tres filtros independientes** conectados secuencialmente  
✅ **Flujo de datos continuo** sin archivos intermedios  
✅ **Funciones encadenadas** mediante el objeto Pipeline  
✅ **Procesamiento modular** y extensible  
✅ **Código limpio** y bien documentado  
✅ **Separación de responsabilidades** clara entre componentes

El patrón permite un procesamiento eficiente, mantenible y escalable de las calificaciones estudiantiles, facilitando futuras extensiones y modificaciones del sistema.

---

## 👨‍💻 Autor

Sistema de Procesamiento de Calificaciones Estudiantiles  
**Fecha**: 29 de octubre de 2025  
**Patrón**: Pipes and Filters (Filtros y Tuberías)
