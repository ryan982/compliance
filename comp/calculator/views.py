from django.shortcuts import render
from django.http import HttpResponse
from .forms import Calculate
# Create your views here.

def calculator(request):
    if request.method == "POST":
        form =Calculate(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            gst = form.cleaned_data['gst']
            tds = form.cleaned_data['tds']

            gst_amount = (amount*gst)/100
            total = amount + gst_amount
            tds_amount  = (tds*amount)/100
            bal_payable = total - tds_amount
           
            
    # form = Calculate()
            return render(request, 'index.html', {'gst_amt':gst_amount,'total': total, 'tds_amt':tds_amount, 'bal_payable':bal_payable})

    return render(request, "index.html")