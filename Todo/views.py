from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from Todo.models import Todo
from django.contrib import messages


now = timezone.now()
# Create your views here.
def index(request):
    data=Todo.objects.all().order_by('-id')
    return render(request,'TodoApp/index.html',{"todos":data})
    
@csrf_exempt
def add_data(request):
  task=request.POST['task']
  now = timezone.now()
  Todo.objects.create(task=task)
  messages.add_message(request, messages.SUCCESS, "Data Inserted Successfully!")

  return HttpResponseRedirect('/')


@csrf_exempt
def delete_task(request,id):
  now = timezone.now()
  Todo.objects.get(id=id).delete()
  return HttpResponseRedirect('/')
  