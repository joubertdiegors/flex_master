from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def custom_page_not_found_view(request, exception):
    return redirect('/')