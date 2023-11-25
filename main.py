from conexion import *
import sys 
import random
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QVBoxLayout, QWidget, QPushButton


import form_entrega
import inventario
import form_entrada
import consumo
import pedido
import entradas
import trabajadores

con = conectar()
crear_tabla_epp(con)
crear_tabla_trabajador(con)
crear_tabla_vsalida(con)
crear_tabla_ventrada(con)
crear_tabla_marca(con)
crear_tabla_categoria(con)
crear_tabla_pedido(con)
crear_tabla_pedido_final(con)

open_windows = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Inventario | Inicio")
        self.setMinimumWidth(400)
        self.setMinimumHeight(250)
        
        # BOTONES
        self.request_button = QPushButton("Registrar Entrega")
        self.request_button.clicked.connect(self.show_request_form)
        self.view_inventory_button = QPushButton("Ver Inventario")
        self.view_inventory_button.clicked.connect(self.show_inventory_view)
        self.add_article_button = QPushButton("Nuevo Artículo")
        self.add_article_button.clicked.connect(self.show_new_article_form)
        self.view_consumption_button = QPushButton("Ver Historial de Consumo")
        self.view_consumption_button.clicked.connect(self.show_consumption_view)
        self.view_entries_button = QPushButton("Ver Historial de Entradas")
        self.view_entries_button.clicked.connect(self.show_entries_view)
        self.view_employees_button = QPushButton("Ver Datos de los Trabajadores")
        self.view_employees_button.clicked.connect(self.show_employees_view)        
        
        # Create layout and add button
        layout = QVBoxLayout()
        layout.addWidget(self.request_button)
        layout.addWidget(self.view_inventory_button)
        layout.addWidget(self.add_article_button)
        layout.addWidget(self.view_consumption_button)
        layout.addWidget(self.view_entries_button)
        layout.addWidget(self.view_employees_button)
        
        # Set central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Instance variable to hold request form
        self.request_form = None
        self.inventory_view = None
        self.new_article_form = None
        self.consumption_view = None
        self.entries_view = None
        self.employees_view = None

        open_windows.append(self)

        self.refresh_all_windows()

    def show_request_form(self):
        self.request_form = form_entrega.RequestForm()
        self.request_form.setWindowTitle("Formulario de Registro de Entrega EPP")
        self.request_form.show()

    def show_inventory_view(self):
        self.inventory_view = inventario.InventoryView()
        self.inventory_view.show()

    def show_new_article_form(self):
        self.new_article_form = form_entrada.NewArticleForm()
        self.new_article_form.show()

    def show_consumption_view(self):
        self.consumption_view = consumo.ConsumptionView()
        self.consumption_view.show()

    def show_entries_view(self):
        self.entries_view = entradas.EntriesView()
        self.entries_view.show()

    def show_employees_view(self):
        self.employees_view = trabajadores.EmployeesView()
        self.employees_view.show()

    def refresh_all_windows(self):

        for window in open_windows:
            window.update()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()