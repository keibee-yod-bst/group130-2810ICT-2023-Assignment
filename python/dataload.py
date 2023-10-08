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
description = df['ACCIDENT_TYPE']



class GUIFrame(Myframe):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()

        self.grid = self.m_grid4

        # min & max date
        min_date = pd.to_datetime(df['ACCIDENT_DATE'], dayfirst=True).min()
        max_date = pd.to_datetime(df['ACCIDENT_DATE'], dayfirst=True).max()


        self.display_data()

        # events
        self.m_button1.Bind(wx.EVT_BUTTON, self.on_filter_button_click)
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.on_checkbox_checked)

        # original date on wxDatePicker (min & max)
        self.m_datePicker2.SetValue(wx.DateTime(min_date.day, min_date.month - 1, min_date.year))
        self.m_datePicker1.SetValue(wx.DateTime(max_date.day, max_date.month - 1, max_date.year))

    # Search description
    def on_search(self, event):
        # Get the search keyword entered by the user
        search_keyword = self.m_searchCtrl2.GetValue()

        # Update the filtered data based on the search keyword
        self.filtered_data = df[description.str.contains(search_keyword, case=False)]

        # Apply other filters
        self.filter_data()

    # alcohol related
    def on_checkbox_checked(self, event):
        is_checked = self.m_checkBox1.GetValue()

    def display_data(self, search_keyword=None):
        # Reset the grid
        self.clear_grid()

        # Filter data based on the search keyword (if provided)
        if search_keyword:
            filtered_data = df[df['ACCIDENT_TYPE'].str.contains(search_keyword, case=False)]
        else:
            filtered_data = df

        for row_index, (id, date, time, day, alcohol, description) in enumerate(
                zip(accidentid, accidentdate, accidenttime, accidentday, accidentalcohol, description)):
            if row_index < self.grid.GetNumberRows():
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))
                self.grid.SetCellValue(row_index, 5, str(description))
            else:
                self.grid.AppendRows(1)
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))
                self.grid.SetCellValue(row_index, 5, str(description))

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

        # Get period
        start_date = self.m_datePicker2.GetValue()
        end_date = self.m_datePicker1.GetValue()

        # extract day, month, and year components
        start_day = start_date.GetDay()
        start_month = start_date.GetMonth() + 1  # Month is 0-based, so add 1
        start_year = start_date.GetYear()

        end_day = end_date.GetDay()
        end_month = end_date.GetMonth() + 1
        end_year = end_date.GetYear()

        # DD/MM/YYYY format
        start_date_str = f"{start_day:02d}/{start_month:02d}/{start_year:04d}"
        end_date_str = f"{end_day:02d}/{end_month:02d}/{end_year:04d}"

        #print("Selected Start Date:", start_date_str)
        #print("Selected End Date:", end_date_str)

        # filter the data for the selected period
        selected_period = df[
            (pd.to_datetime(df['ACCIDENT_DATE'], dayfirst=True) >= pd.to_datetime(start_date_str, dayfirst=True)) &
            (pd.to_datetime(df['ACCIDENT_DATE'], dayfirst=True) <= pd.to_datetime(end_date_str, dayfirst=True))
            ]

        if is_checked:
            filtered_data = selected_period[selected_period['ALCOHOL_RELATED'] == 'Yes']
        else:
            filtered_data = selected_period[selected_period['ALCOHOL_RELATED'] == 'No']

        # further filter by day
        filtered_data = filtered_data[filtered_data['DAY_OF_WEEK'] == selected_day]

        # display the filtered data
        self.display_filtered_data(filtered_data)


    def display_filtered_data(self, filtered_data):
        # Clear the existing data in the grid
        self.grid.ClearGrid()

        # display
        for row_index, (id, date, time, day, alcohol, description) in enumerate(
                zip(filtered_data['OBJECTID'], filtered_data['ACCIDENT_DATE'],
                    filtered_data['ACCIDENT_TIME'], filtered_data['DAY_OF_WEEK'],
                    filtered_data['ALCOHOL_RELATED'], df['ACCIDENT_TYPE'])):
            if row_index < self.grid.GetNumberRows():
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))
                self.grid.SetCellValue(row_index, 5, str(description))
            else:
                self.grid.AppendRows(1)
                self.grid.SetCellValue(row_index, 0, str(int(id)))
                self.grid.SetCellValue(row_index, 1, date)
                self.grid.SetCellValue(row_index, 2, time)
                self.grid.SetCellValue(row_index, 3, str(day))
                self.grid.SetCellValue(row_index, 4, str(alcohol))
                self.grid.SetCellValue(row_index, 5, str(description))


if __name__ == "__main__":
    app = wx.App()
    frame = GUIFrame(None)
    frame.Show()
    app.MainLoop()
