# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Programa principal
def main():
    # Primera llamada a la función con el valor predeterminado del descuento (10%)
    monto_compra_1 = 100  # Ejemplo de monto total de la compra
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1
    print(f"Monto total: ${monto_compra_1:.2f}")
    print(f"Descuento aplicado: ${descuento_1:.2f}")
    print(f"Monto final a pagar: ${monto_final_1:.2f}")
    print("-" * 30)

    # Segunda llamada a la función con un porcentaje de descuento diferente
    monto_compra_2 = 200  # Ejemplo de monto total de la compra
    porcentaje_descuento_2 = 15  # Descuento del 15%
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    monto_final_2 = monto_compra_2 - descuento_2
    print(f"Monto total: ${monto_compra_2:.2f}")
    print(f"Descuento aplicado: ${descuento_2:.2f}")
    print(f"Monto final a pagar: ${monto_final_2:.2f}")

# Ejecuta el programa
if __name__ == "__main__":
    main()
