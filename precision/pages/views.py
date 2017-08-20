from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, View


class HomeView(TemplateResponseMixin, View):
    template_name = 'pages/home.html'

    def get(self, request):
        context = {'section': 'home'}
        return self.render_to_response(context)
