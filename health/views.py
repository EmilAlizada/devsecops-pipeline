from django.http import JsonResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET


@require_GET
@cache_control(no_store=True)
def health(request):
    return JsonResponse({"status": "ok", "service": "devsecops-pipeline"})
