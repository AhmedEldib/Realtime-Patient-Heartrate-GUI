import numpy as np
class Plot_Data(object):
    def __init__(self):

        self.Plot_Stop = 1

        self.GraphIsWav = 0

        self.Gmin = 0
        self.Gmax = 0

        self.data_X = []
        self.data_Y = []
        self.data_stop = 0
    
    def Stop(self):
        self.Plot_Stop = 1
    
    def Start(self):
        self.Plot_Stop = 0

    def Empty(self):
        self.data_X = []
        self.data_Y = []

    