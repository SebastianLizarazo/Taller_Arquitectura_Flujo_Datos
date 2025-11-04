from typing import Dict, List, Any, Callable
from dataclasses import dataclass
import json


@dataclass
class Estudiante:
    """Clase que representa un estudiante con sus calificaciones"""
    nombre: str
    asignatura: str
    nota1: float
    nota2: float
    nota3: float
    promedio: float = 0.0
    estado: str = ""
    valido: bool = True
    mensaje_error: str = ""


class Pipeline:
    """
    Clase que implementa el patrón de Tuberías (Pipeline).
    Permite encadenar filtros de procesamiento de datos.
    """

    def __init__(self):
        self.filtros: List[Callable] = []

    def agregar_filtro(self, filtro: Callable):
        """Agrega un filtro a la tubería"""
        self.filtros.append(filtro)
        return self

    def ejecutar(self, datos: List[Any]) -> List[Any]:
        """
        Ejecuta todos los filtros en secuencia.
        Los datos fluyen a través de cada filtro.
        """
        resultado = datos
        for filtro in self.filtros:
            resultado = filtro(resultado)
        return resultado


# ==================== FILTROS ====================

def filtro_validacion(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO 1: Validación de Notas
    Valida que todas las notas estén en el rango [0, 5]
    """
    print("\nFILTRO 1: Validando notas...")
    estudiantes_validados = []

    for estudiante in estudiantes:
        notas = [estudiante.nota1, estudiante.nota2, estudiante.nota3]

        # Validar que todas las notas estén entre 0 y 5
        notas_invalidas = [nota for nota in notas if nota < 0 or nota > 5]

        if notas_invalidas:
            estudiante.valido = False
            estudiante.mensaje_error = f"Notas fuera del rango [0-5]: {notas_invalidas}"
            print(
                f"{estudiante.nombre} - {estudiante.asignatura}: {estudiante.mensaje_error}")
        else:
            estudiante.valido = True
            print(
                f"{estudiante.nombre} - {estudiante.asignatura}: Notas válidas")

        estudiantes_validados.append(estudiante)

    return estudiantes_validados


def filtro_calculo_promedio(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO 2: Cálculo de Promedio
    Calcula el promedio de las tres notas para cada estudiante
    """
    print("\nFILTRO 2: Calculando promedios...")

    for estudiante in estudiantes:
        if estudiante.valido:
            estudiante.promedio = (
                estudiante.nota1 + estudiante.nota2 + estudiante.nota3) / 3
            print(
                f"{estudiante.nombre} - {estudiante.asignatura}: Promedio = {estudiante.promedio:.2f}")
        else:
            estudiante.promedio = 0.0
            print(
                f"{estudiante.nombre} - {estudiante.asignatura}: Sin promedio (datos inválidos)")

    return estudiantes


def filtro_clasificacion(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO 3: Clasificación
    Clasifica a los estudiantes como "APROBADO" o "NO APROBADO"
    Criterio: Promedio >= 3.0 para aprobar
    """
    print("\nFILTRO 3: Clasificando estudiantes...")
    NOTA_APROBACION = 3.0

    for estudiante in estudiantes:
        if estudiante.valido:
            if estudiante.promedio >= NOTA_APROBACION:
                estudiante.estado = "APROBADO"
                print(
                    f"{estudiante.nombre} - {estudiante.asignatura}: APROBADO ({estudiante.promedio:.2f})")
            else:
                estudiante.estado = "NO APROBADO"
                print(
                    f"{estudiante.nombre} - {estudiante.asignatura}: NO APROBADO ({estudiante.promedio:.2f})")
        else:
            estudiante.estado = "DATOS INVÁLIDOS"
            print(
                f"{estudiante.nombre} - {estudiante.asignatura}: DATOS INVÁLIDOS")

    return estudiantes


def cargar_estudiantes_desde_archivo(ruta_archivo: str) -> List[Estudiante]:
    """
    Carga los datos de estudiantes desde un archivo JSON
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            estudiantes = [
                Estudiante(
                    nombre=e['nombre'],
                    asignatura=e['asignatura'],
                    nota1=e['nota1'],
                    nota2=e['nota2'],
                    nota3=e['nota3']
                )
                for e in datos
            ]
            return estudiantes
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        return []
    except json.JSONDecodeError:
        print(
            f"Error: El archivo '{ruta_archivo}' no tiene un formato JSON válido")
        return []
    except KeyError as e:
        print(f"Error: Falta el campo {e} en los datos")
        return []


def crear_estudiantes_ejemplo() -> List[Estudiante]:
    """
    Crea una lista de estudiantes de ejemplo para demostración
    """
    return [
        Estudiante("Ana García", "Matemáticas", 4.5, 4.0, 4.8),
        Estudiante("Carlos Pérez", "Física", 3.5, 3.0, 3.2),
        Estudiante("María López", "Química", 2.5, 2.8, 2.3),
        Estudiante("Juan Martínez", "Programación", 5.0, 4.9, 5.0),
        Estudiante("Laura Rodríguez", "Base de Datos", 3.0, 3.0, 3.0),
        Estudiante("Pedro Sánchez", "Inglés", 1.5, 2.0, 1.8),
        Estudiante("Sofia Torres", "Arquitectura SW",
                   6.0, 4.5, 3.5),  # Nota inválida
        Estudiante("Diego Ramírez", "Redes", 4.2, -1.0, 4.0),  # Nota inválida
    ]


def mostrar_resultados(estudiantes: List[Estudiante]):
    """
    Muestra los resultados finales en consola
    """
    print("\n" + "="*80)
    print("RESULTADOS FINALES".center(80))
    print("="*80)

    aprobados = [e for e in estudiantes if e.estado == "APROBADO"]
    no_aprobados = [e for e in estudiantes if e.estado == "NO APROBADO"]
    invalidos = [e for e in estudiantes if e.estado == "DATOS INVÁLIDOS"]

    print(f"\nESTADÍSTICAS:")
    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Aprobados: {len(aprobados)}")
    print(f"No Aprobados: {len(no_aprobados)}")
    print(f"Datos Inválidos: {len(invalidos)}")

    print(f"\n{'NOMBRE':<20} {'ASIGNATURA':<20} {'N1':<6} {'N2':<6} {'N3':<6} {'PROM':<6} {'ESTADO':<15}")
    print("-" * 80)

    for estudiante in estudiantes:
        if estudiante.valido:
            print(f"{estudiante.nombre:<20} {estudiante.asignatura:<20} "
                  f"{estudiante.nota1:<6.1f} {estudiante.nota2:<6.1f} {estudiante.nota3:<6.1f} "
                  f"{estudiante.promedio:<6.2f} {estudiante.estado:<15}")
        else:
            print(f"{estudiante.nombre:<20} {estudiante.asignatura:<20} "
                  f"{estudiante.nota1:<6.1f} {estudiante.nota2:<6.1f} {estudiante.nota3:<6.1f} "
                  f"{'N/A':<6} {estudiante.estado:<15}")
            print(f"   └─ Error: {estudiante.mensaje_error}")


def guardar_resultados(estudiantes: List[Estudiante], ruta_archivo: str):
    """
    Guarda los resultados en un archivo JSON
    """
    resultados = []
    for estudiante in estudiantes:
        resultados.append({
            'nombre': estudiante.nombre,
            'asignatura': estudiante.asignatura,
            'nota1': estudiante.nota1,
            'nota2': estudiante.nota2,
            'nota3': estudiante.nota3,
            'promedio': round(estudiante.promedio, 2),
            'estado': estudiante.estado,
            'valido': estudiante.valido,
            'mensaje_error': estudiante.mensaje_error if not estudiante.valido else ""
        })

    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(resultados, archivo, indent=4, ensure_ascii=False)
        print(f"\nResultados guardados en: {ruta_archivo}")
        return True
    except Exception as e:
        print(f"\nError al guardar resultados: {e}")
        return False


def main():
    """
    Función principal que ejecuta el sistema de procesamiento
    """
    print("SISTEMA DE PROCESAMIENTO DE CALIFICACIONES ESTUDIANTILES".center(80))

    # Opción 1: Usar datos de ejemplo
    estudiantes = crear_estudiantes_ejemplo()

    # Opción 2: Cargar desde archivo (descomenta para usar)
    # estudiantes = cargar_estudiantes_desde_archivo('estudiantes.json')

    if not estudiantes:
        print("No hay datos de estudiantes para procesar")
        return

    print(f"Se cargaron {len(estudiantes)} estudiantes")

    # Crear el pipeline y agregar los filtros
    print("\nCreación de la tubería de procesamiento")
    pipeline = Pipeline()
    pipeline.agregar_filtro(filtro_validacion)
    pipeline.agregar_filtro(filtro_calculo_promedio)
    pipeline.agregar_filtro(filtro_clasificacion)
    print("Tubería construida con 3 filtros")

    # Ejecutar el pipeline
    print("-" * 80)

    resultados = pipeline.ejecutar(estudiantes)

    # Mostrar resultados
    mostrar_resultados(resultados)

    # Guardar resultados
    guardar_resultados(resultados, 'resultados_calificaciones.json')


if __name__ == "__main__":
    main()
