from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas.listaparticula import ListP
from particulas.particula import Particle

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.myListP = ListP()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_pushButton.clicked.connect(self.click_agregar)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        self.ui.out_plainTextEdit.clear()
        self.ui.out_plainTextEdit.insertPlainText(str(self.myListP))

    @Slot()
    def click_agregar(self):
        myDestinX = self.ui.destinyX_spinBox.value()
        myDestinY = self.ui.destinyY_spinBox.value()
        mySpeed = self.ui.speed_spinBox.value()
        myRed = self.ui.red_spinBox.value()
        myGreen = self.ui.green_spinBox.value()
        myBlue = self.ui.blue__spinBox.value()

        myParticle = Particle(myDestinX,myDestinY,mySpeed,myRed,myGreen,myBlue)
        self.myListP.add_end(myParticle)