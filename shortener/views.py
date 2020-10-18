from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import  View
from .models import ShortenURL
from analystics.models import ClickEvent
from .forms import SubmitURLForm
# Create your views here.

def home(request):
    if request.method == "GET":
        form = SubmitURLForm()
        return render(request, 'shortener/index.html', {'form':form})

    if request.method == "POST":
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_url = form.cleaned_data.get('url')
            obj = ShortenURL.objects.create(url=new_url)
            created= True
            context = { "obj": obj, "created":created,"form":form}
            if created:
                return render(request,'shortener/index.html',context)
            else:
                return render(request,'shortener/index.html',context)
        context = {"form":form}
        return render(request, 'shortener/index.html',context)


def shortenurl_redirect_view(request, shortcode= None):
    # sc_url = "does not exist"
    # qs = ShortenURL.objects.filter(shortcode__iexact = shortcode)
    # if bool(qs) and qs.count()==  1:
    #     sc_url = qs.first().url
    obj = get_object_or_404(ShortenURL, shortcode = shortcode)
    print(ClickEvent.objects.create_event(obj))
    return HttpResponseRedirect(obj.url)

# def error_404(request,exception):
#     return render(request,'shortener/404.html')
#
# def error_500(request):
#     return render(request,'shortener/500.html')
