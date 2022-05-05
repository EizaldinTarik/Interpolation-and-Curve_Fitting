
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import plot
from pyqtgraph import PlotWidget
import numpy as np
from scipy.fftpack import fft
import math
import pandas as pd
import pyqtgraph as pg
matplotlib.use('Qt5Agg')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 1096)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        #self.PlotWidget = QtWidgets.QWidget(self.frame)
        self.PlotWidget = PlotWidget(self.frame)
        self.PlotWidget.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.PlotWidget.setObjectName("PlotWidget")
        self.gridLayout.addWidget(self.PlotWidget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.ErrorMapWidget = QtWidgets.QWidget(self.frame)
        self.ErrorMapWidget.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.ErrorMapWidget.setObjectName("ErrorMapWidget")
        self.gridLayout.addWidget(self.ErrorMapWidget, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.labelForEquation = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelForEquation.setFont(font)
        self.labelForEquation.setStyleSheet("background-color: rgb(163, 163, 163);\n"
"color: rgb(50, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.labelForEquation.setObjectName("labelForEquation")
        self.gridLayout_4.addWidget(self.labelForEquation, 0, 0, 1, 1)
        self.spinBox_For_ErrorPercenatge = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_For_ErrorPercenatge.setObjectName("spinBox_For_ErrorPercenatge")
        self.gridLayout_4.addWidget(self.spinBox_For_ErrorPercenatge, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(754, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelForNumberOfChunks = QtWidgets.QLabel(self.centralwidget)
        self.labelForNumberOfChunks.setObjectName("labelForNumberOfChunks")
        self.gridLayout_3.addWidget(self.labelForNumberOfChunks, 0, 0, 1, 1)
        self.horizontalSliderFor_chunks = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_chunks.setMaximum(10)
        self.horizontalSliderFor_chunks.setPageStep(1)
        self.horizontalSliderFor_chunks.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_chunks.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_chunks.setObjectName("horizontalSliderFor_chunks")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_chunks, 0, 1, 1, 1)
        self.labelOfNumberOfFittingOrder = QtWidgets.QLabel(self.centralwidget)
        self.labelOfNumberOfFittingOrder.setObjectName("labelOfNumberOfFittingOrder")
        self.gridLayout_3.addWidget(self.labelOfNumberOfFittingOrder, 1, 0, 1, 1)
        self.horizontalSliderFor_FittingOrder = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_FittingOrder.setMaximum(10)
        self.horizontalSliderFor_FittingOrder.setPageStep(1)
        self.horizontalSliderFor_FittingOrder.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_FittingOrder.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_FittingOrder.setObjectName("horizontalSliderFor_FittingOrder")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_FittingOrder, 1, 1, 1, 1)
        self.labelForEfficacy = QtWidgets.QLabel(self.centralwidget)
        self.labelForEfficacy.setObjectName("labelForEfficacy")
        self.gridLayout_3.addWidget(self.labelForEfficacy, 2, 0, 1, 1)
        self.horizontalSliderFor_Effeciacy = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_Effeciacy.setMaximum(10)
        self.horizontalSliderFor_Effeciacy.setPageStep(1)
        self.horizontalSliderFor_Effeciacy.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_Effeciacy.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_Effeciacy.setObjectName("horizontalSliderFor_Effeciacy")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_Effeciacy, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_X_axis.setObjectName("label_X_axis")
        self.gridLayout_2.addWidget(self.label_X_axis, 0, 0, 1, 1)
        self.comboBox_X_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_X_axis.setEditable(False)
        self.comboBox_X_axis.setCurrentText("")
        self.comboBox_X_axis.setObjectName("comboBox_X_axis")
        self.comboBox_X_axis.addItem("")
        self.comboBox_X_axis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_X_axis, 0, 1, 1, 1)
        self.label_FitMethodFor_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_X_axis.setObjectName("label_FitMethodFor_X_axis")
        self.gridLayout_2.addWidget(self.label_FitMethodFor_X_axis, 0, 2, 1, 1)
        self.lineEdit_For_x_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_x_axis.setObjectName("lineEdit_For_x_axis")
        self.gridLayout_2.addWidget(self.lineEdit_For_x_axis, 0, 3, 1, 1)
        self.label_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_Y_axis.setObjectName("label_Y_axis")
        self.gridLayout_2.addWidget(self.label_Y_axis, 1, 0, 1, 1)
        self.comboBox_Y_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Y_axis.setEditable(False)
        self.comboBox_Y_axis.setCurrentText("")
        self.comboBox_Y_axis.setFrame(True)
        self.comboBox_Y_axis.setModelColumn(0)
        self.comboBox_Y_axis.setObjectName("comboBox_Y_axis")
        self.comboBox_Y_axis.addItem("")
        self.comboBox_Y_axis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Y_axis, 1, 1, 1, 1)
        self.label_FitMethodFor_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_Y_axis.setObjectName("label_FitMethodFor_Y_axis")
        self.gridLayout_2.addWidget(self.label_FitMethodFor_Y_axis, 1, 2, 1, 1)
        self.lineEdit_For_y_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_y_axis.setObjectName("lineEdit_For_y_axis")
        self.gridLayout_2.addWidget(self.lineEdit_For_y_axis, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_For_GenerateErrorMap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_GenerateErrorMap.setObjectName("pushButton_For_GenerateErrorMap")
        self.verticalLayout.addWidget(self.pushButton_For_GenerateErrorMap)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_For_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Open.setObjectName("pushButton_For_Open")
        self.horizontalLayout.addWidget(self.pushButton_For_Open)
        self.pushButton_For_Plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Plot.setObjectName("pushButton_For_Plot")
        self.horizontalLayout.addWidget(self.pushButton_For_Plot)
        self.pushButton_For_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Delete.setObjectName("pushButton_For_Delete")
        self.horizontalLayout.addWidget(self.pushButton_For_Delete)
        self.pushButton_For_spare_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_3.setObjectName("pushButton_For_spare_3")
        self.horizontalLayout.addWidget(self.pushButton_For_spare_3)
        self.pushButton_For_spare_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_5.setObjectName("pushButton_For_spare_5")
        self.horizontalLayout.addWidget(self.pushButton_For_spare_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 1, 1, 3)
        self.labelForErrorPercentage = QtWidgets.QLabel(self.centralwidget)
        self.labelForErrorPercentage.setStyleSheet("background-color: rgb(163, 163, 163);\n"
"color: rgb(50, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.labelForErrorPercentage.setObjectName("labelForErrorPercentage")
        self.gridLayout_4.addWidget(self.labelForErrorPercentage, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_X_axis.setCurrentIndex(-1)
        self.comboBox_Y_axis.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_For_Open.clicked.connect(self.Open_file)


    def Open_file(self):
        self.PlotWidget.clear()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open csv', QtCore.QDir.rootPath(), 'csv(*.csv)')
        data_set = pd.read_csv(fileName, header=None)
        plot(data_set)
        self.Save_signal(data_set[0], data_set[1])

    def Save_signal(self, time, Amplitude):
        self.data_amplitude = Amplitude
        self.data_time = time
        self.plot_mainGraph(self.data_amplitude, self.data_time, 0)

    def plot_mainGraph(self, amplitude, time, Fs):
        self.pink_pen = pg.mkPen((255, 0, 255), width=1)
        self.PlotWidget.plotItem.vb.setLimits(xMin=min(time) - 0.01, xMax=max(time), yMin=min(amplitude) - 0.2,
                                                     yMax=max(amplitude) + 0.2)
        if Fs == 0:
            self.PlotWidget.clear()
            self.PlotWidget.plot(time, amplitude)
        else:
            sample_time = 1 / Fs
            no_of_samples = math.ceil(max(time)) / sample_time    ##Getting number of samples as a float number
            no_of_samples = math.ceil(no_of_samples)              ##Getting number of samples as an int number

            index_append = len(time) / no_of_samples
            index_append = math.floor(index_append)
            self.Sample_amp = []
            self.Sample_time = []
            index = 0
            for i in range(no_of_samples):
                self.Sample_time.append(time[index])           ##adding the index of point time
                self.Sample_amp.append(amplitude[index])       ##adding the index of point amplitude
                index += index_append

            self.recons_amp = self.sinc_interp(self.Sample_amp, self.Sample_time, time)  ##plotting the new points

            self.PlotWidget.clear()
            #self.signalWidget2_ilustrator.clear()
            self.PlotWidget.plot(time, amplitude)
            self.PlotWidget.plot(self.Sample_time, self.Sample_amp, symbol='o', pen=None)
            self.PlotWidget.plot(time, self.recons_amp, pen=self.pink_pen)
            #self.signalWidget2_ilustrator.plot(time, self.recons_amp, pen=self.pink_pen)
            #self.signalWidget2_ilustrator.plotItem.vb.setLimits(xMin=min(self.data_time) - 0.01,
             #                                                   xMax=max(self.data_time),
              #                                                  yMin=min(self.data_amplitude) - 0.2,
               #                                                 yMax=max(self.data_amplitude) + 0.2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelForEquation.setText(_translate("MainWindow", "Equation to be here"))
        self.labelForNumberOfChunks.setText(_translate("MainWindow", "Number of Chuncks"))
        self.labelOfNumberOfFittingOrder.setText(_translate("MainWindow", "Fitting order"))
        self.labelForEfficacy.setText(_translate("MainWindow", "Efficency"))
        self.label_X_axis.setText(_translate("MainWindow", "X-axis"))
        self.comboBox_X_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_X_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_FitMethodFor_X_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.label_Y_axis.setText(_translate("MainWindow", "Y-axis"))
        self.comboBox_Y_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_Y_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_FitMethodFor_Y_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.pushButton_For_GenerateErrorMap.setText(_translate("MainWindow", "Generate Error map"))
        self.pushButton_For_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_For_Plot.setText(_translate("MainWindow", "Plot"))
        self.pushButton_For_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_For_spare_3.setText(_translate("MainWindow", "Spare"))
        self.pushButton_For_spare_5.setText(_translate("MainWindow", "Spare"))
        self.labelForErrorPercentage.setText(_translate("MainWindow", "Error Percentage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
