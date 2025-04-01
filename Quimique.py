import streamlit as st
import numpy as np
import pandas as pd

def balance_combustion(carbonos, hidrogenos):
    """ Balancea la ecuación de combustión de un hidrocarburo sin usar sympy """
    oxigenos_reactivos = (carbonos * 2 + hidrogenos / 2)
    return f"C{carbonos}H{hidrogenos} + {oxigenos_reactivos/2} O2 -> {carbonos} CO2 + {hidrogenos / 2} H2O"

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
