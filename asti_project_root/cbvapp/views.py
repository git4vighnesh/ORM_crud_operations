from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView

def fun_greet(request):
    if request.method == 'GET':
        msg = " Hello, GET Http Method Called"
        resp_dict = {'message': msg }
        return render(request, 'cbvapp/greet.html', context=resp_dict)
    elif request.method == 'POST':
        msg = "HELLO, POST method got called"
        resp_dict = {'message': msg}
        return render(request,'cbvapp/greet.html' ,context=resp_dict)



class GreetClassBasedView(View):
    def get(self,request):
        msg = " Hello, GET Http Method Called"
        resp_dict = {'message': msg }
        return render(request, 'cbvapp/greet.html', context=resp_dict)

    def post(self,request):
        msg = "HELLO, POST method got called"
        resp_dict = {'message': msg}
        return render(request, 'cbvapp/greet.html', context=resp_dict)



class LoadHomeTemplate(TemplateView):
    template_name = "cbvapp/home.html"


class LoadHomeTemplateWithData(TemplateView):
    template_name = "cbvapp/emp_data.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emp_id'] = 2255
        context['emp_name'] = 'md ali'
        context['emp_address'] = 'bengaluru'
        return context
