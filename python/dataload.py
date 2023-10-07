import pandas as pd
import wx
from frame_template import MyFrame1 as Myframe
df = pd.read_csv("victoriaaccidents.csv")
accidentid = df['OBJECTID']
accidentdate = df['ACCIDENT_DATE']
accidenttime = df['ACCIDENT_TIME']
accidentday = df['DAY_OF_WEEK']
accidentalcohol = df['ALCOHOLTIME']

class GUIFrame (Myframe):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()



if __name__ == "__main__":
    app = wx.App()
    frame = GUIFrame(None)
    frame.Show()
    app.MainLoop()

