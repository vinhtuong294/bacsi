from django.http import request
from django.shortcuts import render
from form_example.forms import OrderForm
"""
def form_example(request):
    return render(request, "formexample.html", {"method": request.method})
"""
# Create your views here.
"""
from .forms import ExampleForm
def form_example(request):
    form = ExampleForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "formexample.html", {"method": request.method, "form": form})
"""
def form_example(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = OrderForm()
    return render(request, "formexample.html", {"method": request.method, "form": form})
    form = OrderForm()
    return render(request, 'form-example.html', {"form": form})
    initial = {"email": "user@example.com"}

    # Truyền giá trị khởi tạo vào form
    if request.method == "POST":
        # Khi người dùng submit form (POST), khởi tạo form với dữ liệu từ request.POST và giá trị initial
        form = OrderForm(request.POST, initial=initial)
    else:
        # Khi người dùng truy cập lần đầu tiên (GET), khởi tạo form với giá trị initial
        form = OrderForm(initial=initial)

    return render(request, 'form-example.html', {"form": form})