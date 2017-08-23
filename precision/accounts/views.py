from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View

from .forms import LoginForm


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
