import streamlit as st
import sympy as sp

def balance_combustion(formula):
    """ Balancea la ecuación de combustión de un hidrocarburo """
    carbonos, hidrogenos = formula
    oxigenos_reactivos = sp.Symbol("O2")
    ecuacion = sp.Eq(carbonos * sp.Symbol("CO2") + (hidrogenos / 2) * sp.Symbol("H2O"), oxigenos_reactivos * 2)
    solucion = sp.solve(ecuacion, oxigenos_reactivos)
    
    return f"C{carbonos}H{hidrogenos} + {solucion[0]} O2 -> {carbonos} CO2 + {hidrogenos / 2} H2O"

def main():
    st.title("Balanceador de Combustión de Hidrocarburos")
    tipo = st.selectbox("Selecciona el tipo de hidrocarburo", ["Alcano", "Alqueno", "Alquino"])
    carbonos = st.number_input("Número de carbonos", min_value=1, step=1)
    
    if tipo == "Alcano":
        formula = (carbonos, carbonos * 2 + 2)
    elif tipo == "Alqueno":
        formula = (carbonos, carbonos * 2)
    elif tipo == "Alquino":
        formula = (carbonos, carbonos * 2 - 2)
    
    if st.button("Balancear Ecuación"):
        ecuacion_balanceada = balance_combustion(formula)
        st.write("Ecuación balanceada:")
        st.latex(ecuacion_balanceada)

if __name__ == "__main__":
    main()
