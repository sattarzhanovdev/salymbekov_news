from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from news.models import News

def index(request):
  return render(request, 'index.html')

def more(request):
  return render(request, 'more.html')

def category(request):
  return render(request, 'category.html')

from django.http import JsonResponse
from news.models import News

def news_list(request):
  # Retrieve all News objects from the database
  news_objects = News.objects.all()
  
  # Construct a custom JSON response
  news_list = []
  for news in news_objects:
      news_dict = {
          'title': news.title,
          'description': news.description,
          'category': news.category,
          # Add more fields as needed
      }
      if news.image:
          news_dict['image'] = news.image.url
      news_list.append(news_dict)
  
  # Return JSON response
  return JsonResponse(news_list, safe=False)
