"""
Utilidades y funciones auxiliares para el e-commerce
"""

import os
import platform


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola según el sistema operativo
    """
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system("cls")
    else:  # Linux, macOS, etc.
        os.system("clear")


def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter
    """
    input("\n⏸️  Presiona ENTER para continuar...")


def validar_opcion(mensaje, opciones_validas=None):
    """
    Valida que el usuario ingrese una opción válida
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        opciones_validas (list): Lista de opciones válidas (opcional)
    
    Returns:
        str: Opción ingresada por el usuario
    """
    while True:
        opcion = input(mensaje).strip()
        
        if opciones_validas is None:
            return opcion
        
        if opcion in opciones_validas:
            return opcion
        
        print(f"❌ Opción inválida. Opciones válidas: {', '.join(opciones_validas)}")


def validar_numero(mensaje, minimo=None, maximo=None):
    """
    Valida que el usuario ingrese un número dentro de un rango
    
    Args:
        mensaje (str): Mensaje a mostrar
        minimo (int): Valor mínimo aceptado
        maximo (int): Valor máximo aceptado
    
    Returns:
        int: Número válido ingresado
    """
    while True:
        try:
            numero = int(input(mensaje))
            
            if minimo is not None and numero < minimo:
                print(f"❌ El número debe ser mayor o igual a {minimo}")
                continue
            
            if maximo is not None and numero > maximo:
                print(f"❌ El número debe ser menor o igual a {maximo}")
                continue
            
            return numero
        
        except ValueError:
            print("❌ Por favor, ingresa un número válido")


def formatear_precio(precio):
    """
    Formatea un precio con separador de miles
    
    Args:
        precio (int/float): Precio a formatear
    
    Returns:
        str: Precio formateado
    """
    return f"${precio:,.0f}".replace(",", ".")


def confirmar_accion(mensaje="¿Estás seguro? (s/n): "):
    """
    Pide confirmación al usuario para una acción
    
    Args:
        mensaje (str): Mensaje de confirmación
    
    Returns:
        bool: True si confirma, False si cancela
    """
    respuesta = validar_opcion(
        mensaje,
        opciones_validas=["s", "n", "S", "N"]
    )
    
    return respuesta.lower() == "s"