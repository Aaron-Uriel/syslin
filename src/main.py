import scipy as sci
import numpy as np
import numpy.polynomial.polynomial as poly
import control as ct



def main():
    num = input("Coeficientes del polinomio numerador: ").split();
    den = input("Coeficientes del polinomio denominador: ").split();
    num = list(map(float, num));
    den = list(map(float, den));

    zeros = poly.polyroots(poly.Polynomial(num))
    poles = poly.polyroots(poly.Polynomial(num))

    if (len(den) < len(num)):
        print("Función de transferencia inválida");

    # Función de transferencia.
    trf_fn = ct.tf(num, den)

    print("Los ceros de la función están en: ", zeros, "\n",
          "Los polos de la función están en: ", poles, "\n")


if __name__ == "__main__":
    main()
