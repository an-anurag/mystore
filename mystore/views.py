from django.views.generic import TemplateView


class StoreIndex(TemplateView):
    template_name = 'index.html'
