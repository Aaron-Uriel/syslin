import numpy as np
import numpy.polynomial.polynomial as poly
import control as ct
import matplotlib.pyplot as plt
from enum import Enum

class Stability(Enum):
    STABLE = 0
    CRITICALLY_STABLE = 1
    UNSTABLE = 2

def main():
    # Lectura de datos
    (num, den, step_value) = (None, None, None)
    while True:
        try:
            num = input("Coeficientes del polinomio numerador: ")
            num = list([float(x) for x in num.split()])
            den = input("Coeficientes del polinomio denominador: ")
            den = list([float(x) for x in den.split()])

            # Solicitar al usuario el valor del escalón unitario
            step_value = float(input("Ingrese el valor del escalón unitario: "))
        except ValueError:
            print("Error al intentar leer una cadena como números.")
            print("Intente de nuevo...")
            continue
        break

    # Función de transferencia y del espacio de estado.
    sys_tf = ct.tf(num, den)
    sys_ss = ct.tf2ss(num, den)

    # Determinación de valores para imprimir.
    zeros = sys_ss.zeros()
    poles = sys_ss.poles()
    if (len(poles) < len(zeros)):
        print("Función de transferencia inválida")
        return 1
    stability_status = Stability.STABLE
    for i in poles:
        if i.real == 0:
            stability_status = Stability.CRITICALLY_STABLE
        elif i.real > 0:
            stability_status = Stability.UNSTABLE
            break
    (stabilize_time, final_value) = (None, None)
    if stability_status == Stability.STABLE:
        stabilize_time = np.abs(5/np.max(poles.real)) # Hasta e^(-5); error < 0.01
        final_value = step_value*num[-1]/den[-1]

    # Determinar del intervalo de tiempo y de la respuesta del sistema.
    time = 1.1*stabilize_time if stabilize_time else 100
    time = np.linspace(0, time, 1000)
    u = step_value * np.ones(time.shape)
    y = ct.forced_response(sys_tf, T=time, U=u)
    # Determinación del sobrepulso, si hay.
    overpulse = np.max(y[1]) if np.any(poles.imag) else None

    # Impresión de datos.
    print("Información sobre la función de transferencia.")
    print("Función de transferencia:", sys_tf)
    print("Ceros:", zeros)
    print("Polos: ", poles)
    print("Orden del sistema:", len(poles))
    print("Estabilidad del sistema:", stability_status.name)
    if overpulse:
        print("Sobrepulso:", overpulse)
    if stability_status == Stability.STABLE:
        print("Tiempo de estabilización: ", stabilize_time)
        print("Valor final:", final_value)

    # Creación de gráficas.
    plt.style.use('_mpl-gallery')
    (fig, poles_axes) = plt.subplots(figsize=(6,5), layout='constrained')
    poles_axes.scatter(zeros.real, zeros.imag, marker='o', label='Ceros')
    poles_axes.scatter(poles.real, poles.imag, marker='x', label='Polos')
    poles_axes.set_title('Polos y ceros')
    poles_axes.set_xlabel('Componente real')
    poles_axes.set_ylabel('Componente imaginario')
    poles_axes.grid(visible=True)
    poles_axes.legend()

    (fig, axd) = plt.subplot_mosaic([['response'], ['input']],
                                    figsize=(6,6), layout='constrained')

    ax2 = axd['response']
    ax2.plot(time, y[1], label='$y(t)$')
    ax2.set_title('Respuesta escalón unitario')
    ax2.set_ylabel('Magnitud')
    ax2.set_xlabel('Tiempo')
    ax2.grid(visible=True)
    ax2.legend()

    ax3 = axd['input']
    ax3.plot(time, u, "r-", label='$u(t)$')
    ax3.set_title('Señal de entrada.')
    ax3.set_ylabel('Magnitud')
    ax3.set_xlabel('Tiempo')
    ax3.grid(visible=True)
    ax3.legend()

    plt.show()

if __name__ == "__main__":
    main()
