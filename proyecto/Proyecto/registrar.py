"""
    @author: Harol Mauricio Gómez Zapata
    @date: 22/09/2021
"""

# Clase para la ui signup

# Modulos o paquetes de PyQt5
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi

import sys
import time

import conexion

# Clase para la ui signup
class DlgRegistrar(QDialog):
    nombreArchivo = ""

    def __init__(self):
        super(DlgRegistrar, self).__init__()
        loadUi('uis/signup.ui', self)
        self.setFixedWidth(860)
        self.setFixedHeight(810)
        self.txtIdentificacion.setInputMask("9999999999")
        self.txtIdentificacion.textChanged.connect(self.mostrarIdLbl)
        self.txtCorreo.textChanged.connect(self.mostrarEmLbl)
        self.txtNombre.textChanged.connect(self.mostrarNomLbl)
        self.txtApellido.textChanged.connect(self.mostrarApeLbl)
        self.txtDireccion.textChanged.connect(self.mostrarDirLbl)
        self.txtTelefono.textChanged.connect(self.mostrarTelLbl)
        self.txtUsuario.textChanged.connect(self.mostrarUsuLbl)
        self.txtClave.textChanged.connect(self.mostrarClvLbl)
        self.txtRptClave.textChanged.connect(self.mostrarRClvLbl)
        self.bttnRegistrar.clicked.connect(self.fRegistrar)


    def fRegistrar(self):
        id = self.txtIdentificacion.text()
        self.lblMensaje.setText("Has presionado el botón 'REGISTRARME'%s"%id)


    def mostrarIdLbl(self):
        if self.txtIdentificacion.text():
            self.lblIdentificacion.setText("Identificación")
        else:
            self.lblIdentificacion.setText("")


    def mostrarEmLbl(self):
        if self.txtCorreo.text():
            self.lblCorreo.setText("Correo Electrónico")
        else:
            self.lblCorreo.setText("")


    def mostrarNomLbl(self):
        if self.txtNombre.text():
            self.lblNombre.setText("Nombre(s)")
        else:
            self.lblNombre.setText("")


    def mostrarApeLbl(self):
        if self.txtApellido.text():
            self.lblApellido.setText("Apellido(s)")
        else:
            self.lblApellido.setText("")


    def mostrarDirLbl(self):
        if self.txtDireccion.text():
            self.lblDireccion.setText("Dirección")
        else:
            self.lblDireccion.setText("")


    def mostrarTelLbl(self):
        if self.txtTelefono.text():
            self.lblTelefono.setText("Telefono")
        else:
            self.lblTelefono.setText("")


    def mostrarUsuLbl(self):
        if self.txtUsuario.text():
            self.lblUsuario.setText("Usuario")
        else:
            self.lblUsuario.setText("")


    def mostrarClvLbl(self):
        if self.txtClave.text():
            self.lblClave.setText("Contraseña")
        else:
            self.lblClave.setText("")


    def mostrarRClvLbl(self):
        if self.txtRptClave.text():
            self.lblRptClave.setText("Repetir Contraseña")
        else:
            self.txtRptClave.setText("")

        self.bttnRegistrar.clicked.connect(self.registrarPersona)
        self.bttnInsertarImg.clicked.connect(self.insertarImagen)


    def registrarPersona(self):
        # self.lblMensaje.setText("Has presionado el boton 'REGISTRARME' ...")

        if self.verificarCampos():
            self.lblMensaje.setText("todos los campos tienen información ...")
        else:
            self.lblMensaje.setText("* Debe llenar todos los campos...")


    def insertarImagen(self):
        nomArchivo = QFileDialog.getOpenFileName(self, "Añadir Imagen", "C:/Users/ASUS/Pictures", "Archivos de Imágenes (*.png *.jpg *.bmp)")

        if nomArchivo[0] != "":
            stamp = str(time.time())
            stamp = stamp[0:stamp.rfind(".")]
            self.nombreArchivo = nomArchivo[0]
            self.nombreArchivo = self.nombreArchivo.replace("\\", "/")
            self.nombreArchivo = self.nombreArchivo[self.nombreArchivo.rfind("/") + 1:]
            self.nombreArchivo = stamp + "_" + self.nombreArchivo
            self.lblMensaje.setText(nomArchivo[0] + ", " + self.nombreArchivo)
            self.lblImagen.setPixmap(QtGui.QPixmap(nomArchivo[0]))


    def verificarCampos(self):
        correcto = False

        if self.txtCorreo != "" and self.txtIdentificacion != "" and self.txtNombre != "" and self.txtApellido != "" and self.txtDireccion != "" and self.txtTelefono != "" and self.txtUsuario != "" and self.txtClave != "" and self.txtRptClave != "":
            correcto = True

        return correcto


app = QApplication(sys.argv)
dlgRegistrar = DlgRegistrar()
dlgRegistrar.show()
sys.exit(app.exec_())
