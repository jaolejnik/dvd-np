from django.views.generic import TemplateView


class VueTemplateView(TemplateView):
    template_name = "index.html"
