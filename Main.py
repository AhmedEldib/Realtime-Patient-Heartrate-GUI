from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from pyqtgraph import PlotWidget, plot, PlotItem
import pyqtgraph as pg
from PyQt5 import QtCore

import sys  # We need sys so that we can pass argv to QApplication
from random import randint
import numpy as np
from utility_class import Plot_Data

from serial.serialwin32 import Serial 
import time


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()

        #intialize memebers of class plot_data that contains all the functions
        #and the variables needed for plotting to avoid repeativness
        self.Ugraph_1 = Plot_Data()


        #Empty arrays used in singular-import function
        self.Empty_X = []
        self.Empty_Y = []

        #Toggles for the exception handling of pressing start button and crashing before any graph is drawn, used in import
        self.HasEntered1stView = 0


        pg.setConfigOption('background', 'w')

        self.ui.setupUi(self)

        self.ui.StartButton.clicked.connect(self.Startplot)

        self.ui.StopButton.clicked.connect(self.Stop_1)

        self.ui.HideButton.clicked.connect(self.Hide)

        self.ui.ExitButton.clicked.connect(self.Exit)

        self.ui.EmptyButton.clicked.connect(self.Empty)
        

    def Plot_1(self):
        if self.Ugraph_1.Plot_Stop == 1 and self.HasEntered1stView == 1:
            self.Ugraph_1.Start()
            self.Startplot()
        elif self.HasEntered1stView == 1: 
            self.Ugraph_1.Start()   


    def Stop_1(self):
        self.Ugraph_1.Stop()


    def Graph1(self):
        #print(self.Ugraph_1.data_Y)
        #(self.Ugraph_1.data_X)
        
        self.ui.GraphicsView.plot(self.Ugraph_1.data_X, self.Ugraph_1.data_Y, pen='r')
        
        if len(self.Ugraph_1.data_X) > 2:
            self.ui.GraphicsView.setXRange(self.Ugraph_1.data_X[-1] - (self.Ugraph_1.data_X[1] - self.Ugraph_1.data_X[0]) * 100, self.Ugraph_1.data_X[-1])
            min_y = np.amin(self.Ugraph_1.data_Y)
            max_y = np.amax(self.Ugraph_1.data_Y)
            self.ui.GraphicsView.plotItem.getViewBox().setLimits(xMin=self.Ugraph_1.data_X[0], xMax=self.Ugraph_1.data_X[-1], yMin=min_y - min_y * 0.1, yMax=max_y + max_y * 0.1)
        
        QtCore.QCoreApplication.processEvents()
        #self.Ugraph_1.data_stop = self.Ugraph_1.data_stop + 10S
        # if self.Ugraph_1.data_stop >= len(self.Ugraph_1.data_X):
        #     self.Ugraph_1.data_stop = 0
        #     self.Ugraph_1.Stop()


    def Hide(self):
        self.Ugraph_1.Stop()
        self.ui.GraphicsView.clear()


    def Empty(self):
        self.Hide()
        self.Ugraph_1.Empty()

        self.HasEntered1stView = 0
        self.Ugraph_1.GraphIsWav = 0

    def Startplot(self):
        self.Ugraph_1.Plot_Stop = 0
        self.getdatafromserial()
             

    def getdatafromserial(self):
        

            threshold =514.0
            oldvalue = 0
            newvalue = 0

            reading123=0
            oldmillis = 0
            newmillis = 0
            timings= [0]*16

            self.HasEntered1stView = 1


            #insert ur COM here
            ser = Serial('COM15') 
            ser.flushInput()

            while self.Ugraph_1.Plot_Stop == 0:
                try:
                    ser_bytes = ser.readline()
                    decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                except:
                    print("Keyboard Interrupt")
                    break

                oldvalue = newvalue
                newvalue=0

                for i in range(16): # Average over 16 measurements
                    newvalue += decoded_bytes

                newvalue=newvalue/16
                
                self.Ugraph_1.data_X.append(reading123) #self.Ugraph_1.data_X.append((time.strftime("%H:%M:%S", time.localtime()))) #np.append(self.Ugraph_1.data_X,((time.strftime("%H:%M:%S", time.localtime()))))  
                reading123+=1
                self.Ugraph_1.data_Y.append(newvalue) #np.append(self.Ugraph_1.data_Y,newvalue) 
                self.Graph1()

                # find triggering edge
                if oldvalue<threshold and newvalue>=threshold: 
                    oldmillis = newmillis
                    newmillis = time.time()*1000
                    # fill in the current time difference  a ringbuffer
                    timings.append((int)(newmillis-oldmillis))
                    if len(timings)>16:
                        timings.pop(0)           #filling queue of time differences
                    totalmillis = 0
                    # calculate average of the last 16 time differences
                    for i in range(16):
                        totalmillis += timings[i]

                    # calculate heart rate
                    heartrate = 60000//(totalmillis/16)
                    

                    if heartrate>40 and heartrate<130:
                        print(heartrate)
                    else:
                        print("Measuring Heart rate")

                QtCore.QCoreApplication.processEvents()
                
                


        
    def Exit(self):
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
