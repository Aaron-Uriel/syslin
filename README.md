# Simulación de sistemas lineales en Python
Programa hecho en Python para simular sistemas de control continuo para la
materia Control Analógico I.

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
- [x] Obtener los ceros y los polos. Estos números pueden ser complejos, por lo
    que se tiene que tomar en cuenta al obtener las raices de los polinomios.
    - [x] Definir si se trata de un sistema: estable, al borde de la inestabilidad o inestable.
- [x] Obtener funcion de transferencia. Uso de la biblioteca control.
- [x] Graficar los polos en su respectiva gráfica. Esto implica el uso de la
    biblioteca matplotlib.
### Metas finales.
Como objetivos finales tenemos:
- [ ] Recibir sistema de ODEs que definan a un sistema de control.
- [ ] Recibir condiciones iniciales.
- [ ] Aplicar transformada de Laplace para resolver como parte de la resolución
      del sistema.
- [ ] Obtener funciones de transferencia.
- [ ] Determinar si es un sistema estable, críticamente estable o inestable.
- [ ] Aplicar transformada inversa de Laplace para obtener la solución.
- [ ] Graficar las mismas ecuaciones diferenciales.
Extra:
- [ ] Interface gráfica para meter los datos.

