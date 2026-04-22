"""
Función para mostrar el catálogo de productos
"""

from modulos.utils import formatear_precio


def mostrar_catalogo(catalogo):
    """
    Muestra el catálogo completo de productos en formato tabla
    
    Args:
        catalogo (list): Lista de diccionarios con productos
    """
    if len(catalogo) == 0:
        print("⚠️  No hay productos disponibles en el catálogo\n")
        return
    
    print("═" * 100)
    print(f"{'ID':<5} {'NOMBRE':<35} {'CATEGORÍA':<20} {'PRECIO':<15} {'STOCK':<10}")
    print("═" * 100)
    
    for producto in catalogo:
        print(
            f"{producto['id']:<5} "
            f"{producto['nombre']:<35} "
            f"{producto.get('categoria', 'Sin categoría'):<20} "
            f"{formatear_precio(producto['precio']):<15} "
            f"{producto.get('stock', 'N/A'):<10}"
        )
    
    print("═" * 100)
    print(f"Total de productos: {len(catalogo)}")
    print("═" * 100)
    print()