from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View

from .forms import LoginForm, SchoolAdministratorRegistrationForm


# CODE BELOW THIS LINE IS NOT USED, BUT PRESENT FOR EDUCATION PURPOSES
# ====================================================================

class SignInView(TemplateResponseMixin, View):
    template_name = 'accounts/sign_in.html'

    def get(self, request):
        form = LoginForm()
        context = {'section': 'sign_in', 'form': form}
        return self.render_to_response(context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            return redirect('accounts:sign_in')

# ====================================================================


class RegisterView(TemplateResponseMixin, View):
    template_name = 'registration/register.html',

    def get(self, request):
        form = SchoolAdministrationRegistrationForm
        context = {'section': 'register', 'form': form}
        return self.render_to_response(context)

    def post(self, request):
        form = SchoolAdministrationRegistrationForm(request.POST)
        template_name = 'registration/register_done.html'

        if form.is_valid():
            # Create a new administrator but do not save it yet
            new_administrator = form.save(commit=False)

            # Set chosen password
            new_administrator.set_password(form.cleaned_data['password'])

            # Save administrator object
            new_administrator.save()

            context = {'section': 'register', 'new_administrator': new_administrator}
            return render(request, template_name, context)
        else:
            return redirect('accounts:register')
