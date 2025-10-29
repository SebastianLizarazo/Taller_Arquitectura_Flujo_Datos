# 📑 Índice de Navegación del Proyecto

## 🎯 Sistema de Procesamiento de Calificaciones Estudiantiles

### Patrón: Pipes and Filters (Filtros y Tuberías)

---

## 🚀 INICIO RÁPIDO

### ¿Nuevo en el proyecto? Empieza aquí:

1. 📖 **[README.md](README.md)** - Lee esto primero

   - Descripción general del proyecto
   - Requisitos y cómo ejecutar
   - Características principales

2. 🚀 **[GUIA_RAPIDA.md](GUIA_RAPIDA.md)** - Comandos y uso rápido

   - Comandos de ejecución
   - Cómo usar tus propios datos
   - Preguntas frecuentes

3. ▶️ **Ejecutar el sistema**
   ```powershell
   python sistema_calificaciones.py
   ```

---

## 📚 DOCUMENTACIÓN

### Para entender el proyecto en profundidad:

1. 📋 **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** - Vista general completa

   - Objetivos cumplidos
   - Estadísticas del proyecto
   - Resultados de pruebas

2. 📚 **[DOCUMENTACION.md](DOCUMENTACION.md)** - Documentación técnica completa

   - Arquitectura del sistema
   - Explicación del patrón Pipes and Filters
   - Estructura de datos
   - Guía de extensibilidad

3. 🎨 **[DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md)** - Diagramas detallados
   - 7 diagramas ASCII
   - Flujo de datos paso a paso
   - Casos de uso visuales

---

## 💻 CÓDIGO FUENTE

### Archivos de código del sistema:

1. ⭐ **[sistema_calificaciones.py](sistema_calificaciones.py)** - ARCHIVO PRINCIPAL

   - Sistema completo con patrón implementado
   - Clase Pipeline
   - 3 filtros (validación, cálculo, clasificación)
   - Funciones de I/O
   - ~380 líneas

2. 🔧 **[ejemplo_extensibilidad.py](ejemplo_extensibilidad.py)** - Demo de extensibilidad

   - Sistema extendido con 7 filtros
   - 4 filtros adicionales
   - Demuestra escalabilidad del patrón
   - ~180 líneas

3. 🧪 **[test_sistema.py](test_sistema.py)** - Tests unitarios
   - 20 tests completos
   - Cobertura de todos los componentes
   - Tests de integración
   - ~340 líneas

---

## 📊 DATOS

### Archivos de entrada y salida:

1. 📝 **[estudiantes.json](estudiantes.json)** - Datos de entrada

   - 10 estudiantes de ejemplo
   - Formato editable
   - Incluye casos válidos e inválidos

2. 📊 **[resultados_calificaciones.json](resultados_calificaciones.json)** - Resultados
   - Generado automáticamente
   - Contiene datos procesados
   - Formato JSON legible

---

## 🎯 POR CASO DE USO

### ¿Qué quieres hacer?

#### 📖 Quiero entender el proyecto

1. Leer [README.md](README.md)
2. Leer [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)
3. Ver [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md)

#### 🚀 Quiero ejecutar el sistema

1. Leer [GUIA_RAPIDA.md](GUIA_RAPIDA.md)
2. Ejecutar `python sistema_calificaciones.py`
3. Ver resultados en consola y archivo JSON

#### 🔧 Quiero modificar/extender el sistema

1. Leer [DOCUMENTACION.md](DOCUMENTACION.md) sección "Extensibilidad"
2. Ver [ejemplo_extensibilidad.py](ejemplo_extensibilidad.py) como referencia
3. Agregar tus propios filtros

#### 🧪 Quiero probar el sistema

1. Ejecutar `python test_sistema.py`
2. Ver [test_sistema.py](test_sistema.py) para entender las pruebas

#### 📊 Quiero usar mis propios datos

1. Editar [estudiantes.json](estudiantes.json)
2. Seguir instrucciones en [GUIA_RAPIDA.md](GUIA_RAPIDA.md)
3. Ejecutar el sistema

#### 🎓 Quiero estudiar el patrón Pipes and Filters

1. Leer [DOCUMENTACION.md](DOCUMENTACION.md) sección "Patrón"
2. Ver [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md)
3. Estudiar [sistema_calificaciones.py](sistema_calificaciones.py) clase Pipeline

---

## 📁 ESTRUCTURA DEL PROYECTO

```
Taller_Arquitectura_Flujo_Datos/
│
├── 📑 INDICE.md                         # ← ESTÁS AQUÍ
├── 📖 README.md                         # Descripción general
├── 📋 RESUMEN_EJECUTIVO.md              # Resumen completo del proyecto
│
├── 📚 Documentación/
│   ├── DOCUMENTACION.md                 # Documentación técnica completa
│   ├── DIAGRAMAS_VISUALES.md            # 7 diagramas detallados
│   └── GUIA_RAPIDA.md                   # Guía de inicio rápido
│
├── 💻 Código Fuente/
│   ├── sistema_calificaciones.py       # ⭐ SISTEMA PRINCIPAL
│   ├── ejemplo_extensibilidad.py       # Demo de extensibilidad
│   └── test_sistema.py                  # Tests unitarios
│
└── 📊 Datos/
    ├── estudiantes.json                 # Datos de entrada
    └── resultados_calificaciones.json   # Resultados (generado)
```

---

## 🔍 BÚSQUEDA RÁPIDA

### ¿Buscas algo específico?

