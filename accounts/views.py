from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView)

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('dbmf:dbmf')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('dbmf:dbmf')


'''
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")



def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

'''
