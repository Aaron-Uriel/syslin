# Syslin.
Simulación de sistemas de control lineales hecho de forma sencilla con Python.
Programa hecho para el curso de Control Analógico I 2023-2024 de la Facultad
de Ingeniería Eléctrica.

## Objetivos del el producto final.
Los objetivos estarán determinandose conforme avance el curso de control, por
lo que se incluye todo lo que se ha determinado como requisito para el 
proyecto hasta ahora.
### Objetivos necesarios.
- Interfaz gráfica que permita interactuar con el programa.
- Recibir una descripción de la planta. Que puede ser dada en:
    - Matrices de funciones de transferencia.
- Definir el tipo de sistema al que se le calculará la respuesta.
Como opciones tenemos (las opciones son combinables):
    - Sistemas retroalimentados.
    - Sistemas con controlador. El controlador es por ahora un amplificador.
- Definir condiciones iniciales.
- Definir función de entrada. Funciones de entrada contempladas:
    - Escalones con amplitud y duración arbitrarios.
- Diagnóstico de la respuesta obtenida, que incluirá:
    - Valor final en caso de ser estable.
    - Tiempo que tomará en estabilizarse en caso de ser estable.
    - Valor máximo en caso de presentar sobrepulso con polos imaginarios.
- Gráficas interactivas que muestren:
     - La respuesta a través del tiempo. Mostrando el valor final en pantalla,
     en caso de haberlo
     - Función de entrada.
     - Ceros y polos. Mostrando sus valores de forma fácil de ver.
### Objetivos secundarios.
- Configurar parámetros para la gráfica de la respuesta, como son:
    - Intervalo.
    - Cantidad de muestras.

# Detallando en el diseño.
El programa se mostrará en una sola ventana pero habrá secciones en donde se
podrá ingresar/ver cierta información.
Sección gráfica:
- Respuesta. Muestra las gráficas de la función de entrada y la respuesta.
- Polos. Solo muestra los polos
Sección de parámetros:
- Descripción. Se muestra una matriz de transferencia y la matriz de funciones
de entrada en la cual se especificarán sus valores. Presionar un elemento de
la matriz permitirá modificar su valor. Para funciones de entrada se mostrará
la posibilidad de escoger entre un 
- Condiciones iniciales. Aquí se pueden definir los valores iniciales para el
sistema.
Sección de diagnóstico:
- Información del sistema calculado. Muestra información numérica clave del
sistema después de ser calculado.
- Información del sistema antes de ser calculado. Muestra que información es
la que se tomará antes de calcular.

## Bibliotecas.
- [matplotlib](https://matplotlib.org/): para realizar gráficas.
- [NumPy](https://numpy.org/): cálculos númericos y simbolicos básicos.
- [control](https://python-control.readthedocs.io/en/0.9.4/): simulación de
    sistemas de control.
- [SciPy](https://scipy.org/): cálculos numéricos avanzados.
- [PyGObject](https://pygobject.readthedocs.io/en/latest/): posible candidato
    para hacer una interface avanzada que no requiera la terminal.

## Metas
### Metas para primera iteración.
El objetivo de la primera iteración es crear un programa que pueda determinar
si una función de transferencia es estable o no, y graficar los polos obtenidos.
Para ello se proponen los siguientes subproblemas a resolver:
- [x] Lectura de los datos desde la terminal.
- [x] Obtener los ceros y los polos. Estos números pueden ser complejos, por
lo que se tiene que tomar en cuenta al obtener las raices de los polinomios.
    - [x] Definir si se trata de un sistema: estable, al borde de la 
    inestabilidad o inestable.
- [x] Obtener funcion de transferencia. Uso de la biblioteca control.
- [x] Graficar los polos en su respectiva gráfica. Esto implica el uso de la
    biblioteca matplotlib.
### Metas para segunda iteración.
Se busca la ampliación del programa con mayor funcionalidad y modularización
del código.
Metas:
- [ ] Hacer una interfaz gráfica (Aaron).
- [ ] Implementar las formas de la entrada:
    - [x] Escalón unitario.
    - [ ] Escalón con múltiples intervalos (Brandon).
    - [ ] Pulso.
- [ ] Encontrar la forma de determinar el valor final del sistema.
    - Ya la sabemos para el escalón unitario.
    - Escalón con múltiples intervalos no la ocupa.
    - Un pulso termina en 0 (la mayoría de las veces).
- [x] Especificar el valor del escalón unitario y ponerlo como entrada a la 
    función de transferencia (Brandon).
- [x] Indicar el valor máximo y porcentage del sobrepulso de la función en 
    caso de que los polos tengan componentes imaginarios (Jorge).
- [ ] Recibir y calcular la respuesta al escalón para sistemas MIMO.
    - [ ] El programa tiene que ser capaz de pedirlo desde la terminal.
    - [ ] Implementarlo en la interfaz también.
- [ ] Recibir condiciones iniciales (Jorge).
- [ ] Determinar respuesta con un sistema retroalimentado (Aaron).
- [ ] Determinar respuesta con un controlador (Aaron).
- [x] Incluir gráfica de la función de entrada (Aaron).
- [x] Asegurarse que la gráfica incluya todo el intervalo para funciones que son
    estables (Aaron).
    - [x] ~Obtener constantes de tiempo e imprimirlas~. No es necesario porque
    los polos ya nos indican las constantes de tiempo.

## Organización del código.
El código tendrá separación entre lo que procesa el sistema y lo que maneja
la interface gráfica.
- `main.py` archivo principal del programa, cargará la interface de Qt.
- `cli.py` incluirá el manejo de la aplicación por terminal.
- `syslin.py` tendrá toda la lógica para procesar los sitemas de control.
