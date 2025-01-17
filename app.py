import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Financiera"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Función y logica para calcular interés compuesto
    def calcular_interes_compuesto(e):
        principal = float(principal_input.value)
        tasa_interes = float(tasa_input.value) / 100
        tiempo = float(tiempo_input.value)
        monto_total = principal * (1 + tasa_interes) ** tiempo
        interes_generado = monto_total - principal
        resultado_text.value = f"Monto total: ${monto_total:.2f}\nInterés generado: ${interes_generado:.2f}"
        historial.append(resultado_text.value)
        page.update()

    # Función y logica  para calcular cuota mensual (EMI)
    def calcular_emi(e):
        principal = float(principal_input.value)
        tasa_interes = float(tasa_input.value) / 1200  # Tasa mensual
        tiempo = float(tiempo_input.value) * 12  # Meses
        emi = (principal * tasa_interes * (1 + tasa_interes) ** tiempo) / ((1 + tasa_interes) ** tiempo - 1)
        resultado_text.value = f"Cuota mensual (EMI): ${emi:.2f}"
        historial.append(resultado_text.value)
        page.update()

    # Función y logica  para cambiar entre modo claro y oscuro
    def cambiar_tema(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    # Función y logica  para mostrar historial
    def mostrar_historial(e):
        historial_text.value = "\n".join(historial)
        page.update()

    # Campos de entrada
    principal_input = ft.TextField(label="Monto Principal", width=200)
    tasa_input = ft.TextField(label="Tasa de Interés (%)", width=200)
    tiempo_input = ft.TextField(label="Tiempo (años)", width=200)

    # logica de los Botones para calcular y cambiar tema
    calcular_interes_button = ft.ElevatedButton(text="Calcular Interés Compuesto", on_click=calcular_interes_compuesto)
    calcular_emi_button = ft.ElevatedButton(text="Calcular EMI", on_click=calcular_emi)
    cambiar_tema_button = ft.ElevatedButton(text="Cambiar Tema", on_click=cambiar_tema)
    mostrar_historial_button = ft.ElevatedButton(text="Mostrar Historial", on_click=mostrar_historial)

    # Campo de resultado y historial
    resultado_text = ft.Text(value="", size=20)
    historial_text = ft.Text(value="", size=20)
    historial = []

    # Agregar componentes a la página
    page.add(
        ft.Column(
            [
                ft.Text("Calculadora Financiera", size=30, weight=ft.FontWeight.BOLD),
                principal_input,
                tasa_input,
                tiempo_input,
                calcular_interes_button,
                calcular_emi_button,
                cambiar_tema_button,
                mostrar_historial_button,
                resultado_text,
                historial_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
