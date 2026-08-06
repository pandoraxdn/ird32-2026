import sys                      # Sistema: argumentos de línea de comandos y salida
import random                   # Generación de números aleatorios para el gráfico en tiempo real
import math                     # Funciones matemáticas (seno, coseno) sin usar NumPy

# PySide6: bindings oficiales de Qt para Python
from PySide6.QtWidgets import (
    QApplication,      # La aplicación en sí, gestiona el bucle de eventos
    QMainWindow,       # Ventana principal con barra de título y menú
    QWidget,           # Contenedor genérico para colocar otros widgets
    QGridLayout        # Distribución en cuadrícula (filas x columnas)
)
from PySide6.QtCore import QTimer  # Temporizador para actualizaciones periódicas

import pyqtgraph as pg              # Librería de gráficos (alias pg)

# ======================================================================
# 2. CLASE PRINCIPAL
# ======================================================================

class GraficWindow(QMainWindow):
    """
    Ventana que muestra 8 gráficos diferentes en un layout de cuadrícula.
    Todos los gráficos usan listas de Python (sin NumPy) para los datos.
    Incluye un gráfico de barras personalizable mediante arreglos.
    """

    # ------------------------------------------------------------------
    # 2.1 CONSTRUCTOR
    # ------------------------------------------------------------------

    def __init__(self):
        """
        Inicializa la ventana, crea los 8 gráficos, configura el layout
        y arranca el temporizador para el gráfico en tiempo real.
        """
        # Llamada obligatoria al constructor de la clase base (QMainWindow)
        super().__init__()

        # ---------- Configuración básica de la ventana ----------
        self.setWindowTitle("Todos los gráficos en uno + Barras personalizadas")
        self.setGeometry(100, 100, 1400, 1000)  # (x, y, ancho, alto)

        # ---------- Widget central y layout ----------
        # QWidget: contenedor vacío que actuará como fondo para los gráficos
        central = QWidget()
        self.setCentralWidget(central)   # Establece el widget central de QMainWindow

        # QGridLayout: organiza los widgets en una matriz de filas y columnas
        grid = QGridLayout(central)

        # ======================================================================
        # 3. GRÁFICO 1: LÍNEA (fila 0, columna 0)
        # ======================================================================

        # pg.PlotWidget: widget que contiene un gráfico 2D con ejes y leyenda
        p1 = pg.PlotWidget(title="Línea")

        # Datos: dos listas de enteros (coordenadas X e Y)
        # El método .plot() dibuja una línea conectando los puntos en orden.
        # 'pen' establece el color y grosor ('b' = azul).
        p1.plot(
            [0, 1, 2, 3, 4, 5, 6, 7],   # coordenadas X
            [1, 3, 2, 5, 4, 6, 8, 7],   # coordenadas Y
            pen='b'
        )

        # Activa las líneas de cuadrícula verticales (x) y horizontales (y)
        p1.showGrid(x=True, y=True)

        # Añade este gráfico al layout en la fila 0, columna 0
        grid.addWidget(p1, 0, 0)

        # ======================================================================
        # 4. GRÁFICO 2: DISPERSIÓN (SCATTER) (fila 0, columna 1)
        # ======================================================================

        p2 = pg.PlotWidget(title="Dispersión")

        # ScatterPlotItem: dibuja puntos sueltos en el gráfico
        # - x, y: listas de coordenadas
        # - size: diámetro de cada punto en píxeles
        # - brush: color de relleno ('r' = rojo)
        scatter = pg.ScatterPlotItem(
            x=[1, 2, 3, 4, 5, 6, 7, 8],
            y=[2, 5, 3, 7, 4, 8, 6, 9],
            size=12,
            brush='r'
        )

        # addItem() añade un elemento gráfico al PlotWidget (no solo líneas)
        p2.addItem(scatter)
        p2.showGrid(x=True, y=True)
        grid.addWidget(p2, 0, 1)

        # ======================================================================
        # 5. GRÁFICO 3: BARRAS FIJAS (fila 0, columna 2)
        # ======================================================================

        p3 = pg.PlotWidget(title="Barras fijas")

        # BarGraphItem: dibuja barras verticales
        # - x: posición de cada barra en el eje horizontal
        # - height: altura de cada barra
        # - width: ancho de cada barra (en unidades del eje X)
        # - brush: color de relleno ('g' = verde)
        bar = pg.BarGraphItem(
            x=[0, 1, 2, 3, 4],
            height=[7, 4, 9, 6, 8],
            width=0.6,
            brush='g'
        )
        p3.addItem(bar)

        # Configurar etiquetas personalizadas en el eje X
        # setTicks() recibe una lista de listas de tuplas (posición, etiqueta)
        p3.getAxis('bottom').setTicks([
            [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
        ])

        # Mostrar solo cuadrícula horizontal (y=True) para no saturar
        p3.showGrid(x=False, y=True)
        grid.addWidget(p3, 0, 2)

        # ======================================================================
        # 6. GRÁFICO 4: ÁREA RELLENA (fila 1, columna 0)
        # ======================================================================

        p4 = pg.PlotWidget(title="Área rellena")

        # .plot() con parámetros especiales para relleno:
        # - fillLevel=0: rellena desde el eje Y=0 hasta la curva
        # - fillBrush: color y transparencia del relleno (R, G, B, A)
        # - pen: color de la línea de contorno
        p4.plot(
            [0, 1, 2, 3, 4, 5, 6],          # X
            [2, 4, 3, 6, 5, 7, 6],          # Y
            fillLevel=0,
            fillBrush=(100, 100, 200, 80),  # Azul con 80/255 opacidad
            pen='purple'
        )
        p4.showGrid(x=True, y=True)
        grid.addWidget(p4, 1, 0)

        # ======================================================================
        # 7. GRÁFICO 5: HISTOGRAMA (fila 1, columna 1)
        # ======================================================================

        p5 = pg.PlotWidget(title="Histograma")

        # Datos de ejemplo: lista con valores repetidos
        datos = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8, 9]

        # --- Construcción manual de frecuencias (sin NumPy) ---
        # frec = { valor : cantidad_de_veces_que_aparece }
        frec = {}
        for v in datos:
            frec[v] = frec.get(v, 0) + 1   # get(v,0) devuelve 0 si no existe la clave

        # bins: valores únicos ordenados (ej: [1,2,3,4,5,6,7,8,9])
        bins = sorted(frec.keys())
        # counts: frecuencias correspondientes
        counts = [frec[b] for b in bins]

        # BarGraphItem para el histograma
        bar_hist = pg.BarGraphItem(
            x=bins,
            height=counts,
            width=0.8,
            brush=(200, 100, 0)   # Naranja
        )
        p5.addItem(bar_hist)
        p5.showGrid(x=False, y=True)
        grid.addWidget(p5, 1, 1)

        # ======================================================================
        # 8. GRÁFICO 6: SENO Y COSENO (fila 1, columna 2)
        # ======================================================================

        p6 = pg.PlotWidget(title="Seno y Coseno")

        # Generar 63 puntos de 0 a 6.2 con paso 0.1 mediante comprensión de listas
        x6 = [i * 0.1 for i in range(63)]

        # Calcular seno y coseno usando math (sin NumPy)
        seno = [math.sin(v) for v in x6]
        coseno = [math.cos(v) for v in x6]

        # Dibujar ambas curvas; 'name' se usa para la leyenda
        p6.plot(x6, seno, pen='r', name='Seno')
        p6.plot(x6, coseno, pen='b', name='Coseno')

        # Añadir la leyenda automáticamente usando los nombres
        p6.addLegend()
        p6.showGrid(x=True, y=True)
        grid.addWidget(p6, 1, 2)

        # ======================================================================
        # 9. GRÁFICO 7: TIEMPO REAL (fila 2, columnas 0 a 2)
        #    Ocupa todo el ancho de la ventana (3 columnas)
        # ======================================================================

        p7 = pg.PlotWidget(title="Tiempo real (actualiza cada 100 ms)")

        # self.buffer: lista que almacena los últimos 50 valores (inicializada a ceros)
        self.buffer = [0] * 50

        # self.curva: objeto que representa la línea en el gráfico.
        # Almacenamos una referencia para poder actualizarla después.
        self.curva = p7.plot(self.buffer, pen='orange')

        p7.showGrid(x=True, y=True)

        # Añadir este gráfico en la fila 2, columna 0, ocupando 1 fila y 3 columnas
        grid.addWidget(p7, 2, 0, 1, 3)

        # ======================================================================
        # 10. GRÁFICO 8: BARRAS PERSONALIZADAS (fila 3, columnas 0 a 2)
        #     ¡AQUÍ PUEDES CAMBIAR LOS ARREGLOS x e y!
        # ======================================================================

        p8 = pg.PlotWidget(title="Barras personalizadas")

        # --------------------------------------------------------------
        #  DEFINE TUS PROPIOS DATOS PARA LAS BARRAS
        #  Cambia los valores de 'x_personal' y 'y_personal' a tu gusto.
        #  También puedes modificar la lista 'etiquetas'.
        # --------------------------------------------------------------

        # x_personal: posiciones de las barras en el eje horizontal (número de barras)
        x_personal = [0, 1, 2, 3, 4, 5, 6]

        # y_personal: alturas de cada barra (debe tener la misma longitud que x_personal)
        y_personal = [10, 5, 12, 8, 15, 6, 9]

        # etiquetas: nombres que aparecerán debajo de cada barra (opcional)
        etiquetas = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul']

        # Crear el objeto BarGraphItem con los datos personalizados
        bar_personal = pg.BarGraphItem(
            x=x_personal,
            height=y_personal,
            width=0.6,                      # Ancho de cada barra (en unidades X)
            brush=pg.mkBrush(139, 92, 246)  # Color violeta (R=139, G=92, B=246)
        )
        p8.addItem(bar_personal)

        # Asignar etiquetas al eje X si se definieron y tienen la misma longitud
        if len(etiquetas) == len(x_personal):
            # Construir los ticks: lista de listas de tuplas (posición, etiqueta)
            ticks = [[(x_personal[i], etiquetas[i]) for i in range(len(x_personal))]]
            p8.getAxis('bottom').setTicks(ticks)

        p8.showGrid(x=False, y=True)   # Solo cuadrícula horizontal
        grid.addWidget(p8, 3, 0, 1, 3)  # Fila 3, columna 0, 1 fila, 3 columnas

        # ======================================================================
        # 11. TEMPORIZADOR PARA ACTUALIZAR EL GRÁFICO EN TIEMPO REAL
        # ======================================================================

        # QTimer ejecuta una función cada cierto intervalo
        self.timer = QTimer()

        # Conectamos la señal 'timeout' al método 'actualizar'
        self.timer.timeout.connect(self.actualizar)

        # Iniciamos el temporizador con 100 milisegundos de intervalo
        self.timer.start(100)

        # ======================================================================
        # FIN DEL CONSTRUCTOR
        # ======================================================================

    # ------------------------------------------------------------------
    # 2.2 MÉTODO DE ACTUALIZACIÓN PARA EL TIEMPO REAL
    # ------------------------------------------------------------------

    def actualizar(self):
        """
        Se ejecuta automáticamente cada 100 ms (gracias al QTimer).
        Genera un número aleatorio, lo añade al buffer y actualiza la curva.
        """
        # Genera un entero aleatorio entre 0 y 10 (ambos inclusive)
        nuevo = random.randint(0, 10)

        # Elimina el primer elemento del buffer (el más antiguo)
        self.buffer.pop(0)

        # Añade el nuevo valor al final del buffer
        self.buffer.append(nuevo)

        # Actualiza la curva con los datos del buffer completo
        # setData() reemplaza todos los datos de la curva en el gráfico
        self.curva.setData(self.buffer)


# ======================================================================
# 12. PUNTO DE ENTRADA DE LA APLICACIÓN
# ======================================================================

if __name__ == '__main__':
    """
    Bloque principal que se ejecuta solo cuando el script se corre directamente.
    - Crea la aplicación Qt (QApplication)
    - Instancia la ventana principal
    - La muestra y ejecuta el bucle de eventos.
    """
    # QApplication es obligatoria para cualquier aplicación Qt.
    # sys.argv pasa los argumentos de línea de comandos.
    app = QApplication(sys.argv)

    # Creamos la ventana
    ventana = GraficWindow()

    # Mostramos la ventana (por defecto está oculta)
    ventana.show()

    # sys.exit(app.exec()) inicia el bucle de eventos y finaliza cuando se cierra.
    # El código de retorno se pasa al sistema operativo.
    sys.exit(app.exec())
