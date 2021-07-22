from django.shortcuts import render
import pandas as pd
from django.conf import settings


# Create your views here.

def home(request):
    if request.method == "POST":
        file = request.FILES["myFile"]
        csv = pd.read_csv(file)
        print(csv)
        media_data = "{}data.csv".format(settings.MEDIA_ROOT)
        media_data_csv = open(media_data, 'w')
        return render(request, "index.html", {"something": True})
    else:
        return render(request, "index.html")


def upload(request):
    return render(request, "fileupload.html")
