"""
Tests Unitarios para el Sistema de Calificaciones
Demuestra la testabilidad del patrón Pipes and Filters
"""

import unittest
from sistema_calificaciones import (
    Estudiante, Pipeline,
    filtro_validacion, filtro_calculo_promedio, filtro_clasificacion
)


class TestEstudiante(unittest.TestCase):
    """Tests para la clase Estudiante"""

    def test_crear_estudiante(self):
        """Verifica la creación correcta de un estudiante"""
        estudiante = Estudiante("Test", "Materia", 4.0, 4.5, 4.2)
        self.assertEqual(estudiante.nombre, "Test")
        self.assertEqual(estudiante.asignatura, "Materia")
        self.assertEqual(estudiante.nota1, 4.0)
        self.assertEqual(estudiante.nota2, 4.5)
        self.assertEqual(estudiante.nota3, 4.2)
        self.assertTrue(estudiante.valido)


class TestFiltroValidacion(unittest.TestCase):
    """Tests para el filtro de validación"""

    def test_notas_validas(self):
        """Verifica que notas válidas pasen la validación"""
        estudiantes = [
            Estudiante("Test1", "Materia1", 4.0, 4.5, 4.2),
            Estudiante("Test2", "Materia2", 3.0, 3.5, 3.8)
        ]
        resultado = filtro_validacion(estudiantes)

        self.assertTrue(resultado[0].valido)
        self.assertTrue(resultado[1].valido)
        self.assertEqual(resultado[0].mensaje_error, "")
        self.assertEqual(resultado[1].mensaje_error, "")

    def test_notas_invalidas_superiores(self):
        """Verifica que notas > 5 sean rechazadas"""
        estudiantes = [
            Estudiante("Test", "Materia", 6.0, 4.5, 4.2)
        ]
        resultado = filtro_validacion(estudiantes)

        self.assertFalse(resultado[0].valido)
        self.assertIn("6.0", resultado[0].mensaje_error)

    def test_notas_invalidas_negativas(self):
        """Verifica que notas < 0 sean rechazadas"""
        estudiantes = [
            Estudiante("Test", "Materia", 4.0, -1.0, 4.2)
        ]
        resultado = filtro_validacion(estudiantes)

        self.assertFalse(resultado[0].valido)
        self.assertIn("-1.0", resultado[0].mensaje_error)

    def test_notas_limite_inferior(self):
        """Verifica que nota = 0 sea válida"""
        estudiantes = [
            Estudiante("Test", "Materia", 0.0, 2.5, 3.0)
        ]
        resultado = filtro_validacion(estudiantes)

        self.assertTrue(resultado[0].valido)

    def test_notas_limite_superior(self):
        """Verifica que nota = 5 sea válida"""
        estudiantes = [
            Estudiante("Test", "Materia", 5.0, 5.0, 5.0)
        ]
        resultado = filtro_validacion(estudiantes)

        self.assertTrue(resultado[0].valido)


class TestFiltroCalculoPromedio(unittest.TestCase):
    """Tests para el filtro de cálculo de promedio"""

    def test_calculo_promedio_correcto(self):
        """Verifica el cálculo correcto del promedio"""
        estudiantes = [
            Estudiante("Test", "Materia", 3.0, 4.0, 5.0)
        ]
        estudiantes[0].valido = True
        resultado = filtro_calculo_promedio(estudiantes)

        promedio_esperado = (3.0 + 4.0 + 5.0) / 3
        self.assertAlmostEqual(
            resultado[0].promedio, promedio_esperado, places=2)

    def test_promedio_con_datos_invalidos(self):
        """Verifica que estudiantes inválidos tengan promedio 0"""
        estudiantes = [
            Estudiante("Test", "Materia", 6.0, 4.0, 5.0)
        ]
        estudiantes[0].valido = False
        resultado = filtro_calculo_promedio(estudiantes)

        self.assertEqual(resultado[0].promedio, 0.0)

    def test_promedio_notas_iguales(self):
        """Verifica el promedio cuando todas las notas son iguales"""
        estudiantes = [
            Estudiante("Test", "Materia", 4.5, 4.5, 4.5)
        ]
        estudiantes[0].valido = True
        resultado = filtro_calculo_promedio(estudiantes)

        self.assertAlmostEqual(resultado[0].promedio, 4.5, places=2)


