from django.shortcuts import render
from django.views import View
from django.http import HttpResponse # <- View class to handle requests
from django.views.generic.base import TemplateView
from .models import Architect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Now that we have our route established it is time to build out
#  our view function.

# We will be leveraging class base views provided to us by Django. 
# To do this we will be importing 
# the classes at the top of the file.
# Create your views here.
# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name = "home.html"

class About(TemplateView):
        template_name = "about.html"

class ArchitectList(TemplateView):
        template_name = "architect_list.html"

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
# to get the query parameter we have to acccess it in the request.GET dictionary object        
                name = self.request.GET.get("name")
# If a query exists we will filter by name 
                if name != None:
# .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
                        context["architects"] = Architect.objects.filter(name__icontains=name)
                        context["header"] = f"Searching for {name}"
                else:
                        context["architects"] = Architect.objects.all()
# default header for not searching 
                        context["header"] = "Top Architects"
                return context

class ArchitectCreate(CreateView):
        model = Architect
        fields = ['name', 'image', 'firm', 'nationality','award','bio']
        template_name = "architect_create.html"
        success_url = "/architects/"


class ArchitectDetail(DetailView):
        model = Architect
        template_name = "architect_detail.html"

# architects = [ 
#     Architect("Richard Meier","https://archinect.imgix.net/uploads/ea/ea09afa925e45f621f785ecc7c8ab409.jpg?auto=compress%2Cformat", "MeierPartners", "American"," Pritzker 1984, AIA gold medal 1997","Richard Meier is an American abstract artist and architect, whose geometric designs make prominent use of the color white."),
#     Architect("Santiago Calatrava","https://www.artemide.com/contents/immagini/designer/4865837-960x960.jpg","Santiago Calatrava- Architects & Engineers","Spanish","AIA Gold Medal, European prize for Architects","Santiago Calatrava Valls is a Spanish architect, structural engineer, sculptor and painter, particularly known for his bridges supported by single leaning pylons, and his railway stations, stadiums, and museums, whose sculptural forms often resemble living organisms."),
#     Architect("Renzo Piano","https://www.interviewmagazine.com/wp-content/uploads/2015/05/img-renzo_183908884492.jpg","Renzo Piano Building Workshop","Italian","Priztker Architecture Prize 1998","Renzo Piano OMRI OMCA is an Italian architect. His notable buildings include the Centre Georges Pompidou in Paris, The Shard in London, the Whitney Museum of American Art in New York City and Stavros Niarchos Foundation Cultural Center in Athens.")
#     ]

# class ArchitectList(TemplateView):
#     template_name = "architect_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["architects"] = architects # this is where we add the key into our context object for the view to use
    #     return context