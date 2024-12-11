from django.shortcuts import render 


def home(request):
    

    return render(request, "home.html")


    
        

def about(request):
    cont="I LOVE YOU"
    return render(request, "about.html", context={"load":cont})
