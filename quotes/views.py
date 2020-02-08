#houses the functions that intake requests and return the webpages requested

from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
# pk_3a855ded1b8a49a292785f1fc30d03e9 IEX cloud public API key

def home(request):
    import requests
    import json

    if request.method == 'POST' : #standard practice to use POST method instead of get
        ticker = request.POST['ticker'] #variable = request.POST['name of input box']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3a855ded1b8a49a292785f1fc30d03e9")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html',{'api': api})

    else:
        return render(request, 'home.html',{'ticker': "Enter Ticker Symbol Above"})

def about(request):
    return render(request, 'about.html',{})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST' :
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
        return redirect('add_stock')
    else: 
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_3a855ded1b8a49a292785f1fc30d03e9")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

    return render(request, 'add_stock.html',{'ticker': ticker, 'output' : output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect('add_stock')