import string
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 Grupo A")
        self.setMinimumSize(300, 100)
        self.setMaximumSize(1000, 600)

        # Layout Principal
        self.layout_principal = QGridLayout()

        # Contenedor
        contenedor = QWidget()
        contenedor.setLayout(self.layout_principal)
        self.setCentralWidget(contenedor)

        self.stack = QStackedLayout()

        self.zoa1 = QWidget()
        self.zoa2 = QWidget()
        self.zoa3 = QWidget()

        ### ZONA 1 #####################3
        grid1 = QGridLayout()


        ## Z1 Izquierda
        grid_izq_widget = QWidget()
        grid_izq = QGridLayout()
        grid_izq_widget.setLayout(grid_izq)

        grid_izq.addWidget(QLabel("Zoa Activada"), 0, 0)
        self.check_activada = QCheckBox()
        self.check_activada.clicked.connect(self.activar_zona)

        grid_izq.addWidget(self.check_activada, 0, 1)

        grid_izq.addWidget(QLabel("Hora de comezo de rego"), 1, 0)
        self.rego = QLineEdit()
        grid_izq.addWidget(self.rego, 1, 1)

        grid_izq.addWidget(QLabel("Duración rego"), 2, 0)
        self.duracion_rego = QSlider(Qt.Orientation.Horizontal)
        self.duracion_rego.setMinimum(0)
        self.duracion_rego.setMaximum(600)
        self.duracion_rego.valueChanged.connect(self.duracion_rego_activada)
        grid_izq.addWidget(self.duracion_rego, 2, 1)


        opciones_widget = QGroupBox("Opcións")
        opciones = QHBoxLayout()
        opciones_widget.setLayout(opciones)

        self.select_semanal = QComboBox()
        self.select_semanal.addItems(["semanal", "diario"])
        self.select_semanal.currentIndexChanged.connect(self.activar_tiempos)
        opciones.addWidget(self.select_semanal)

        self.antixiada = QCheckBox("Antixiada")
        self.chuvia = QCheckBox("Chuvia")

        opciones.addWidget(self.antixiada)
        opciones.addWidget(self.chuvia)

        grid_izq.addWidget(opciones_widget, 3, 0, 1, 2)

        grid1.addWidget(grid_izq_widget, 0, 0)

        ## Z1 Derecha
        grid_der_widget = QWidget()
        grid_der = QGridLayout()
        grid_der_widget.setLayout(grid_der)

        self.dias_group = QGroupBox("Dias")

        grid_der_dias = QGridLayout()

        grid_der.addWidget(self.dias_group, 0, 0)
        self.luns = QCheckBox("Luns")
        grid_der_dias.addWidget(self.luns, 1, 0)
        self.martes = QCheckBox("Martes")
        grid_der_dias.addWidget(self.martes, 1, 1)
        self.mercores = QCheckBox("Mercores")
        grid_der_dias.addWidget(self.mercores, 2, 0)
        self.xoves = QCheckBox("Xoves")
        grid_der_dias.addWidget(self.xoves, 2, 1)
        self.venres = QCheckBox("Venres")
        grid_der_dias.addWidget(self.venres, 3, 0)
        self.sabado = QCheckBox("Sabado")
        grid_der_dias.addWidget(self.sabado, 3, 1)
        self.domingo = QCheckBox("Domingo")
        grid_der_dias.addWidget(self.domingo, 4, 0)
        self.dias_group.setLayout(grid_der_dias)

        grid1.addWidget(grid_der_widget, 0, 1)

        self.aceptar = QPushButton("Aceptar")
        grid1.addWidget(self.aceptar, 1, 1)


        # No tocar
        self.zoa1.setLayout(grid1)

        ### ZONA 2 ############################
        grid2 = QGridLayout()

        self.label_zoa2 = QLabel("Zoa 2")
        grid2.addWidget(self.label_zoa2, 0, 0)

        self.zoa2.setLayout(grid2)


        ### ZONA 3 ############################33
        grid3 = QGridLayout()

        self.texto_consola = QTextEdit()

        grid3.addWidget(QLabel("Texto:"), 0, 0)
        grid3.addWidget(self.texto_consola, 0, 1)

        self.zoa3.setLayout(grid3)

        ### Definicion de stack
        self.stack.addWidget(self.zoa1)
        self.stack.addWidget(self.zoa2)
        self.stack.addWidget(self.zoa3)

        ### CREAR BOTONES

        self.botones = QWidget()
        self.botones_layout = QHBoxLayout()
        self.botones.setLayout(self.botones_layout)

        self.boton1 = QPushButton("Configuración zoa 1")
        self.botones_layout.addWidget(self.boton1)
        self.boton1.clicked.connect(self.cambiar_zoa1)

        self.boton2 = QPushButton("Configuración zoa 2")
        self.botones_layout.addWidget(self.boton2)
        self.boton2.clicked.connect(self.cambiar_zoa2)

        self.boton3 = QPushButton("Consola")
        self.botones_layout.addWidget(self.boton3)
        self.boton3.clicked.connect(self.cambiar_consola)

        self.layout_principal.addLayout(self.stack, 0, 0)
        self.layout_principal.addWidget(self.botones, 1, 0)

        self.luns.setDisabled(True)
        self.martes.setDisabled(True)
        self.mercores.setDisabled(True)
        self.xoves.setDisabled(True)
        self.venres.setDisabled(True)
        self.sabado.setDisabled(True)
        self.domingo.setDisabled(True)

    def cambiar_zoa1(self):
        self.stack.setCurrentIndex(0)
        self.boton1.setDisabled(True)
        self.boton2.setDisabled(False)
        self.boton3.setDisabled(False)

    def cambiar_zoa2(self):
        self.stack.setCurrentIndex(1)
        self.boton1.setDisabled(False)
        self.boton2.setDisabled(True)
        self.boton3.setDisabled(False)

    def cambiar_consola(self):
        self.stack.setCurrentIndex(2)
        self.boton1.setDisabled(False)
        self.boton2.setDisabled(False)
        self.boton3.setDisabled(True)

    def activar_zona(self):
        if self.check_activada.isChecked():
            self.texto_consola.insertPlainText("Zoa activada\n")
        else:
            self.texto_consola.insertPlainText("Zoa desactivada\n")

    def duracion_rego_activada(self):
        #Pasar a string
        valor = str(self.duracion_rego.value())
        self.label_zoa2.setText("Duracion rego : " + valor + " min")
        self.texto_consola.insertPlainText("Duracion rego : " + valor + " min\n")

    def activar_tiempos(self):
        if self.select_semanal.currentIndex() == 0:
            self.luns.setDisabled(True)
            self.martes.setDisabled(True)
            self.mercores.setDisabled(True)
            self.xoves.setDisabled(True)
            self.venres.setDisabled(True)
            self.sabado.setDisabled(True)
            self.domingo.setDisabled(True)
        elif self.select_semanal.currentIndex() == 1:
            self.luns.setEnabled(True)
            self.martes.setEnabled(True)
            self.mercores.setEnabled(True)
            self.xoves.setEnabled(True)
            self.venres.setEnabled(True)
            self.sabado.setEnabled(True)
            self.domingo.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())