#Variables Calcular salario con descuento
Días = int(input("Ingresa los Días trabajados: "))
Pago = float(input("ingresa el pago por Días trabajados: "))
Despension = Días * Pago * 0.10
Dessalud = Días * Pago * 0.15
SalMensual = Días * Pago - Despension - Dessalud
print("El salario Mensual es: $",round(SalMensual,1))
