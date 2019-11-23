from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from motionToolUI import Ui_MainWindow
import sys

# headArray = ["headPitchBox", "headYawBox"]
# shoulderRightArray = ["elbowPitchRightBox", "shoulderRollRightBox", "shoulderPitchRightBox"]
# shoulderLeftArray = ["elbowPitchLeftBox", "shoulderRollLeftBox", "shoulderPitchLeftBox"]
# hipRightArray = ["hipPitchRightBox", "hipRollRightBox", "hipYawRightBox"]
# hipLeftArray = ["hipPitchLeftBox", "hipRollLeftBox", "hipYawLeftBox"]
# kneeRight = ["kneePitchRightBox"]
# kneeLeft = ["kneePitchLeftBox"]
# ankleLeft = ["ankleRollLeftBox", "anklePitchLeftBox"]
# ankleRight = ["ankleRollRightBox", "anklePitchRightBox"]

motorNamesArray = ["headPitchBox", "headYawBox",
"elbowPitchRightBox", "shoulderRollRightBox", "shoulderPitchRightBox",
"elbowPitchLeftBox", "shoulderRollLeftBox", "shoulderPitchLeftBox", 
"hipPitchRightBox", "hipRollRightBox", "hipYawRightBox", "hipPitchLeftBox", 
"hipRollLeftBox", "hipYawLeftBox", 
"kneePitchRightBox", 
"kneePitchLeftBox", 
"ankleRollLeftBox", "anklePitchLeftBox", 
"ankleRollRightBox", "anklePitchRightBox"]

class motionToolWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(motionToolWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons 
        self.clearButton = self.findChild(QtWidgets.QPushButton, 'clearButton')
        self.clearButton.clicked.connect(self.clearButtonClicked) 

        self.setButton = self.findChild(QtWidgets.QPushButton, 'setButton')
        self.setButton.clicked.connect(self.setButtonClicked) 
        
        self.pos0Button = self.findChild(QtWidgets.QPushButton, 'pos0Button')
        self.pos0Button.clicked.connect(self.pos0ButtonClicked) 


        self.show()


    def clearButtonClicked(self):

        print('clear Button Clicked')
        global motorNamesArray
        for motorNamesArray in motorNamesArray:
            # print(motorNamesArray)
            self.headPitchBox = self.findChild(QtWidgets.QDoubleSpinBox, motorNamesArray)
            self.headPitchBox.setValue(0.0)
            
        _set()

    def setButtonClicked(self):
        print('set Button Clicked')


    def pos0ButtonClicked(self):
        print('pos0 Button Clicked')


def get():
    print("get func called")

def _set():
    print("_set func called")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = motionToolWindow()
    application.show()
    sys.exit(app.exec())