"""
Gestión del carrito de compras
"""

from modulos.utils import validar_numero, formatear_precio, confirmar_accion

# Carrito de compras (lista de diccionarios)
carrito = []


def agregar_al_carrito(catalogo, carrito_actual):
    """
    Agrega un producto al carrito
    
    Args:
        catalogo (list): Lista de productos disponibles
        carrito_actual (list): Carrito de compras actual
    """
    try:
        id_producto = validar_numero(
            "Ingresa el ID del producto a agregar: ",
            minimo=1,
            maximo=len(catalogo)
        )
        
        # Buscar el producto por ID
        producto = None
        for p in catalogo:
            if p["id"] == id_producto:
                producto = p
                break
        
        if producto:
            cantidad = validar_numero(
                f"¿Cuántas unidades de '{producto['nombre']}' deseas agregar? ",
                minimo=1
            )
            
            # Verificar si el producto ya está en el carrito
            producto_existente = None
            for item in carrito_actual:
                if item["id"] == id_producto:
                    producto_existente = item
                    break
            
            if producto_existente:
                producto_existente["cantidad"] += cantidad
                print(f"\n✅ Se agregaron {cantidad} unidades más de '{producto['nombre']}'")
                print(f"   Total en carrito: {producto_existente['cantidad']} unidades")
            else:
                carrito_actual.append({
                    "id": producto["id"],
                    "nombre": producto["nombre"],
                    "precio": producto["precio"],
                    "cantidad": cantidad
                })
                print(f"\n✅ '{producto['nombre']}' agregado al carrito")
                print(f"   Cantidad: {cantidad} unidades")
                print(f"   Precio unitario: {formatear_precio(producto['precio'])}")
        else:
            print(f"\n❌ No se encontró producto con ID {id_producto}")
    
    except Exception as e:
        print(f"\n❌ Error al agregar producto: {e}")


def ver_carrito(carrito_actual):
    """
    Muestra el contenido del carrito y el total
    
    Args:
        carrito_actual (list): Carrito de compras actual
    """
    if len(carrito_actual) == 0:
        print("🛒 Tu carrito está vacío\n")
        return
    
    print("═" * 80)
    print(f"{'ID':<5} {'PRODUCTO':<30} {'PRECIO UNIT.':<15} {'CANT.':<8} {'SUBTOTAL':<15}")
    print("═" * 80)
    
    total = 0
    
    for item in carrito_actual:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        
        print(
            f"{item['id']:<5} "
            f"{item['nombre']:<30} "
            f"{formatear_precio(item['precio']):<15} "
            f"{item['cantidad']:<8} "
            f"{formatear_precio(subtotal):<15}"
        )
    
    print("═" * 80)
    print(f"{'TOTAL A PAGAR:':<60} {formatear_precio(total):<15}")
    print("═" * 80)
    print()


def eliminar_del_carrito(carrito_actual):
    """
    Elimina un producto específico del carrito
    
    Args:
        carrito_actual (list): Carrito de compras actual
    """
    try:
        id_producto = validar_numero(
            "Ingresa el ID del producto a eliminar: ",
            minimo=1
        )
        
        # Buscar el producto en el carrito
        producto_encontrado = None
        indice = -1
        
        for i, item in enumerate(carrito_actual):
            if item["id"] == id_producto:
                producto_encontrado = item
                indice = i
                break
        
        if producto_encontrado:
            print(f"\n📦 Producto encontrado: {producto_encontrado['nombre']}")
            print(f"   Cantidad en carrito: {producto_encontrado['cantidad']}")
            
            if confirmar_accion("¿Deseas eliminar este producto del carrito? (s/n): "):
                carrito_actual.pop(indice)
                print(f"✅ '{producto_encontrado['nombre']}' eliminado del carrito\n")
            else:
                print("❌ Operación cancelada\n")
        else:
            print(f"\n❌ No se encontró producto con ID {id_producto} en el carrito\n")
    
    except Exception as e:
        print(f"\n❌ Error al eliminar producto: {e}\n")


def vaciar_carrito(carrito_actual):
    """
    Vacía completamente el carrito
    
    Args:
        carrito_actual (list): Carrito de compras actual
    """
    carrito_actual.clear()


def finalizar_compra(carrito_actual):
    """
    Finaliza la compra y muestra resumen
    
    Args:
        carrito_actual (list): Carrito de compras actual
    """
    print("═" * 80)
    print("                        RESUMEN DE COMPRA")
    print("═" * 80)
    
    ver_carrito(carrito_actual)
    
    if confirmar_accion("¿Confirmar compra? (s/n): "):
        print("\n" + "═" * 80)
        print("✅ ¡COMPRA REALIZADA EXITOSAMENTE!")
        print("═" * 80)
        print("📧 Recibirás un correo con los detalles de tu compra")
        print("📦 Tu pedido será despachado en 24-48 horas hábiles")
        print("═" * 80)
        
        vaciar_carrito(carrito_actual)
    else:
        print("\n❌ Compra cancelada. Tu carrito se mantiene intacto.\n")