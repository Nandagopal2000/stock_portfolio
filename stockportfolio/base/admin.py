from django.contrib import admin
from .models import Stock, User, StockAccount, Holdings, StockTransaction, MonthlyPortfolioStatus, MonthlyPortfolioStockStatus

# Register your models here.

admin.site.register(Stock)
admin.site.register(User)
admin.site.register(StockAccount)
admin.site.register(Holdings)
admin.site.register(StockTransaction)
admin.site.register(MonthlyPortfolioStatus)
admin.site.register(MonthlyPortfolioStockStatus)