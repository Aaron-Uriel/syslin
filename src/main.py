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
    num = input("Coeficientes del polinomio numerador: ")
    den = input("Coeficientes del polinomio denominador: ")
    num = list(map(float, num.split()))
    den = list(map(float, den.split()))

    # Solicitar al usuario el valor del escalón unitario
    step_value = float(input("Ingrese el valor del escalón unitario: "))

    # Función de transferencia.
    sys_tf = ct.tf(num, den)
    sys_ss = ct.tf2ss(num, den)

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

    # Calcular la respuesta al escalón unitario personalizado manualmente
    t = np.linspace(0, 10, 1000)
    u = step_value * np.ones(t.shape)
    y = ct.forced_response(sys_tf, T=t, U=u)

    print("Información sobre la función de transferencia.")
    print("Función de transferencia:", sys_tf)
    print("Ceros:", zeros)
    print("Polos: ", poles)
    print("Orden del sistema:", len(poles))
    print("Estabilidad del sistema:", stability_status.name)
    print('Valor máximo de la función:', np.max(y[1]))
    if stability_status == Stability.STABLE:
        print("Valor final:", step_value*num[len(num)-1]/den[len(den)-1])

    plt.style.use('_mpl-gallery')
    (fig, poles_axes) = plt.subplots(figsize=(5, 5), layout='constrained')
    poles_axes.scatter(zeros.real, zeros.imag, marker='o', label='Ceros')
    poles_axes.scatter(poles.real, poles.imag, marker='x', label='Polos')
    poles_axes.set_title('Polos y ceros')
    poles_axes.set_xlabel('Componente real')
    poles_axes.set_ylabel('Componente imaginario')
    poles_axes.grid(visible=True)
    poles_axes.legend()

    (fig, axd) = plt.subplot_mosaic([['response'], ['input']],
                                    figsize=(5,6), layout='constrained')

    ax2 = axd['response']
    ax2.plot(t, y[1], label='$y(t)$')
    ax2.set_title('Respuesta escalón unitario')
    ax2.set_ylabel('Magnitud')
    ax2.set_xlabel('Tiempo')
    ax2.grid(visible=True)
    ax2.legend()

    ax3 = axd['input']
    ax3.plot(t, u, label='$u(t)$')
    ax3.set_title('Señal de entrada.')
    ax3.set_ylabel('Magnitud')
    ax3.set_xlabel('Tiempo')
    ax3.grid(visible=True)
    ax3.legend()

    plt.show()

if __name__ == "__main__":
    main()
