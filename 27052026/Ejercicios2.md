# Problema 1 — Sistema Avanzado de Ventas y Reportes Inteligentes

**Dificultad:** Alta

Una tienda desea analizar las ventas realizadas durante el día.
Debes desarrollar un programa que permita registrar múltiples productos vendidos y generar estadísticas avanzadas.

El programa deberá:

1. Recibir un número entero `N` que representa la cantidad de productos vendidos.
2. Por cada producto recibir:

   * Nombre del producto
   * Categoría
   * Precio unitario
   * Cantidad vendida
3. Calcular:

   * Total general de ventas
   * Producto con mayor ingreso generado
   * Promedio de ventas por producto
   * Cantidad total de productos vendidos
4. Ordenar los productos por ingreso generado de mayor a menor.
5. Mostrar el reporte final.

---

## Input Format

* Primera línea: entero `N`
* Las siguientes `N` líneas contienen:

```text
nombre categoria precio cantidad
```

---

## Constraints

* `1 <= N <= 10^5`
* `1 <= precio <= 10^6`
* `1 <= cantidad <= 10^4`

---

## Sample Input

```text
5
Laptop Tecnologia 15000 2
Mouse Accesorios 350 10
Teclado Accesorios 800 5
Monitor Tecnologia 4200 3
USB Accesorios 150 20
```

---

## Sample Output

```text
TOTAL_GENERAL: 53000
PRODUCTO_TOP: Laptop
PROMEDIO_VENTA: 10600
TOTAL_PRODUCTOS: 40

REPORTE_ORDENADO:
Laptop 30000
Monitor 12600
Teclado 4000
Mouse 3500
USB 3000
```

---

# Problema 2 — Control de Inventario y Ventas

**Dificultad:** Media

Una tienda necesita verificar si las ventas realizadas exceden el inventario disponible.

Debes crear un programa que:

1. Reciba la cantidad de productos.
2. Por cada producto:

   * Nombre
   * Inventario disponible
   * Cantidad vendida
3. Mostrar:

   * `"VENTA VALIDA"` si no excede el inventario.
   * `"STOCK INSUFICIENTE"` si la venta supera el inventario.
4. Mostrar el inventario restante.

---

## Input Format

```text
N
nombre inventario venta
```

---

## Sample Input

```text
4
Laptop 10 3
Mouse 15 20
Teclado 8 4
Monitor 5 5
```

---

## Sample Output

```text
Laptop VENTA VALIDA STOCK_RESTANTE 7
Mouse STOCK INSUFICIENTE
Teclado VENTA VALIDA STOCK_RESTANTE 4
Monitor VENTA VALIDA STOCK_RESTANTE 0
```

---

# Problema 3 — Ticket de Compra con Descuentos

**Dificultad:** Media

Una tienda desea generar tickets automáticos aplicando descuentos según el total de compra.

Reglas:

* Si el total es mayor o igual a `5000`, aplicar 20%
* Si el total es mayor o igual a `2000` y menor a `5000`, aplicar 10%
* En otro caso, no aplicar descuento

El programa deberá:

1. Recibir la cantidad de productos.
2. Por cada producto:

   * Nombre
   * Precio
   * Cantidad
3. Mostrar:

   * Subtotal
   * Descuento aplicado
   * Total final

---

## Input Format

```text
N
nombre precio cantidad
```

---

## Sample Input

```text
3
Laptop 15000 1
Mouse 300 2
USB 200 5
```

---

## Sample Output

```text
SUBTOTAL: 16600
DESCUENTO: 3320
TOTAL_FINAL: 13280
```

---

# Problema 4 — Producto Más Vendido

**Dificultad:** Media

Una tienda quiere identificar cuál fue el producto más vendido durante el día.

Debes desarrollar un programa que:

1. Reciba un número `N`.
2. Por cada producto:

   * Nombre
   * Cantidad vendida
3. Determinar:

   * Producto con mayor cantidad vendida
   * Cantidad total vendida
   * Productos que superen el promedio de ventas

---

## Input Format

```text
N
nombre cantidad
```

---

## Sample Input

```text
5
Laptop 4
Mouse 15
Teclado 8
Monitor 3
USB 20
```

---

## Sample Output

```text
PRODUCTO_TOP: USB
CANTIDAD_TOP: 20
TOTAL_VENDIDO: 50
PROMEDIO: 10

SUPERAN_PROMEDIO:
Mouse
USB
```
