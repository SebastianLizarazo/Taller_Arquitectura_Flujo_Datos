# 🚀 Guía Rápida de Uso

## Ejecución de los Scripts

### 1️⃣ Sistema Principal

Ejecuta el sistema de procesamiento de calificaciones:

```powershell
python sistema_calificaciones.py
```

**¿Qué hace?**

- Procesa 8 estudiantes de ejemplo
- Aplica 3 filtros (validación, cálculo, clasificación)
- Muestra resultados en consola
- Guarda resultados en `resultados_calificaciones.json`

---

### 2️⃣ Ejemplo de Extensibilidad

Demuestra cómo agregar nuevos filtros al pipeline:

```powershell
python ejemplo_extensibilidad.py
```

**¿Qué hace?**

- Usa los 3 filtros originales
- Agrega 4 filtros adicionales:
  - Ordenamiento por promedio
  - Cálculo de estadísticas
  - Detección de estudiantes en riesgo
  - Reconocimiento de estudiantes destacados

---

### 3️⃣ Tests Unitarios

Ejecuta las pruebas del sistema:

```powershell
python test_sistema.py
```

**¿Qué hace?**

- Ejecuta 20 tests unitarios
- Verifica cada filtro individualmente
- Prueba el pipeline completo
- Valida casos edge (límites)

---

## Usar Tus Propios Datos

### Opción A: Modificar el archivo JSON

1. Edita `estudiantes.json` con tus datos:

```json
[
  {
    "nombre": "Juan Pérez",
    "asignatura": "Cálculo",
    "nota1": 4.5,
    "nota2": 4.0,
    "nota3": 4.8
  }
]
```

2. En `sistema_calificaciones.py`, busca la función `main()` y cambia:

```python
# Comenta esta línea:
# estudiantes = crear_estudiantes_ejemplo()

# Descomenta esta línea:
estudiantes = cargar_estudiantes_desde_archivo('estudiantes.json')
```

### Opción B: Modificar datos de ejemplo

Edita la función `crear_estudiantes_ejemplo()` en `sistema_calificaciones.py`:

```python
def crear_estudiantes_ejemplo() -> List[Estudiante]:
    return [
        Estudiante("Tu Nombre", "Tu Materia", 4.0, 4.5, 4.8),
        # Agrega más estudiantes aquí...
    ]
```

---

## Estructura de Archivos Generados

```
📁 Taller_Arquitectura_Flujo_Datos/
├── 📄 sistema_calificaciones.py         # Sistema principal ⭐
├── 📄 estudiantes.json                  # Datos de entrada
├── 📄 resultados_calificaciones.json    # Resultados generados 📊
├── 📄 ejemplo_extensibilidad.py         # Demostración de extensibilidad
├── 📄 test_sistema.py                   # Tests unitarios 🧪
├── 📄 DOCUMENTACION.md                  # Documentación completa 📚
├── 📄 README.md                         # Readme principal
└── 📄 GUIA_RAPIDA.md                    # Esta guía
```

---

## Comandos Útiles

### Navegar al directorio

```powershell
cd "h:\Mi unidad\Documentos\Trabajos-UPTC\Semestre-9\Software2\Taller_Arquitectura_Flujo_Datos"
```

### Ejecutar todos los scripts

```powershell
# Sistema principal
python sistema_calificaciones.py

# Ejemplo de extensibilidad
python ejemplo_extensibilidad.py

# Tests
python test_sistema.py
```

### Ver resultados generados

```powershell
# Ver en el explorador
explorer resultados_calificaciones.json

# Ver con PowerShell
cat resultados_calificaciones.json
```

---

## Preguntas Frecuentes

### ❓ ¿Cómo cambio el criterio de aprobación?

En `sistema_calificaciones.py`, busca la función `filtro_clasificacion()` y modifica:

```python
NOTA_APROBACION = 3.0  # Cambia este valor
```

### ❓ ¿Cómo agrego un nuevo filtro?

1. Crea tu función filtro:

```python
def mi_filtro(estudiantes: List[Estudiante]) -> List[Estudiante]:
    # Tu lógica aquí
    return estudiantes
```

2. Agrégalo al pipeline en `main()`:

```python
pipeline.agregar_filtro(mi_filtro)
```

### ❓ ¿Cómo cambio el rango de notas válidas?

En `filtro_validacion()`, modifica las validaciones:

```python
if nota < 0 or nota > 5:  # Cambia estos valores
```

---

## Características del Sistema

✅ **Validación automática** de notas [0-5]  
✅ **Cálculo de promedios** con precisión de 2 decimales  
✅ **Clasificación** (APROBADO/NO APROBADO/DATOS INVÁLIDOS)  
✅ **Visualización** formateada en consola  
✅ **Persistencia** de resultados en JSON  
✅ **Extensible** - fácil agregar nuevos filtros  
✅ **Testeable** - 20 tests unitarios incluidos

---

## Patrón Implementado

**Pipes and Filters** (Filtros y Tuberías)

```
Datos → [Validación] → [Cálculo] → [Clasificación] → Resultados
```

### Ventajas

- 🧩 **Modular**: Cada filtro es independiente
- ♻️ **Reutilizable**: Los filtros pueden usarse en otros pipelines
- 🔧 **Mantenible**: Fácil corregir cada componente
- 📈 **Escalable**: Agregar filtros sin afectar existentes
- 🧪 **Testeable**: Pruebas unitarias por filtro

---

## Soporte

Para más información, consulta:

- 📚 [DOCUMENTACION.md](DOCUMENTACION.md) - Documentación completa con diagramas
- 📖 [README.md](README.md) - Descripción general del proyecto

---

**¡Listo para usar! 🎉**
