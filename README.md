# Práctica 5

## Desarrollo de una funcionalidad siguiendo TDD (Test-Driven Development)

> ### Integrantes del Equipo:
> * García Herrera Valeria
> * Grajeda Palacios Dulce Abril
> * Pérez Megchun Pablo de Jesús

> ### Breve descripción de la práctica:
><p align="justify">
> El objetivo principal fue construir una función encargada de calcular el costo de envío de un paquete según el peso del paquete en kilogramos y el tipo de envío, utilizando TDD para guiar cada decisión de diseño. En lugar de implementar todos los requisitos desde el inicio, el sistema se construyó paso a paso en cinco ciclos principales: manejo de tarifas estándar, cobro por exceso de peso, multiplicador por servicio exprés y validación de excepciones ante entradas inválidas (peso menor o igual a cero y tipos de envío no reconocidos). Todo el proceso quedó respaldado por un historial de pruebas y commits incrementales que demuestran la evolución de la solución.   
></p>

---

## Antes de programar

1. **¿Qué significa que una prueba esté en estado ROJO?**
  - Significa que la prueba falló, demostrando que la funcionalidad deseada aún no existe o no se comporta como se espera.

2. **¿Qué debe hacerse para llegar a VERDE?**
  - Escribir la cantidad mínima necesaria de código en la función para que la prueba pase.

3. **¿Qué diferencia existe entre agregar funcionalidad y refactorizar?**
  - **Agregar funcionalidad** añade nuevos comportamientos (y requiere nuevas pruebas en rojo). **Refactorizar** mejora la estructura o legibilidad del código sin alterar su comportamiento observable (las pruebas deben seguir en verde).

4. **¿Por qué en TDD no conviene implementar todos los requisitos desde el inicio?**
  - En TDD no conviene implementar todos los requisitos desde el inicio porque trabajar en pasos pequeños permite detectar errores al instante y asegurar que las pruebas guíen el diseño del programa. Escribir todo el código de golpe dificulta identificar qué causó una falla y rompe el ciclo incremental de desarrollo.   