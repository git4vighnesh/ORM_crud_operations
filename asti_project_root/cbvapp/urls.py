from django.urls import path
from . import views

urlpatterns = [
    path('fun-greet/', views.fun_greet,name='fun-greet'),
    path('cls_greet/', views.GreetClassBasedView.as_view(), name='cls_greet'),

    path('home/', views.LoadHomeTemplate.as_view(), name='home'),
    path('emp_data/', views.LoadHomeTemplateWithData.as_view(), name='emp_data'),
    path('home1/', views.TemplateView.as_view(template_name='cbvapp/home.html'),name='home1'),


    path('',views.TemplateView.as_view(template_name='cbvapp/my_home.html'),name='myhome'),
    path('my-home/',views.RedirectView.as_view(url= '/cbvapp'),name='my-home'),
    path('python/',views.RedirectView.as_view(url= '/cbvapp'),name='python'),


    path('amazon/',views.RedirectView.as_view(url='https://www.amazon.in/'), name="amazon")


]


#http://localhost:8000/cbvapp/fun-greet/
#http://localhost:8000/cbvapp/cls_greet/
#http://localhost:8000/cbvapp/home/
#http://localhost:8000/cbvapp/emp_data/
#http://localhost:8000/cbvapp/home1/
#http://localhost:8000/cbvapp/amazon/