"""
Sistema de E-commerce - Menú Principal
Gestión de catálogo y carrito de compras
"""

from modulos.catalogo import catalogo_productos
from modulos.mostrar_catalogo import mostrar_catalogo
from modulos.buscar_producto import buscar_producto
from modulos.carrito import (
    carrito,
    agregar_al_carrito,
    ver_carrito,
    vaciar_carrito,
    eliminar_del_carrito,
    finalizar_compra
)
from modulos.utils import limpiar_pantalla, pausar, validar_opcion


def mostrar_menu_principal():
    """
    Muestra el menú principal del e-commerce
    """
    print("""
    ╔════════════════════════════════════════╗
    ║    BIENVENIDO/A A TU E-COMMERCE        ║
    ╚════════════════════════════════════════╝
    
    📦 CATÁLOGO
    ───────────────────────────────────────
    [1] Ver catálogo completo de productos
    [2] Buscar producto (nombre/categoría)
    
    🛒 CARRITO DE COMPRAS
    ───────────────────────────────────────
    [3] Agregar producto al carrito
    [4] Ver carrito y total
    [5] Eliminar producto del carrito
    [6] Vaciar carrito completo
    [7] Finalizar compra
    
    🚪 SALIR
    ───────────────────────────────────────
    [0] Salir del sistema
    
    """)


def ejecutar_opcion_1():
    """Ver catálogo completo"""
    limpiar_pantalla()
    print("📦 CATÁLOGO DE PRODUCTOS\n")
    mostrar_catalogo(catalogo_productos)
    pausar()


def ejecutar_opcion_2():
    """Buscar producto"""
    limpiar_pantalla()
    print("🔍 BUSCAR PRODUCTO\n")
    print("Opciones de búsqueda:")
    print("  [1] Por nombre")
    print("  [2] Por categoría")
    
    tipo_busqueda = validar_opcion(
        "Selecciona tipo de búsqueda: ",
        opciones_validas=["1", "2"]
    )
    
    if tipo_busqueda == "1":
        buscar_producto("nombre", catalogo_productos)
    elif tipo_busqueda == "2":
        buscar_producto("categoria", catalogo_productos)
    
    pausar()


def ejecutar_opcion_3():
    """Agregar al carrito"""
    limpiar_pantalla()
    print("➕ AGREGAR AL CARRITO\n")
    mostrar_catalogo(catalogo_productos)
    print()
    agregar_al_carrito(catalogo_productos, carrito)
    pausar()


def ejecutar_opcion_4():
    """Ver carrito"""
    limpiar_pantalla()
    print("🛒 TU CARRITO DE COMPRAS\n")
    ver_carrito(carrito)
    pausar()


def ejecutar_opcion_5():
    """Eliminar del carrito"""
    limpiar_pantalla()
    print("🗑️ ELIMINAR PRODUCTO DEL CARRITO\n")
    
    if len(carrito) == 0:
        print("⚠️  Tu carrito está vacío. No hay productos para eliminar.\n")
    else:
        ver_carrito(carrito)
        print()
        eliminar_del_carrito(carrito)
    
    pausar()


def ejecutar_opcion_6():
    """Vaciar carrito"""
    limpiar_pantalla()
    print("🗑️ VACIAR CARRITO COMPLETO\n")
    
    if len(carrito) == 0:
        print("⚠️  Tu carrito ya está vacío.\n")
    else:
        ver_carrito(carrito)
        print()
        confirmar = validar_opcion(
            "⚠️  ¿Estás seguro de vaciar TODO el carrito? (s/n): ",
            opciones_validas=["s", "n", "S", "N"]
        )
        
        if confirmar.lower() == 's':
            vaciar_carrito(carrito)
            print("✅ Carrito vaciado correctamente.\n")
        else:
            print("❌ Operación cancelada.\n")
    
    pausar()


def ejecutar_opcion_7():
    """Finalizar compra"""
    limpiar_pantalla()
    print("💳 FINALIZAR COMPRA\n")
    
    if len(carrito) == 0:
        print("⚠️  Tu carrito está vacío. Agrega productos antes de finalizar.\n")
    else:
        finalizar_compra(carrito)
    
    pausar()


def main():
    """
    Función principal que ejecuta el loop del menú
    """
    print("╔════════════════════════════════════════╗")
    print("║  Inicializando sistema E-commerce...   ║")
    print("╚════════════════════════════════════════╝\n")
    
    # Diccionario de funciones por opción
    opciones = {
        "1": ejecutar_opcion_1,
        "2": ejecutar_opcion_2,
        "3": ejecutar_opcion_3,
        "4": ejecutar_opcion_4,
        "5": ejecutar_opcion_5,
        "6": ejecutar_opcion_6,
        "7": ejecutar_opcion_7,
    }
    
    # Loop principal
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        
        opcion = input("👉 Selecciona una opción: ").strip()
        
        if opcion == "0":
            limpiar_pantalla()
            print("\n╔════════════════════════════════════════╗")
            print("║   ¡Gracias por tu visita! 👋          ║")
            print("║   Vuelve pronto a visitarnos 🛍️       ║")
            print("╚════════════════════════════════════════╝\n")
            break
        
        elif opcion in opciones:
            opciones[opcion]()
        
        else:
            print(f"\n❌ Opción '{opcion}' no válida. Por favor, selecciona una opción del menú.\n")
            pausar()


# Punto de entrada del programa
if __name__ == "__main__":
    main()