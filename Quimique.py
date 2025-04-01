import streamlit as st
import numpy as np
import pandas as pd

def balance_combustion(carbonos, hidrogenos):
    """ Balancea la ecuación de combustión de un hidrocarburo sin usar sympy """
    oxigenos_reactivos = (carbonos * 2 + hidrogenos / 2)
    
    # Asegurar que todos los coeficientes sean enteros
    factor = 2 if oxigenos_reactivos % 2 != 0 else 1

    return f"{factor}C_{carbonos}H_{hidrogenos} + {int(oxigenos_reactivos * factor / 2)} O_2 \\rightarrow {carbonos * factor} CO_2 + {int(hidrogenos * factor / 2)} H_2O"

def main():
    st.title("Balanceador de Combustión de Hidrocarburos")
    tipo = st.selectbox("Selecciona el tipo de hidrocarburo", ["Alcano", "Alqueno", "Alquino"])
    carbonos = st.number_input("Número de carbonos", min_value=1, step=1)
    
    if tipo == "Alcano":
        hidrogenos = carbonos * 2 + 2
    elif tipo == "Alqueno":
        hidrogenos = carbonos * 2
    elif tipo == "Alquino":
        hidrogenos = carbonos * 2 - 2
    
    if st.button("Balancear Ecuación"):
        ecuacion_balanceada = balance_combustion(carbonos, hidrogenos)
        st.write("Ecuación balanceada:")
        st.latex(ecuacion_balanceada)

if __name__ == "__main__":
    main()