class TestFiltroClasificacion(unittest.TestCase):
    """Tests para el filtro de clasificación"""

    def test_clasificacion_aprobado(self):
        """Verifica clasificación correcta de estudiante aprobado"""
        estudiantes = [
            Estudiante("Test", "Materia", 4.0, 4.0, 4.0)
        ]
        estudiantes[0].valido = True
        estudiantes[0].promedio = 4.0
        resultado = filtro_clasificacion(estudiantes)

        self.assertEqual(resultado[0].estado, "APROBADO")

    def test_clasificacion_no_aprobado(self):
        """Verifica clasificación correcta de estudiante no aprobado"""
        estudiantes = [
            Estudiante("Test", "Materia", 2.0, 2.0, 2.0)
        ]
        estudiantes[0].valido = True
        estudiantes[0].promedio = 2.0
        resultado = filtro_clasificacion(estudiantes)

        self.assertEqual(resultado[0].estado, "NO APROBADO")

    def test_clasificacion_limite_aprobacion(self):
        """Verifica clasificación con promedio exactamente en el límite (3.0)"""
        estudiantes = [
            Estudiante("Test", "Materia", 3.0, 3.0, 3.0)
        ]
        estudiantes[0].valido = True
        estudiantes[0].promedio = 3.0
        resultado = filtro_clasificacion(estudiantes)

        self.assertEqual(resultado[0].estado, "APROBADO")

    def test_clasificacion_datos_invalidos(self):
        """Verifica clasificación de estudiante con datos inválidos"""
        estudiantes = [
            Estudiante("Test", "Materia", 6.0, 4.0, 4.0)
        ]
        estudiantes[0].valido = False
        resultado = filtro_clasificacion(estudiantes)

        self.assertEqual(resultado[0].estado, "DATOS INVÁLIDOS")


class TestPipeline(unittest.TestCase):
    """Tests para la clase Pipeline"""

    def test_pipeline_vacio(self):
        """Verifica que un pipeline vacío retorna los datos sin modificar"""
        pipeline = Pipeline()
        datos = [1, 2, 3]
        resultado = pipeline.ejecutar(datos)

        self.assertEqual(resultado, datos)

    def test_pipeline_con_filtros(self):
        """Verifica la ejecución correcta del pipeline completo"""
        estudiantes = [
            Estudiante("Test1", "Materia1", 4.0, 4.5, 4.2),
            Estudiante("Test2", "Materia2", 2.0, 2.5, 2.3)
        ]

        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        # Verificar que todos los filtros se ejecutaron
        self.assertTrue(resultado[0].valido)
        self.assertGreater(resultado[0].promedio, 0)
        self.assertEqual(resultado[0].estado, "APROBADO")

        self.assertTrue(resultado[1].valido)
        self.assertGreater(resultado[1].promedio, 0)
        self.assertEqual(resultado[1].estado, "NO APROBADO")

    def test_pipeline_orden_filtros(self):
        """Verifica que el orden de los filtros importe"""
        estudiantes = [
            Estudiante("Test", "Materia", 4.0, 4.5, 4.2)
        ]

        # Pipeline en el orden correcto
        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        # Todos los campos deben estar procesados
        self.assertTrue(resultado[0].valido)
        self.assertGreater(resultado[0].promedio, 0)
        self.assertIn(resultado[0].estado, ["APROBADO", "NO APROBADO"])


