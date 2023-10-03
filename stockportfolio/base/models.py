from django.db import models
from decimal import Decimal
from django.db.models import F, ExpressionWrapper, DecimalField
# Create your models here.


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_symbol = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)

    class Meta:
        db_table = 'Stock'

    def __str__(self):
        return self.stock_symbol
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=225)
    password_hash = models.CharField(max_length=225)
    last_login_date = models.DateTimeField(auto_now=True,null=True)
    registration_date = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username

class StockAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=225)

    class Meta:
        db_table = 'StockAccount'

    def __str__(self):
        return self.account_name
    
class Holdings(models.Model):
    holding_id = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    total_invested_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    account = models.ForeignKey(StockAccount, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Holdings'

    def __str__(self):
        return f"{self.account}"

class MonthlyPortfolioStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    YEAR_CHOICES = [(year, year) for year in range(2000, 2100)]
    year = models.IntegerField(choices=YEAR_CHOICES,null=True)

    MONTH_CHOICES = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec'),
    )
    month = models.IntegerField(choices=MONTH_CHOICES,null=True)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_market_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_profit_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    

    class Meta:
        db_table = 'MonthlyPortfolioStatus'

    def __str__(self):
        return f"{self.year} / {self.month}"
    
# MONTH_CHOICES = (
#         (1, 'Jan'),
#         (2, 'Feb'),
#         (3, 'Mar'),
#         (4, 'Apr'),
#         (5, 'May'),
#         (6, 'Jun'),
#         (7, 'Jul'),
#         (8, 'Aug'),
#         (9, 'Sep'),
#         (10, 'Oct'),
#         (11, 'Nov'),
#         (12, 'Dec'),
#     )

#     month = models.IntegerField(choices=MONTH_CHOICES, null=True)
    
class MonthlyPortfolioStockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market_value = models.DecimalField(max_digits=10, decimal_places=2)
    invested_value = models.DecimalField(max_digits=10, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    account = models.ForeignKey(StockAccount, on_delete=models.CASCADE)

    YEAR_CHOICES = [(year, year) for year in range(2000, 2100)]
    year = models.IntegerField(choices=YEAR_CHOICES, null=True)

    MONTH_CHOICES = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec'),
    )
    month = models.IntegerField(choices=MONTH_CHOICES, null=True)

    class Meta:
        db_table = 'MonthlyPortfolioStockStatus'

    def __str__(self):
        return f"{self.stock} - {self.year}/{self.month}"



class StockTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(StockAccount, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField()
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2)
    total_transaction_amount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'StockTransaction'

    def __str__(self):
        return f"{self.account} / {self.stock}"