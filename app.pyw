from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QDoubleValidator
from interface.ventana_principal import Ui_MainWindow
import sys

class RegistroLibros(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Instancias
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicialización de la ventana
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabla_registro.setRowCount(0)
        self.ui.precio.setValidator(QDoubleValidator())

        # Control de botones
        self.ui.btn_agregar.clicked.connect(self.agregar_registro)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_registro)

    def agregar_registro(self):
        titulo = self.ui.titulo.text().strip().title()
        autor = self.ui.autor.text().strip().title()
        editorial = self.ui.editorial.text().strip().title()
        isbn = self.ui.isbn.text().strip().title()
        precio = self.ui.precio.text().strip()

        if len(titulo) > 0 and len(autor) > 0 and len(editorial) > 0 and len(isbn) > 0 and len(precio) > 0:
            filas_tabla = self.ui.tabla_registro.rowCount()
            self.ui.tabla_registro.insertRow(filas_tabla)

            self.ui.tabla_registro.setItem(filas_tabla, 0, QTableWidgetItem(titulo))
            self.ui.tabla_registro.setItem(filas_tabla, 1, QTableWidgetItem(autor))
            self.ui.tabla_registro.setItem(filas_tabla, 2, QTableWidgetItem(editorial))
            self.ui.tabla_registro.setItem(filas_tabla, 3, QTableWidgetItem(isbn))
            self.ui.tabla_registro.setItem(filas_tabla, 4, QTableWidgetItem(precio))

            self.ui.titulo.clear()
            self.ui.autor.clear()
            self.ui.editorial.clear()
            self.ui.isbn.clear()
            self.ui.precio.clear()

            self.ui.titulo.setFocus()
    
    def eliminar_registro(self):
        fila_actual = self.ui.tabla_registro.currentRow()
        if fila_actual >= 0:
            self.ui.tabla_registro.removeRow(fila_actual)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = RegistroLibros()
    mi_app.show()
    sys.exit(app.exec_())