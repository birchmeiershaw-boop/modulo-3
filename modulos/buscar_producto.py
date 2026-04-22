"""
Función para buscar productos en el catálogo
"""

from modulos.utils import formatear_precio


def buscar_producto(tipo, catalogo):
    """
    Busca productos por nombre o categoría
    
    Args:
        tipo (str): 'nombre' o 'categoria'
        catalogo (list): Lista de productos
    """
    termino = input(f"Ingresa el {tipo} a buscar: ").strip().lower()
    
    if not termino:
        print("\n❌ Debes ingresar un término de búsqueda\n")
        return
    
    resultados = []
    
    for producto in catalogo:
        if tipo == "nombre":
            if termino in producto["nombre"].lower():
                resultados.append(producto)
        elif tipo == "categoria":
            if termino in producto.get("categoria", "").lower():
                resultados.append(producto)
    
    if len(resultados) == 0:
        print(f"\n⚠️  No se encontraron productos con {tipo} '{termino}'\n")
    else:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s):\n")
        print("═" * 100)
        print(f"{'ID':<5} {'NOMBRE':<35} {'CATEGORÍA':<20} {'PRECIO':<15} {'STOCK':<10}")
        print("═" * 100)
        
        for producto in resultados:
            print(
                f"{producto['id']:<5} "
                f"{producto['nombre']:<35} "
                f"{producto.get('categoria', 'Sin categoría'):<20} "
                f"{formatear_precio(producto['precio']):<15} "
                f"{producto.get('stock', 'N/A'):<10}"
            )
        
        print("═" * 100)
        print()