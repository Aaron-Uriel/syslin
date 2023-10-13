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
    num = input("Coeficientes del polinomio numerador: ");
    den = input("Coeficientes del polinomio denominador: ");
    num = list(map(float, num.split()));
    den = list(map(float, den.split()));

    # Función de transferencia.
    sys_tf = ct.tf(num[::-1], den[::-1])
    sys_ss = ct.tf2ss(num[::-1], den[::-1])

    zeros = sys_ss.zeros()
    poles = sys_ss.poles()

    if (len(poles) < len(zeros)):
        print("Función de transferencia inválida");
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

    plt.style.use('_mpl-gallery')
    #plt.style.use('grayscale')
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                                   figsize=(10, 5), layout='compressed')
    ax1.scatter(zeros.real, zeros.imag, marker='o', label='Ceros')
    ax1.scatter(poles.real, poles.imag, marker='x', label='Polos')
    ax1.set_title('Polos y ceros')
    ax1.set_xlabel('Componente real')
    ax1.set_ylabel('Componente imaginario')
    ax1.grid(visible=True)
    ax1.legend()

    response = ct.step_response(sys_tf)
    ax2.plot(response.time, response.outputs, label='$y(t)$')
    ax2.set_title('Respuesta escalón unitario')
    ax2.set_ylabel('Magnitud')
    ax2.set_xlabel('Tiempo')
    ax2.grid(visible=True)
    ax2.legend()

    plt.show()

if __name__ == "__main__":
    main()
