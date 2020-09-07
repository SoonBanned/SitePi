from django.shortcuts import render
from .models import ImageEntry
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'test_pixel.html')

def check_keyword(request):
    if request.method == 'GET':
        keyword = request.GET['keyword']
        print(request.session['active_image_id'])
        keywords_set = []
        for keyword_set in ImageEntry.objects.get(id=int(request.session['active_image_id'])).keywords_set.all():
            for kw in keyword_set.keywords.all():
                keywords_set.append(kw.value.lower())
        return JsonResponse({'valid': keyword.lower() in keywords_set, 'in': keywords_set})

def session_image(request): #fullsize now, register zoom in session
    if request.method == 'GET':
        #get category later
        request.session['active_image_id'] = ImageEntry.random_id()
        print(request.session['active_image_id'])
        return render(request, 'test_pixel.html', {'image': ImageEntry.objects.get(id=int(request.session['active_image_id'])).image})