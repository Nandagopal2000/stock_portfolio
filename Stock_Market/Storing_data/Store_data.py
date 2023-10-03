from Access_Data.Data import Recived_Data
import openpyxl
# import pandas as pd
data = Recived_Data()
# data = Recived_Data()
Symbol = input()
# Series = input()

print(data.Get_stock_info_show(Symbol))

# print(data.Get_stock_value('infy'))
# print(data.Get_Stock_List_Nifty_200())

# New_Data1 = data.Get_Historical_data_OneMonth(Symbol, Series)
# excel_path = "historical_data_month.xlsx"
# New_Data1.to_excel(excel_path, index=False)

# New_Data2 = data.Get_Historical_data_Particular_Month(Symbol, Series, 2023, 3)
# excel_path = "historical_data_particular_month.xlsx"
# New_Data2.to_excel(excel_path, index=False)

# New_Data3 = data.Get_Historical_data_OneYear(Symbol, Series)
# excel_path = "historical_data_year.xlsx"
# New_Data3.to_excel(excel_path, index=False)

# New_Data4 = data.Get_Historical_data_Particular_Day(Symbol, Series, 2023, 8, 18)
# excel_path = "historical_data_particular_day.xlsx"
# New_Data4.to_excel(excel_path, index=False)

# print(data.Get_SME_Stock_List())

# New_Data3 = data.Get_Historical_data_OneYear(Symbol, Series)
# excel_path = "historical_data_year.xlsx"
# New_Data3.to_excel(excel_path, index=False)




