import sympy as sp

def balance_combustion(formula):
    """ Balancea la ecuación de combustión de alcanos, alquenos y alquinos """
    carbonos = int(formula[1:]) if len(formula) > 1 else 1
    hidrogenos = carbonos * 2 + 2 if "ane" in formula else (carbonos * 2 if "ene" in formula else carbonos * 2 - 2)
    oxigenos_reactivos = sp.Symbol("O2")
    oxigenos_productos = sp.Symbol("CO2") + (sp.Symbol("H2O") / 2)
    
    ecuacion = sp.Eq(carbonos * oxigenos_productos + (hidrogenos / 2) * sp.Symbol("H2O"), oxigenos_reactivos * 2)
    solucion = sp.solve(ecuacion, oxigenos_reactivos)
    
    return f"C{carbonos}H{hidrogenos} + {solucion[0]} O2 -> {carbonos} CO2 + {hidrogenos / 2} H2O"

def main():
    while True:
        tipo = input("Introduce el tipo de hidrocarburo (alcano, alqueno, alquino): ").strip().lower()
        carbonos = int(input("Introduce el número de carbonos: "))
        
        if tipo == "alcano":
            formula = f"C{carbonos}H{carbonos * 2 + 2}"
        elif tipo == "alqueno":
            formula = f"C{carbonos}H{carbonos * 2}"
        elif tipo == "alquino":
            formula = f"C{carbonos}H{carbonos * 2 - 2}"
        else:
            print("Tipo no válido")
            continue
        
        print("Ecuación balanceada:")
        print(balance_combustion(formula))
        
        again = input("¿Quieres otra ecuación? (s/n): ").strip().lower()
        if again != 's':
            break

if __name__ == "__main__":
    main()