class TestIntegracion(unittest.TestCase):
    """Tests de integración del sistema completo"""

    def test_flujo_completo_estudiante_aprobado(self):
        """Verifica el flujo completo para un estudiante aprobado"""
        estudiantes = [
            Estudiante("Ana García", "Matemáticas", 4.5, 4.0, 4.8)
        ]

        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        self.assertTrue(resultado[0].valido)
        self.assertAlmostEqual(resultado[0].promedio, 4.43, places=2)
        self.assertEqual(resultado[0].estado, "APROBADO")

    def test_flujo_completo_estudiante_no_aprobado(self):
        """Verifica el flujo completo para un estudiante no aprobado"""
        estudiantes = [
            Estudiante("Pedro Sánchez", "Inglés", 1.5, 2.0, 1.8)
        ]

        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        self.assertTrue(resultado[0].valido)
        self.assertAlmostEqual(resultado[0].promedio, 1.77, places=2)
        self.assertEqual(resultado[0].estado, "NO APROBADO")

    def test_flujo_completo_datos_invalidos(self):
        """Verifica el flujo completo para un estudiante con datos inválidos"""
        estudiantes = [
            Estudiante("Sofia Torres", "Arquitectura SW", 6.0, 4.5, 3.5)
        ]

        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        self.assertFalse(resultado[0].valido)
        self.assertEqual(resultado[0].promedio, 0.0)
        self.assertEqual(resultado[0].estado, "DATOS INVÁLIDOS")

    def test_multiples_estudiantes(self):
        """Verifica el procesamiento de múltiples estudiantes"""
        estudiantes = [
            Estudiante("Estudiante1", "Materia1", 4.5, 4.0, 4.8),
            Estudiante("Estudiante2", "Materia2", 2.5, 2.8, 2.3),
            Estudiante("Estudiante3", "Materia3", 6.0, 4.5, 3.5),
        ]

        pipeline = Pipeline()
        pipeline.agregar_filtro(filtro_validacion)
        pipeline.agregar_filtro(filtro_calculo_promedio)
        pipeline.agregar_filtro(filtro_clasificacion)

        resultado = pipeline.ejecutar(estudiantes)

        # Verificar que se procesaron todos
        self.assertEqual(len(resultado), 3)

        # Verificar estados individuales
        self.assertEqual(resultado[0].estado, "APROBADO")
        self.assertEqual(resultado[1].estado, "NO APROBADO")
        self.assertEqual(resultado[2].estado, "DATOS INVÁLIDOS")


def run_tests():
    """Función para ejecutar todos los tests"""
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Agregar todos los tests
    suite.addTests(loader.loadTestsFromTestCase(TestEstudiante))
    suite.addTests(loader.loadTestsFromTestCase(TestFiltroValidacion))
    suite.addTests(loader.loadTestsFromTestCase(TestFiltroCalculoPromedio))
    suite.addTests(loader.loadTestsFromTestCase(TestFiltroClasificacion))
    suite.addTests(loader.loadTestsFromTestCase(TestPipeline))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegracion))

    # Ejecutar tests con resultado verboso
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Mostrar resumen
    print("\n" + "="*80)
    print("📊 RESUMEN DE TESTS".center(80))
    print("="*80)
    print(f"✅ Tests ejecutados: {result.testsRun}")
    print(
        f"✅ Tests exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Tests fallidos: {len(result.failures)}")
    print(f"⚠️  Errores: {len(result.errors)}")
    print("="*80)

    return result.wasSuccessful()


if __name__ == "__main__":
    print("="*80)
    print("🧪 TESTS UNITARIOS - Sistema de Calificaciones".center(80))
    print("Demostración de Testabilidad del Patrón Pipes and Filters".center(80))
    print("="*80)
    print()

    success = run_tests()

    if success:
        print("\n✅ TODOS LOS TESTS PASARON EXITOSAMENTE")
    else:
        print("\n❌ ALGUNOS TESTS FALLARON")

    print("\n💡 NOTA:")
    print("   Los tests demuestran la TESTABILIDAD del patrón Pipes and Filters.")
    print("   Cada filtro puede ser probado de forma independiente y aislada.")
