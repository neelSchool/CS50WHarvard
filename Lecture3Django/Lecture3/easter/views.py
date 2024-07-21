from django.shortcuts import render
import datetime


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "easter/index.html", {
          "easter": now.month == 3 and now.day == 31
})
    
    
