from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Country_data, Country_data_List
# router = routers.DefaultRouter()
# router.register(r'postecom', Ecom_data)

urlpatterns = [
    path('country/', Country_data.as_view()),
    path('country/<int:id>', Country_data_List.as_view()),

    
]