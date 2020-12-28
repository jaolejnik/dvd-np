from django.views.generic.base import TemplateView


class VueTemplateView(TemplateView):
    def get_template_names(self):
        return "index.html"