| Busco...                  | Lo encuentro en...                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------- |
| Cómo ejecutar el sistema  | [GUIA_RAPIDA.md](GUIA_RAPIDA.md)                                                      |
| Diagrama de arquitectura  | [DOCUMENTACION.md](DOCUMENTACION.md) o [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md) |
| Explicación del patrón    | [DOCUMENTACION.md](DOCUMENTACION.md) sección "Integración del Patrón"                 |
| Código de ejemplo         | [sistema_calificaciones.py](sistema_calificaciones.py)                                |
| Cómo agregar filtros      | [DOCUMENTACION.md](DOCUMENTACION.md) sección "Extensibilidad"                         |
| Tests del sistema         | [test_sistema.py](test_sistema.py)                                                    |
| Datos de prueba           | [estudiantes.json](estudiantes.json)                                                  |
| Resultados ejemplo        | [resultados_calificaciones.json](resultados_calificaciones.json)                      |
| Estadísticas del proyecto | [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)                                          |
| Casos de uso visuales     | [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md) Diagrama 6                             |

---

## 📖 ORDEN DE LECTURA RECOMENDADO

### Para evaluadores/profesores:

1. 📋 [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) - 5 min

   - Vista general de lo que se logró

2. 🎨 [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md) - 10 min

   - Entender la arquitectura visualmente

3. 📚 [DOCUMENTACION.md](DOCUMENTACION.md) - 15 min

   - Profundizar en el patrón y la implementación

4. ⭐ [sistema_calificaciones.py](sistema_calificaciones.py) - 20 min

   - Revisar el código fuente

5. 🧪 Ejecutar tests: `python test_sistema.py` - 2 min
   - Verificar funcionamiento

### Para estudiantes que aprenden:

1. 📖 [README.md](README.md) - 5 min

   - Entender qué es el proyecto

2. 🚀 [GUIA_RAPIDA.md](GUIA_RAPIDA.md) - 5 min

   - Aprender a ejecutarlo

3. ▶️ Ejecutar: `python sistema_calificaciones.py` - 2 min

   - Ver funcionamiento

4. 📚 [DOCUMENTACION.md](DOCUMENTACION.md) - 20 min

   - Estudiar el patrón en detalle

5. 🎨 [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md) - 15 min

   - Visualizar la arquitectura

6. 💻 [sistema_calificaciones.py](sistema_calificaciones.py) - 30 min

   - Estudiar el código

7. 🔧 [ejemplo_extensibilidad.py](ejemplo_extensibilidad.py) - 15 min

   - Ver cómo extender el sistema

8. 🧪 [test_sistema.py](test_sistema.py) - 15 min
   - Aprender sobre testing

### Para desarrolladores que quieren extender:

1. 📖 [README.md](README.md) - 3 min
2. 💻 [sistema_calificaciones.py](sistema_calificaciones.py) - 20 min
3. 🔧 [ejemplo_extensibilidad.py](ejemplo_extensibilidad.py) - 15 min
4. 📚 [DOCUMENTACION.md](DOCUMENTACION.md) sección "Extensibilidad" - 10 min
5. Empezar a codificar tu extensión

---

## 💡 TIPS DE NAVEGACIÓN

### Atajos útiles:

- **🚀 Inicio rápido**: [GUIA_RAPIDA.md](GUIA_RAPIDA.md)
- **📊 Resumen completo**: [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)
- **🎨 Ver diagramas**: [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md)
- **💻 Código principal**: [sistema_calificaciones.py](sistema_calificaciones.py)
- **❓ FAQ**: [GUIA_RAPIDA.md](GUIA_RAPIDA.md) sección "Preguntas Frecuentes"

### Comandos rápidos:

```powershell
# Ejecutar sistema principal
python sistema_calificaciones.py

# Demo de extensibilidad
python ejemplo_extensibilidad.py

# Ejecutar tests
python test_sistema.py
```

---

## 📞 INFORMACIÓN DEL PROYECTO

**Proyecto**: Sistema de Procesamiento de Calificaciones Estudiantiles  
**Patrón**: Pipes and Filters (Filtros y Tuberías)  
**Lenguaje**: Python 3.7+  
**Archivos**: 11 (3 código + 5 documentación + 2 datos + 1 índice)  
**Líneas de código**: ~900+  
**Tests**: 20 unitarios (100% exitosos)  
**Estado**: ✅ Completado y funcional

---

## 🎓 PARA PROFESORES

### Puntos clave de evaluación:

1. **Patrón correctamente implementado**: Ver [sistema_calificaciones.py](sistema_calificaciones.py) clase `Pipeline`
2. **Tres filtros funcionando**: Validación, Cálculo, Clasificación
3. **Sin archivos intermedios**: Flujo directo en memoria (ver método `ejecutar`)
4. **Documentación completa**: 5 archivos Markdown detallados
5. **Diagramas de arquitectura**: 7 diagramas en [DIAGRAMAS_VISUALES.md](DIAGRAMAS_VISUALES.md)
6. **Tests**: 20 tests unitarios con 100% de éxito

### Rúbrica sugerida:

| Criterio                  | Ubicación                   | Puntos |
| ------------------------- | --------------------------- | ------ |
| Implementación del patrón | `sistema_calificaciones.py` | 30%    |
| Funcionalidad correcta    | Ejecutar + tests            | 30%    |
| Documentación             | Archivos .md                | 20%    |
| Calidad del código        | Todo el código              | 10%    |
| Extensibilidad            | `ejemplo_extensibilidad.py` | 10%    |

---

**¡Bienvenido al proyecto! Navega usando este índice para encontrar lo que necesitas. 🚀**
