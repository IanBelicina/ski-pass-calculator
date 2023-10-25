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

@require_http_methods(["GET","DELETE"])
def show_resort(request, id):

    if request.method == "GET":
        try:
            resort = Resort.objects.get(id=id)
            return JsonResponse(
                {"resort":model_to_dict(resort)},
                encoder=QuerySetEncoder,
                safe=False
            )
        except Resort.DoesNotExist:
            response = JsonResponse({"Message": f"Resort with ID {id} does not exist"})
            response.status_code = 404
            return response
    else:
        try:
            resort = Resort.objects.get(id=id)
            resort.delete()
            return JsonResponse(
                {"deleted":True},
                safe=False
            )
        except Resort.DoesNotExist:
            response = JsonResponse({"Message": f'Resort with ID {id} does not exist'})
            response.status_code=404
            return response
