from django.shortcuts import render
from .models import Task
from .forms import ExampleForm


# Create your views here.
def index(request):
    task = Task.objects.all()
    tasklist = []
    for i in task:
        tasklist.append({'task': i})
    context = {'tasklist': tasklist}
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format((name, type(value), value)))
    return render(request, "form-example.html", {"method": request.method, "form": form})
