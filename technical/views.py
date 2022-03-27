from django.shortcuts import render,redirect
from tradingview_ta import TA_Handler, Interval, Exchange
from django.views import View
from django.contrib import messages
from .coins import Hour



class Index(View):
        

        def get(self,request):
                context={}

                context['pageview'] = "تکنیکال"
                context['title'] = "تکنیکال"
                
                # Sample coins
                context['ada1'] =      Hour.summary(1, "ADAUSD")
                context['ada2'] =      Hour.summary(2, "ADAUSD")
                context['ada4'] =      Hour.summary(4, "ADAUSD")

                context['btc1'] =      Hour.summary(1, "BTCUSD")
                context['btc2'] =      Hour.summary(2, "BTCUSD")
                context['btc4'] =      Hour.summary(4, "BTCUSD")

                context['eth1'] =      Hour.summary(1, "ETHUSD")
                context['eth2'] =      Hour.summary(2, "ETHUSD")
                context['eth4'] =      Hour.summary(4, "ETHUSD")

                return render(request,"technical/index.html",context)




