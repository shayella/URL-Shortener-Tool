from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import URLCountForm
from shortener.models import ShortenURL
from django.conf import settings

# Create your views here.

URL_START_STRING = getattr(settings,"URL_START_STRING")

def url_count(request, shortcode=None):
    if ShortenURL.objects.count() > 0:
        sc_eg = ShortenURL.objects.first().shortcode
        sc_eg = URL_START_STRING+'/'+sc_eg+'/'
    else:
        sc_eg = ""

    if shortcode is None:
        if request.method == 'GET':
            form = URLCountForm();
            return render(request,'analystics/url_count.html',{'form':form,'sc_eg':sc_eg})

        elif request.method == 'POST':
            form = URLCountForm(request.POST)
            if form.is_valid():
                short_url = form.cleaned_data.get('short_url')

                if short_url.startswith(URL_START_STRING+'/'):
                    if short_url.endswith('/'):
                        sc = short_url.split('/')[-2]
                    else:
                        sc = short_url.split('/')[-1]

                    qs = ShortenURL.objects.filter(shortcode__iexact = sc)
                    if bool(qs) and qs.count()==  1:
                        obj = qs.first()
                        print(obj)
                        return render(request,'analystics/total_url_count.html',{'obj':obj,'sc_eg':sc_eg})
                    else:
                        return render(request,'analystics/url_count.html',{'form':form, 'not_exists':True,'sc_eg':sc_eg})

            return  render(request,'analystics/url_count.html',{'form':form, 'wrong_url':True,'sc_eg':sc_eg})

    else:
        obj = get_object_or_404(ShortenURL, shortcode = shortcode)
        s_url = URL_START_STRING +'/'+ shortcode
        return render(request,'analystics/total_url_count.html',{'obj':obj,'sc_eg':sc_eg})
