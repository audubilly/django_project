from django.shortcuts import render
from .models import Image


def point(request):
    images = Image.objects.order_by("publish_date")
    context = {
        "images": images
    }
    return render(request, 'Index.html', context)

# Create your views here.
