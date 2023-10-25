from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
import json
from django.db.models.query import QuerySet  # Import QuerySet
from .models import Resort

class QuerySetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return list(obj)
        return super().default(obj)

@require_http_methods(["GET", "POST"])
def list_resorts(request):
    if request.method == "GET":
        resorts = Resort.objects.all().values()
        return JsonResponse(
            {"resorts": resorts},
            encoder=QuerySetEncoder,  # Use the custom encoder
            safe=False
        )
    else:
        content = json.loads(request.body)
        resort = Resort.objects.create(**content)
        return JsonResponse(
            {"resort": model_to_dict(resort)},
            encoder=QuerySetEncoder,  # Use the custom encoder
            safe=False
        )
