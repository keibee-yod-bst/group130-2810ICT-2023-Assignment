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
        # Get the selected day of the week from the choice control
        selected_day = self.m_choice1.GetStringSelection()

        # Filter the DataFrame based on the selected day
        filtered_data = df[df['DAY_OF_WEEK'] == selected_day]

        # Display the filtered data in the grid
        self.display_filtered_data(filtered_data)

    # alcohol related
    def on_checkbox_checked(self, event):
        # Check the state of the checkbox
        is_checked = self.m_checkBox1.GetValue()

        # Filter the DataFrame based on the checkbox state (ALCOHOL_RELATED == 'Yes' or 'No')
        if is_checked:
            filtered_data = df[df['ALCOHOL_RELATED'] == 'Yes']
        else:
            filtered_data = df[df['ALCOHOL_RELATED'] == 'No']

        # Display the filtered data in the grid
        self.display_filtered_data(filtered_data)

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
        # remove all rows from the grid
        self.grid.DeleteRows(0, self.grid.GetNumberRows())

    def display_filtered_data(self, data):
        # Display the filtered data in the grid
        self.display_data(data)

    def on_filter_button_click(self, event):
        # Get the selected day of the week from the choice control
        selected_day = self.m_choice1.GetStringSelection()

        # Filter the DataFrame based on the selected day
        filtered_data = df[df['DAY_OF_WEEK'] == selected_day]

        # Display the filtered data in the grid
        self.display_filtered_data(filtered_data)

        # Display the filtered data in your grid or another part of your GUI
        self.display_filtered_data(filtered_data)

    def display_filtered_data(self, filtered_data):
        # Clear the existing data in the grid
        self.grid.ClearGrid()

        # Display the filtered data in the grid
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

