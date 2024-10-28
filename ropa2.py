from abc import ABC, abstractmethod
class Producto(ABC):
    def __init__(self, nombre, precio, marca, descripcion):
        self._nombre = nombre  
        self._precio = precio
        self._marca = marca
        self._descripcion = descripcion
    @abstractmethod
    def mostrar_info(self):
        pass  

    def obtener_precio(self):
        return self._precio  
class Ropa(Producto):
    def __init__(self, nombre, precio, marca, descripcion, talla):
        super().__init__(nombre, precio, marca, descripcion)
        self._talla = talla
class Camisa(Ropa):
    def mostrar_info(self):
        return f"Camisa: {self._nombre} ({self._marca}) - ${self._precio:.2f}: {self._descripcion}, Talla: {self._talla}"

class Pantalon(Ropa):
    def mostrar_info(self):
        return f"Pantalón: {self._nombre} ({self._marca}) - ${self._precio:.2f}: {self._descripcion}, Talla: {self._talla}"

class Zapato(Producto):
    def __init__(self, nombre, precio, marca, descripcion, talla):
        super().__init__(nombre, precio, marca, descripcion)
        self._talla = talla
    def mostrar_info(self):
        return f"Zapato: {self._nombre} ({self._marca}) - ${self._precio:.2f}: {self._descripcion}, Talla: {self._talla}"


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        print(f"\nCategoría: {self.nombre}")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. {producto.mostrar_info()}")


class Tienda:
    def __init__(self):
        self.categorias = []
        self.carrito = [] 
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
    def mostrar_categorias(self):
        print("\nCategorías disponibles:")
        for i, categoria in enumerate(self.categorias):
            print(f"{i + 1}. {categoria.nombre}")
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"Producto agregado al carrito: {producto.mostrar_info()}")
    def mostrar_resumen_final(self):
        if not self.carrito:
            print("\nNo hay productos en el carrito.")
            return
        print("\nResumen de la compra:")
        total = 0
        for producto in self.carrito:
            print(f"- {producto.mostrar_info()}")
            total += producto.obtener_precio()
        
        print(f"\nTotal a pagar: ${total:.2f}")


camisas = Categoria("Camisas")
camisas.agregar_producto(Camisa("Camisa Casual", 80000, "Zara", "Camisa de algodón con corte regular.", "M"))
camisas.agregar_producto(Camisa("Camisa Formal", 250000, "H&M", "Camisa de vestir con ajuste slim.", "L"))
camisas.agregar_producto(Camisa("Camisa de Rayas", 240000, "Tommy Hilfiger", "Camisa con rayas clásicas.", "S"))
camisas.agregar_producto(Camisa("Camisa de Seda", 300000, "Chanel", "Camisa de seda elegante.", "M"))

pantalones = Categoria("Pantalones")
pantalones.agregar_producto(Pantalon("Pantalón Chino", 50000, "Levi's", "Pantalón chino ligero y cómodo.", "32"))
pantalones.agregar_producto(Pantalon("Jeans", 90000, "Diesel", "Jeans de corte clásico.", "34"))
pantalones.agregar_producto(Pantalon("Pantalón de Vestir", 320000, "Calvin Klein", "Pantalón formal para ocasiones especiales.", "36"))
pantalones.agregar_producto(Pantalon("Joggers", 290000, "Adidas", "Pantalones cómodos para deporte.", "M"))

zapatos = Categoria("Zapatos")
zapatos.agregar_producto(Zapato("Zapatos Deportivos", 490000, "Nike", "Zapatos ideales para hacer ejercicio.", 42))
zapatos.agregar_producto(Zapato("Zapatos de Cuero", 980000, "Gucci", "Zapatos de cuero elegantes.", 44))
zapatos.agregar_producto(Zapato("Zapatillas", 390000, "Puma", "Zapatillas de estilo urbano.", 43))
zapatos.agregar_producto(Zapato("Botas", 600000, "Timberland", "Botas resistentes para el invierno.", 45))

tienda = Tienda()
tienda.agregar_categoria(camisas)
tienda.agregar_categoria(pantalones)
tienda.agregar_categoria(zapatos)

def main():
    while True:
        tienda.mostrar_categorias()
        
        try:
            categoria_index = int(input("\nSelecciona una categoría (número) o 0 para salir: ")) - 1
            if categoria_index == -1:
                tienda.mostrar_resumen_final()
                print("Gracias por visitar la tienda.")
                break
            if categoria_index < 0 or categoria_index >= len(tienda.categorias):
                print("Selección no válida. Intenta de nuevo.")
                continue
            
            categoria = tienda.categorias[categoria_index]
            categoria.mostrar_productos()
            
            producto_index = int(input("\nSelecciona un producto (número) para agregar al carrito: ")) - 1
            if producto_index < 0 or producto_index >= len(categoria.productos):
                print("Selección no válida. Intenta de nuevo.")
                continue
            
            producto = categoria.productos[producto_index]
            tienda.agregar_al_carrito(producto)

        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
