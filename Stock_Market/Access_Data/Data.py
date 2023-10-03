from Recived_data.nse import NSE
from datetime import date, timedelta, datetime
import json
import nsepython
import calendar

class Recived_Data():

    def __init__(self):
        self.nse = NSE()

    def Get_stock_info_show(self, symbol):
        symbol = symbol.upper()
        Quote = self.nse.get_quote_data(symbol)
        data_found1 = Quote['priceInfo']['intraDayHighLow']['value']
        data_found2 = Quote['info']['companyName']
        return "Symbol : {0}, Value : {1}, CompanyName : {2}".format(symbol, data_found1, data_found2)
        # return Quote

        # Stock_name = input("Enter The Stock Name : ").upper()
        # print(Get_stock_info(Stock_name))

    def Get_stock_value(self, symbol):
        symbol = symbol.upper()
        Quote = self.nse.get_quote_data(symbol)
        data_found1 = Quote['priceInfo']['intraDayHighLow']['value']
        # data_found2 = Quote['info']['companyName']
        return data_found1

    def Get_Stock_List_Nifty_200(self):
        all_contract = self.nse.get_all_stocks()
        data = all_contract['data']
        for i in data:
            if i['priority'] == 1:
                print(None)
            else:
                company_Symbol = i['meta']['symbol']    # symbols
                company_Name = i['meta']['companyName']     # companyName
                print("{0} :\t{1}".format(company_Name, company_Symbol))
        return len(data)

        # print(Get_Stock_List())

    def Get_SME_Stock_List(self):
        all_contract = self.nse.get_SME_market_stocks()
        data = all_contract['data']
        for i in data:
            company_Symbol = i['symbol']  # symbols
            last_Price = i['lastPrice']  # companyName
            print("{0} :\t{1}".format(company_Symbol, last_Price))
        return len(data)

    def Get_Historical_data_OneMonth(self, Stock_Symbol, Stock_Series):
        # Making One Month TimeStamps using timedelta
        current_date = date.today()
        one_month_delta = timedelta(days=30)
        new_date = current_date - one_month_delta

        # using Upper in-built function to make Capital_Letters
        Stock_Symbol1 = Stock_Symbol.upper()
        Stock_Series1 = Stock_Series.upper()

        # Getting the data of one month of a particular stock and returning into a dataframe
        Historical_data = self.nse.getHistoricalData_Of_OneYear(Stock_Symbol1, Stock_Series1, new_date, current_date)
        return Historical_data

        # Stock_Symbol = input("Enter The Stock Symbol : ").upper()
        # Stock_Series = input("Enter The Stock Series('EQ' or 'SM') : ").upper()
        # print(Get_Historical_data(Stock_Symbol, Stock_Series))

    def Get_Historical_data_OneYear(self, Stock_Symbol, Stock_Series):
        # Making One Month TimeStamps using timedelta
        current_date = date.today()
        one_year_delta = timedelta(days=365)
        new_date = current_date - one_year_delta

        # using Upper in-built function to make Capital_Letters
        Stock_Symbol1 = Stock_Symbol.upper()
        Stock_Series1 = Stock_Series.upper()

        # Getting the data of one month of a particular stock and returning into a dataframe
        Historical_data = self.nse.getHistoricalData_Of_OneYear(Stock_Symbol1, Stock_Series1, new_date, current_date)
        return Historical_data

    def Get_Historical_data_Particular_Month(self, Stock_Symbol, Stock_Series, Year, Month):
        first_day_of_month = datetime(year=Year, month=Month, day=1)
        month_name = first_day_of_month.strftime("%B")
        days_in_month = (first_day_of_month.replace(month=Month+1) - first_day_of_month).days
        weedkday_of_first_day = first_day_of_month.strftime("%A")

        Stock_Symbol1 = Stock_Symbol.upper()
        Stock_Series1 = Stock_Series.upper()

        Historical_data = self.nse.getHistoricalData_Of_OneYear(Stock_Symbol1, Stock_Series1, first_day_of_month, datetime(year=Year, month=Month, day=days_in_month))
        return Historical_data

    def Get_Historical_data_Particular_Day(self, Stock_Symbol, Stock_Series, Year, Month, Day):
        Exact = datetime(year=Year, month=Month, day=Day)
        Exact_day = Exact.strftime("%A")

        if Exact_day == "Saturday" or Exact_day == "Sunday":
            return "No data on Weekends"
        else:
            Stock_Symbol1 = Stock_Symbol.upper()
            Stock_Series1 = Stock_Series.upper()

            Historical_data = self.nse.getHistoricalData_Of_OneYear(Stock_Symbol1, Stock_Series1, Exact, Exact)
            return Historical_data

# nse = NSE()
# Historical_data = nse.getHistoricalData('SUZLON', 'EQ', date(2023, 7, 17), date(2023, 8, 17))
# print(Historical_data)
#
# nse = NSE()
# symbol = input("Enter The Symbol of Equity : ").upper()
# Quote = nse.get_quote_data(symbol)
# data_found = Quote['priceInfo']['intraDayHighLow']['value']
# print("Symbol : {0}, Value : {1}".format(symbol, data_found))
#
# nse = NSE()
# all_contract = nse.get_all_stocks()
# data = all_contract['data']
# count = 0
# for i in data:
#     print(i['symbol'])     # symbols
#     count += 1
# print(count)  # 200 stocks count

# nse = NSE()
# all_contract = nse.get_SME_market_stocks()
# data = all_contract['data']
# count = 0
# for i in data:
#     print(i['symbol'])     # symbols
#     count += 1
# print(count)    # 192 stock count
#
# print(count)  # 200 stocks count
