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

    estado = "estable"
    for i in poles:
        if i.real == 0:
            estado = "críticamente estable"
        elif i.real > 0:
            estado = "inestable"
            break

    if (len(poles) < len(zeros)):
        print("Función de transferencia inválida");
        return 1

    # Función de transferencia.
    trf = ct.tf(num, den)
    (t, y) = ct.step_response(trf)
    print("Función de transferencia recibida:")
    print(trf)
    print("El orden de la función de transferencia es:", len(poles))
    print("Los ceros de la función están en: ", zeros)
    print("Los polos de la función están en: ", poles)
    print("El estado del sistema es:", estado)

    plt.style.use('_mpl-gallery')
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                                   figsize=(10, 5), layout='compressed')
    ax1.scatter(zeros.real, zeros.imag, marker='o', label='Ceros')
    ax1.scatter(poles.real, poles.imag, marker='x', label='Polos')
    ax1.set_title('Polos y ceros')
    ax1.set_xlabel('Componente real')
    ax1.set_ylabel('Componente imaginario')
    ax1.legend()

    ax2.plot(t, y)
    ax2.set_title('Respuesta escalón unitario')
    ax2.set_ylabel('Magnitud')
    ax2.set_xlabel('Tiempo')

    plt.show()

if __name__ == "__main__":
    main()
