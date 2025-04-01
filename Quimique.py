import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd

def balance_combustion(carbonos, hidrogenos):
    """ Balancea la ecuación de combustión de un hidrocarburo """
    O2 = sp.Symbol("O2")
    CO2 = sp.Symbol("CO2")
    H2O = sp.Symbol("H2O")
    ecuacion = sp.Eq(carbonos * CO2 + (hidrogenos / 2) * H2O, O2 * 2)
    solucion = sp.solve(ecuacion, O2)
    return f"C{carbonos}H{hidrogenos} + {solucion[0]} O2 -> {carbonos} CO2 + {hidrogenos / 2} H2O"

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
