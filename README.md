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
   * Significa que la prueba falló, demostrando que la funcionalidad deseada aún no existe o no se comporta como se espera.

2. **¿Qué debe hacerse para llegar a VERDE?**
   * Escribir la cantidad mínima necesaria de código en la función para que la prueba pase.

3. **¿Qué diferencia existe entre agregar funcionalidad y refactorizar?**
   * **Agregar funcionalidad** añade nuevos comportamientos (y requiere nuevas pruebas en rojo). **Refactorizar** mejora la estructura o legibilidad del código sin alterar su comportamiento observable (las pruebas deben seguir en verde).

4. **¿Por qué en TDD no conviene implementar todos los requisitos desde el inicio?**
   * <p align="justify">En TDD no conviene implementar todos los requisitos desde el inicio porque trabajar en pasos pequeños permite detectar errores al instante y asegurar que las pruebas guíen el diseño del programa. Escribir todo el código de golpe dificulta identificar qué causó una falla y rompe el ciclo incremental de desarrollo.   
</p>

---

## Durante el desarrollo

1. **¿Qué prueba escribiste?**
   * **Ciclo 1:** `test_envio_estandar_hasta_5kg` y `test_envio_estandar_exactamente_5kg`.
   * **Ciclo 2:** `test_envio_estandar_mas_de_5kg`.
   * **Ciclo 3:** `test_envio_express_hasta_5kg` y `test_envio_express_mas_de_5kg`.
   * **Ciclo 4:** `test_peso_cero_lanza_error` y `test_peso_negativo_lanza_error`.
   * **Ciclo 5:** `test_tipo_envio_invalido_lanza_error`.

2. **¿Por qué falló inicialmente?**
   * **Ciclo 1:** La función `calcular_envio` no existía en el módulo.
   * **Ciclo 2:** La función regresaba un costo fijo de 50 y no calculaba el cobro por los kilogramos excedentes.
   * **Ciclo 3:** No existía la lógica para duplicar el costo base cuando el tipo de servicio era `express`.
   * **Ciclo 4:** No se validaba el rango del peso, procesando valores menores o iguales a cero como válidos.
   * **Ciclo 5:** La función no validaba la cadena del tipo de envío, aceptando cualquier valor no reconocido.

3. **¿Qué cambio mínimo hiciste?**
   * **Ciclo 1:** Se creó la función `calcular_envio` regresando el valor constante `50`.
   * **Ciclo 2:** Se agregó la condición `if peso > 5:` para calcular y sumar $10 por cada kilogramo de exceso.
   * **Ciclo 3:** Se añadió la instrucción `if tipo_envio == "express":` para multiplicar el costo resultante por 2.
   * **Ciclo 4:** Se colocó al inicio la validación `if peso <= 0: raise ValueError(...)`.
   * **Ciclo 5:** Se agregó la validación `if tipo_envio not in ["estandar", "express"]: raise ValueError(...)`.

4. **¿Todas las pruebas anteriores continuaron pasando?**
   * Sí, en cada iteración se ejecutó `pytest` comprobando que las pruebas previas se mantenían en **VERDE** junto a la nueva prueba agregada. Esto se pruede corroborar en el archivo adjunto `evidencia-pruebas.pdf`, en el cual se observan las capturas de pantalla de cada prueba realizada y cada falla.

5. **¿Realizaste alguna refactorización?**
   * Sí, tras completar todos los ciclos se extrajeron los valores numéricos fijos a constantes globales (`COSTO_BASE = 50`, `PESO_LIMITE = 5`, `COSTO_EXCESO_POR_KG = 10`) para mejorar la mantenibilidad y legibilidad del código sin alterar su comportamiento esperado.

---

### Registro de ciclos

| Ciclo | Prueba agregada | Cambio realizado | Resultado |
| :---: | :--- | :--- | :---: |
| **1** | `test_envio_estandar_hasta_5kg` y `test_envio_estandar_exactamente_5kg` | Se creó la función `calcular_envio` retornando `50`. | VERDE |
| **2** | `test_envio_estandar_mas_de_5kg` | Se añadió el cobro de $10 por kg adicional si `peso > 5`. | VERDE |
| **3** | `test_envio_express_hasta_5kg` y `test_envio_express_mas_de_5kg` | Se implementó el multiplicador `* 2` para servicio `"express"`. | VERDE |
| **4** | `test_peso_cero_lanza_error` y `test_peso_negativo_lanza_error` | Se agregó validación para lanzar `ValueError` si `peso <= 0`. | VERDE |
| **5** | `test_tipo_envio_invalido_lanza_error` | Se agregó validación para lanzar `ValueError` si el servicio no es válido. | VERDE |

---

## Reflexión final

1. **¿En qué momento una prueba te obligó a modificar el diseño?**
   * <p align="justify">Al agregar los casos de error (pesos y tipos de envío inválidos), la función tuvo que reorganizarse para verificar y rechazar los datos incorrectos al principio. Esto cambió el flujo del programa, asegurando que ningún cálculo se realizara con entradas no válidas.
</p>

2. **¿Qué ventaja encontraste al ejecutar todas las pruebas después de cada cambio?**
   * <p align="justify">Nos dió la seguridad constante de que cada nueva regla agregada o cada cambio de refactorización no alteró el código que ya funcionaba correctamente. Al ejecutar la totalidad de las pruebas tras cada modificación, se pudo confirmar de inmediato que el comportamiento previo se mantenía intacto.
</p>

3. **¿Qué parte del proceso TDD te resultó más difícil?**
   * <p align="justify">Resistir la tentación de programar toda la lógica desde el principio y limitarnos a escribir solo el código mínimo para hacer pasar cada prueba individual.
</p>

---

## Instrucciones para ejecutar el programa

- Clonar el repositorio remoto e ingresar a la carpeta del proyecto: 
  
  `git clone https://github.com/valeriagh-star/Practica-5.git`

  `cd Practica-5` 

- Crear un entorno virtual e instalar las dependencias necesarias:

  `python3 -m venv venv`

  `source venv/bin/activate`

  `pip install pytest`

- Ejecutar las pruebas unitarias:

  `pytest`

- Se puede ejecutar `pytest -v` para ver un reporte detallado del resultado de cada prueba unitaria realizada.