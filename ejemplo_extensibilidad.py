"""
Ejemplo de Extensibilidad del Sistema
Demuestra cómo agregar nuevos filtros al pipeline
"""

from sistema_calificaciones import (
    Pipeline, Estudiante, crear_estudiantes_ejemplo,
    filtro_validacion, filtro_calculo_promedio, filtro_clasificacion
)
from typing import List


# ==================== NUEVOS FILTROS DE EJEMPLO ====================

def filtro_ordenamiento(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO ADICIONAL 1: Ordenamiento
    Ordena los estudiantes por promedio (de mayor a menor)
    """
    print("\n📋 FILTRO ADICIONAL 1: Ordenando por promedio...")

    estudiantes_validos = [e for e in estudiantes if e.valido]
    estudiantes_invalidos = [e for e in estudiantes if not e.valido]

    # Ordenar estudiantes válidos por promedio descendente
    estudiantes_validos.sort(key=lambda e: e.promedio, reverse=True)

    print(f"   ✓ Estudiantes ordenados por promedio (mayor a menor)")

    # Retornar válidos primero, luego inválidos
    return estudiantes_validos + estudiantes_invalidos


def filtro_estadisticas(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO ADICIONAL 2: Estadísticas
    Calcula y muestra estadísticas generales
    """
    print("\n📊 FILTRO ADICIONAL 2: Calculando estadísticas...")

    estudiantes_validos = [e for e in estudiantes if e.valido]

    if estudiantes_validos:
        promedios = [e.promedio for e in estudiantes_validos]
        promedio_general = sum(promedios) / len(promedios)
        promedio_maximo = max(promedios)
        promedio_minimo = min(promedios)

        print(f"   📈 Promedio General: {promedio_general:.2f}")
        print(f"   🔝 Promedio Máximo: {promedio_maximo:.2f}")
        print(f"   🔻 Promedio Mínimo: {promedio_minimo:.2f}")
        print(f"   👥 Estudiantes Válidos: {len(estudiantes_validos)}")
    else:
        print("   ⚠️  No hay estudiantes válidos para calcular estadísticas")

    return estudiantes


def filtro_alertas(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO ADICIONAL 3: Sistema de Alertas
    Detecta estudiantes en riesgo (promedio entre 2.5 y 3.0)
    """
    print("\n⚠️  FILTRO ADICIONAL 3: Detectando estudiantes en riesgo...")

    estudiantes_en_riesgo = [
        e for e in estudiantes
        if e.valido and 2.5 <= e.promedio < 3.0
    ]

    if estudiantes_en_riesgo:
        print(
            f"   🚨 {len(estudiantes_en_riesgo)} estudiante(s) en riesgo académico:")
        for estudiante in estudiantes_en_riesgo:
            print(
                f"      • {estudiante.nombre} ({estudiante.asignatura}): {estudiante.promedio:.2f}")
    else:
        print("   ✓ No hay estudiantes en riesgo académico")

    return estudiantes


def filtro_reconocimientos(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    FILTRO ADICIONAL 4: Reconocimientos
    Identifica estudiantes destacados (promedio >= 4.5)
    """
    print("\n🏆 FILTRO ADICIONAL 4: Identificando estudiantes destacados...")

    destacados = [
        e for e in estudiantes
        if e.valido and e.promedio >= 4.5
    ]

    if destacados:
        print(
            f"   ⭐ {len(destacados)} estudiante(s) destacado(s) (Promedio >= 4.5):")
        for estudiante in destacados:
            print(
                f"      🌟 {estudiante.nombre} ({estudiante.asignatura}): {estudiante.promedio:.2f}")
    else:
        print("   • No hay estudiantes con promedio >= 4.5")

    return estudiantes


# ==================== FUNCIÓN PRINCIPAL ====================

def main():
    """
    Demuestra la extensibilidad del sistema agregando filtros adicionales
    """
    print("="*80)
    print("🔧 SISTEMA EXTENDIDO - Ejemplo de Extensibilidad".center(80))
    print("Patrón: Filtros y Tuberías con Filtros Adicionales".center(80))
    print("="*80)

    # Cargar datos
    print("\n📝 Cargando datos de estudiantes...")
    estudiantes = crear_estudiantes_ejemplo()
    print(f"✓ Se cargaron {len(estudiantes)} estudiantes")

    # Crear pipeline EXTENDIDO con filtros adicionales
    print("\n🔧 Construyendo la tubería EXTENDIDA...")
    pipeline = Pipeline()

    # Filtros originales
    pipeline.agregar_filtro(filtro_validacion)
    pipeline.agregar_filtro(filtro_calculo_promedio)
    pipeline.agregar_filtro(filtro_clasificacion)

    # Filtros adicionales (¡nuevos!)
    pipeline.agregar_filtro(filtro_ordenamiento)
    pipeline.agregar_filtro(filtro_estadisticas)
    pipeline.agregar_filtro(filtro_alertas)
    pipeline.agregar_filtro(filtro_reconocimientos)

    print("✓ Tubería construida con 7 filtros (3 originales + 4 adicionales)")

    # Ejecutar pipeline
    print("\n🚀 Iniciando procesamiento a través de la tubería extendida...")
    print("-" * 80)

    resultados = pipeline.ejecutar(estudiantes)

    # Mostrar resultados finales
    print("\n" + "="*80)
    print("📋 RESULTADOS FINALES".center(80))
    print("="*80)

    print(f"\n{'NOMBRE':<20} {'ASIGNATURA':<20} {'PROMEDIO':<10} {'ESTADO':<15}")
    print("-" * 80)

    for estudiante in resultados:
        if estudiante.valido:
            emoji = "✅" if estudiante.estado == "APROBADO" else "❌"
            print(f"{emoji} {estudiante.nombre:<18} {estudiante.asignatura:<20} "
                  f"{estudiante.promedio:<10.2f} {estudiante.estado:<15}")
        else:
            print(f"⚠️  {estudiante.nombre:<18} {estudiante.asignatura:<20} "
                  f"{'N/A':<10} {estudiante.estado:<15}")

    print("\n" + "="*80)
    print("✅ Procesamiento completado exitosamente".center(80))
    print("="*80)

    print("\n💡 NOTA:")
    print("   Este ejemplo demuestra la EXTENSIBILIDAD del patrón Pipes and Filters.")
    print("   Se agregaron 4 filtros adicionales sin modificar el código original:")
    print("   • Ordenamiento por promedio")
    print("   • Cálculo de estadísticas")
    print("   • Detección de estudiantes en riesgo")
    print("   • Reconocimiento de estudiantes destacados")


if __name__ == "__main__":
    main()
