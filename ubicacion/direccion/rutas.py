from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from direccion.views import DireccionDetail,DireccionList


urlpatterns = [
    path('direcciones/', DireccionList.as_view()),
    path('direccion/<int:pk>', DireccionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)