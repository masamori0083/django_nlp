from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return render(
            request,
            "nlp/home.html",
        )
    else:
        title = request.POST["title"]
        return render(
            request,
            "nlp/home.html",
            {"title": title.split()}
        )
