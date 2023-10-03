import requests
from .NSE_API import NSE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Stock,StockAccount,StockTransaction,MonthlyPortfolioStatus,MonthlyPortfolioStockStatus,Holdings,User
from .forms import StockSymbolForm, StockAccountForm



# Create your views here.

def home(request):
    return render(request, 'base/home.html')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does not Exist.')

        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page' : page}
    return render(request, 'base/login_register.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registartion')

    context = {'form' : form}
    return render(request, 'base/login_register.html', context)


def stockDetails(request):
    if request.method == "POST":
        form1 = StockSymbolForm(request.POST)
        if form1.is_valid():
            stock_symbol = form1.cleaned_data['stock_symbol']
            nse = NSE()
            data = nse.get_quote_data(stock_symbol)

            company_name = data.get('info')['companyName']
            industry = data.get('industryInfo')['industry']
            sector = data.get('industryInfo')['sector']

            stock = Stock(stock_symbol=stock_symbol,
                          company_name=company_name,
                          industry=industry,
                          sector=sector)
            stock.save()
    else:
        form1 = StockSymbolForm()

    datas = Stock.objects.all()
    return render(request, 'base/stock.html', {'form1' : form1, 'datas' : datas})


def create_stock_account(request):
    if request.method == 'POST':
        form = StockAccountForm(request.POST)
        if form.is_valid():
            stock_account = form.save(commit=False)
            stock_account.user = request.user
            stock_account.save()
    else:
        form = StockAccountForm()
    
    return render(request, 'base/stock.html', {'form':form})