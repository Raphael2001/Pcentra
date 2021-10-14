from django.views import View
from django.http import JsonResponse, HttpResponseRedirect, Http404
import json
from .models import Shortener
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class create(View):
    # creating a new short url
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        url = data.get('url')

        s = Shortener(long_url=url)
        s.save()

        full_url = request.build_absolute_uri()
        create_path = request.get_full_path()
        full_url = full_url.replace(create_path, '')

        data = {
            "message": f"The shorter url is: {full_url}/{s.short_url}"
        }
        return JsonResponse(data, status=201)


def redirect_url_view(request, shortened_part):
    # redirecting with the short url
    try:

        shortener = Shortener.objects.get(short_url=shortened_part)

        shortener.times_followed += 1

        shortener.save()

        returned_url = shortener.long_url

        if returned_url.find("https://") == -1 and returned_url.find("http://") == -1:
            returned_url = "https://" + returned_url

        return HttpResponseRedirect(returned_url)

    except:
        raise Http404('Sorry this link is broken :(')
