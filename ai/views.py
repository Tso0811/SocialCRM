from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import recommend_events_for_user

@login_required
def recommend_events(request):
    user = request.user
    recommendations = recommend_events_for_user(user)
    return JsonResponse({'recommendations': recommendations})