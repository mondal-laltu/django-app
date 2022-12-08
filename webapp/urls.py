
from django.urls import path
from webapp import views


urlpatterns = (

    path('',views.home,name='home'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('restaurant',views.restaurant,name='restaurant'),
    path('schedule_demo',views.schedule_demo,name='schedule_demo'),
    path('contact_us',views.contact_us,name='contact_us'),

)    