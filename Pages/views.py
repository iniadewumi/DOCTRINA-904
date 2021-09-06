from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from Doctors.models import Doctor
from Taxonomy.models import DoctorTaxonomy
from Hospitals.models import HospitalSystem
from django.views.generic import TemplateView, ListView
import operator
from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions import Concat 
from itertools import chain
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import ListView
# import socket

#07231281158dd1#
class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise


class HomepageView(TemplateView):
    template_name = 'Pages/index.html'

    def header(self, *args, **kwargs):
        pass    

    def get_context_data(self, **kwargs):
        # x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[0]
        # else:
        #     ip = self.request.META.get('REMOTE_ADDR')

        # try:
        #     socket.inet_aton(ip)
        #     ip_valid = True
        # except socket.error:
        #     ip_valid = False

        context = super().get_context_data(**kwargs)
        context['hospitals'] = HospitalSystem.objects.all()[:50]
        context['doctors'] = Doctor.objects.all()[:50]
        context['taxonomies'] = [ x for x in DoctorTaxonomy.objects.all() if x.specialization!=None ]
        # context['hospitals'] = HospitalSystem.objects.filter(practice_address__city = "Tulsa")[:20]
        # context['doctors'] = Doctor.objects.filter(practice_address__city = "Tulsa")[:20]
        print(context)
        return context 



class SearchResultsView(ListView):
    model = Doctor
    template_name = 'Pages/Search-Results.html'
    paginate_by = 5

    def get_queryset(self, **kwargs):  # sourcery no-metrics
        name = self.request.GET['doctorname'].replace("  ", " ")
        expertise = self.request.GET['aoe']
        experience = self.request.GET['experience']
        location = self.request.GET['location']
        if experience=="0":
            experience = ""
        if expertise=="None":
            expertise = ""

        terms = [term for term in [name, expertise, experience, location] if term!=""]
        if not terms:
            return Doctor.objects.all()[:100]


        if " " in name:
            first_name = name.split(" ")[0]
            last_name = name.split(" ")[1]
            name_results = Doctor.objects.filter(Q(first_name__icontains =first_name) | Q(last_name__icontains =last_name))

        elif name=="":
            name_results = []
        else:
            name_results = Doctor.objects.filter(Q(first_name__icontains =name) | Q(last_name__icontains =name))


        if location=="":
            location_results = name_results
        else:
            if "," in location:
                city = location.split(",")[0].strip()
                state = location.split(",")[1].strip()
            else:
                city = location.strip()
                state = location.strip()
            if len(name_results)<20:
                    location_results = Doctor.objects.filter(Q(practice_address__city__icontains=city) | Q(practice_address__state__icontains=state))
                    location_results = list(chain(location_results, location_results))
            else:
                location_results =[x for x in name_results if city.lower() in x.practice_address.city.lower()]
        
        if expertise=="None" or expertise=="":
            expertise_result = location_results
        else:
            if len(location_results)<20:
                expertise_result = list(chain(Doctor.objects.filter(doctor_taxonomy__area_of_expertise__contains=expertise), location_results))
            else:
                for doc in location_results:
                    location_results = [x for x in location_results if x.doctor_taxonomy.area_of_expertise!=None]
                    expertise_result = [x for x in location_results if expertise.lower() in x.doctor_taxonomy.area_of_expertise.lower()]

        if len(expertise_result)<20:
            if experience==4:
                experience_result = Doctor.objects.filter(experience__lte=5)
            elif experience in [5, 10, 15]:
                experience_result = Doctor.objects.filter(experience__gt=experience)
            else:
                experience_result = expertise_result

        else:
            if experience==4:
                experience_result = [x for x in expertise_result if int(x.experience)<5]
            elif experience in [5, 10, 15]:
                experience_result = [x for x in expertise_result if int(x.experience)<experience]
            else:
                experience_result = expertise_result

        results = experience_result
        
        # results = list(
        #     chain(
        #        experience_result, expertise_result, location_results
        #     )
        # )

        return sorted(results, key=operator.attrgetter('practice_address.city'))
        

    # paginate_by = 10
    # def get_queryset(self):
    #     query_set = Doctor.objects.filter(first_name__contains="John")








    # def get_queryset(self,**kwargs):
    #     name = self.request.POST['doctorname']
    #     expertise = self.request.POST['aoe']
    #     experience = self.request.POST['experience']

    #     if self.request.POST['location']=="":
    #         location = ""
    #     if "," in self.request.POST['location']:
    #         self.city = self.request.POST['location'].split(",")[0].strip()
    #         self.state = self.request.POST['location'].split(",")[1].strip()
    #     else:
    #         self.city = self.request.POST['location'].strip()
    #         self.state = self.request.POST['location'].strip()

    #     context = super().get_context_data(**kwargs)
    #     names = self.name_search()
    #     loc = self.location_search()
    #     expr = self.experience_search()
    #     expt = self.expertise_search()
    #     context['results'] = list(chain(names, loc, expr, expt))
    #     return super(SearchResultsView, self).dispatch(**kwargs)
    


    # def experience_search(self):
    #     if self.experience==0:
    #         return None
    #     elif self.experience==4:
    #         return Doctor.objects.filter(experience__lte=5)
    #     elif self.experience in [5, 10, 15]:
    #         return Doctor.objects.filter(experience__gt=self.experience)

    # def location_search(self):         
    #     if self.location == "":
    #         return None
    #     return Doctor.objects.filter(Q(practice_address__city__icontains=self.city) | Q(practice_address__state__icontains=self.state))
    
    # def expertise_search(self):
    #     if self.expertise=="None":
    #         return None
    #     else:
    #         return Doctor.objects.filter(area_of_expertise__contains=self.expertise)



def Signup(request):
    return render(request, 'Pages/Sign-Up.html')

def About(request):
    return render(request, 'Pages/About.html')


# Create your views here.
# def SearchResults(request):


#     name = request.POST['doctorname']
#     expertise = request.POST['aoe']
#     experience = request.POST['experience']
#     print(type(experience))

#     if "," in request.POST['location']:
#         city = request.POST['location'].split(",")[0].strip()
#         state = request.POST['location'].split(",")[1].strip()
#     else:
#         city = request.POST['location'].strip()
#         state = request.POST['location'].strip()
    


#     if expertise!="":
#         print(expertise)
#         expt_results = Doctor.objects.filter(area_of_expertise__contains=expertise)
#     else:
#         expt_results =[]

#     if name !="":
#         name_results = Doctor.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).filter(full_name__icontains=name)
#     else:
#         name_results = []

#     if experience!="":
#         expr_results = Doctor.objects.filter(experience__contains=experience)
#     else:
#         expr_results = []
    
    
    
#     location_results = Doctor.objects.filter(Q(practice_address__city__icontains=city) | Q(practice_address__state__icontains=state))


#     results = list(chain(Doctor.objects.filter(Q(experience__contains=experience)), name_results))
#     context = {'results': results}

#     return render(request, 'Pages/Search-Results.html', context=context)
