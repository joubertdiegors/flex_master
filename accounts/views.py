from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, CustomerRegistrationForm
from customers.models import Customer, CustomerState, CustomerType

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not user.is_superuser and not user.is_staff:
                return redirect('/')
            return redirect('dashboard')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerRegistrationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and customer_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            customer = customer_form.save(commit=False)
            customer.user = new_user
            customer.name = new_user.first_name
            customer.contact_person_email = new_user.email

            # Definir valores padrão para campos obrigatórios
            customer.created_by = new_user  # Assumindo que o próprio usuário é o criador

            print("Customer antes de salvar:", customer)
            try:
                customer.save()
                print("Customer salvo com sucesso")
            except Exception as e:
                print("Erro ao salvar Customer:", e)
            
            return redirect('login')
        else:
            print("Formulários inválidos")
            print("Erros user_form:", user_form.errors)
            print("Erros customer_form:", customer_form.errors)
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerRegistrationForm()

    return render(request, 'register.html', {'user_form': user_form, 'customer_form': customer_form})