import pandas as pd
import wx
from frame_template import MyFrame1 as Myframe
df = pd.read_csv("victoriaaccidents.csv")
accidentid = df['OBJECTID']
accidentdate = df['ACCIDENT_DATE']
accidenttime = df['ACCIDENT_TIME']
accidentday = df['DAY_OF_WEEK']
accidentalcohol = df['ALCOHOLTIME']

class GUIFrame(Myframe):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()


        self.grid = self.m_grid4


        self.display_data()

    def display_data(self):
        for row_index, (id, date, time, day, alcohol) in enumerate(
                zip(accidentid, accidentdate, accidenttime, accidentday, accidentalcohol)):
            if row_index < self.grid.GetNumberRows():
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))
            else:
                self.grid.AppendRows(1)
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))



if __name__ == "__main__":
    app = wx.App()
    frame = GUIFrame(None)
    frame.Show()
    app.MainLoop()

