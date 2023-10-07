import pandas as pd
import numpy as np
import wx
import wx.xrc
import wx.adv
import wx.grid

from frame_template import MyFrame1 as Myframe

df = pd.read_csv("victoriaaccidents.csv")
accidentid = df['OBJECTID']
accidentdate = df['ACCIDENT_DATE']
accidenttime = df['ACCIDENT_TIME']
accidentday = df['DAY_OF_WEEK']
accidentalcohol = df['ALCOHOL_RELATED']

class GUIFrame(Myframe):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()

        self.grid = self.m_grid4

        self.display_data()

        # events
        self.m_button1.Bind(wx.EVT_BUTTON, self.on_filter_button_click)
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.on_checkbox_checked)

    # day choice
    def on_filter_button_click(self, event):
        selected_day = self.m_choice1.GetStringSelection()
        filtered_data = df[accidentday == selected_day]
        self.display_filtered_data(filtered_data)

    # alcohol related
    def on_checkbox_checked(self, event):
        is_checked = self.m_checkBox1.GetValue()

    def display_data(self):

        # reset the result
        self.clear_grid()

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

    def clear_grid(self):
        # remove rows
        self.grid.DeleteRows(0, self.grid.GetNumberRows())

    def display_filtered_data(self, data):
        # display filtered data
        self.display_data(data)

    # event
    def on_filter_button_click(self, event):
        # Get the selected day
        selected_day = self.m_choice1.GetStringSelection()
        # Get the checkbox value
        is_checked = self.m_checkBox1.GetValue()

        if is_checked:
            filtered_data = df[(accidentday == selected_day) & (accidentalcohol == 'Yes')]
        else:
            filtered_data = df[(accidentday == selected_day) & (accidentalcohol == 'No')]

        # Display the filtered data
        self.display_filtered_data(filtered_data)



    def display_filtered_data(self, filtered_data):
        # Clear the existing data in the grid
        self.grid.ClearGrid()

        # display
        for row_index, (id, date, time, day, alcohol) in enumerate(
                zip(filtered_data['OBJECTID'], filtered_data['ACCIDENT_DATE'],
                    filtered_data['ACCIDENT_TIME'], filtered_data['DAY_OF_WEEK'],
                    filtered_data['ALCOHOL_RELATED'])):
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

