import numpy as np
import numpy.polynomial.polynomial as poly
import control as ct
import matplotlib.pyplot as plt

def main():
    num = input("Coeficientes del polinomio numerador: ").split();
    den = input("Coeficientes del polinomio denominador: ").split();
    num = list(map(float, num));
    den = list(map(float, den));

    zeros = poly.polyroots(num)
    poles = poly.polyroots(den)

    if (len(den) < len(num)):
        print("Función de transferencia inválida");

    # Función de transferencia.
    trf_fn = ct.tf(num, den)

    print("Los ceros de la función están en: ", zeros)
    print("Los polos de la función están en: ", poles)

    plt.style.use('_mpl-gallery')

    fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
    ax.scatter(zeros.real, zeros.imag, marker='x', label='Ceros')
    ax.scatter(poles.real, poles.imag, marker='o', label='Polos')
    ax.set_title('Polos y ceros')
    ax.set_xlabel('$Re(z)$')
    ax.set_ylabel('$Im(z)$')
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()
