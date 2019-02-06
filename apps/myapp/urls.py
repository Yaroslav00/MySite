from django.urls import path
from apps.myapp.views import start_page
from apps.myapp.views import page_with_category
from apps.myapp.views import log_in


urlpatterns = [
    path('', start_page, name='start_page'),
    path('category/', page_with_category, name='page_with_category'),
    path('LogIn.html', log_in, name='log_in')


]
