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
    sys_tf = ct.tf(num[::-1], den[::-1])
    sys_ss = ct.tf2ss(num[::-1], den[::-1])

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

    print("Información sobre la función de transferencia.")
    print("Función de transferencia:", sys_tf)
    print("Ceros:", zeros)
    print("Polos: ", poles)
    print("Orden del sistema:", len(poles))
    print("Estabilidad del sistema:", stability_status.name)
    if stability_status == Stability.STABLE:
        print("Valor final:", step_value*num[0]/den[0])

    plt.style.use('_mpl-gallery')
    (fig, axd) = plt.subplot_mosaic([['poles', 'response'],
                                     ['input', 'response']],
                                    figsize=(10,5), layout='constrained')
    ax1 = axd['poles']
    ax1.scatter(zeros.real, zeros.imag, marker='o', label='Ceros')
    ax1.scatter(poles.real, poles.imag, marker='x', label='Polos')
    ax1.set_title('Polos y ceros')
    ax1.set_xlabel('Componente real')
    ax1.set_ylabel('Componente imaginario')
    ax1.grid(visible=True)
    ax1.legend()

    # Calcular la respuesta al escalón unitario personalizado manualmente
    t = np.linspace(0, 10, 1000)
    u = step_value * np.ones(t.shape)
    y = ct.forced_response(sys_tf, T=t, U=u)

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
