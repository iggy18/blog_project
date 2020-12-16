from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# create home page view extend list view
class HomePageView(ListView):
    template_name = "home.html"
    model = Post

# add detail view
class DetailView(TemplateView):
    template_name = "post_detail.html"
    model = Post