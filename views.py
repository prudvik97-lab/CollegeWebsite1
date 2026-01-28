from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Admission,Contact

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


class CSEView(TemplateView):
    template_name = "cse.html"

class CSE_AIML_View(TemplateView):
    template_name = 'cse_ai_ml.html'
    
class CSE_Data_Science_View(TemplateView):
    template_name = "cse_data_science.html"
    
class MechanicalEngineeringView(TemplateView):
    template_name = "mechanical_engineering.html"
    
class CivilEngineeringView(TemplateView):
    template_name = "civil_engineering.html"
    
class ElectricalEngineeringView(TemplateView):
    template_name = "electrical_engineering.html"
    
class AboutUsView(TemplateView):
    template_name = "about_us.html"
    
class ContactUsView(TemplateView):
    template_name = "contact_us.html"
    
class LibraryView(TemplateView):
    template_name = "library.html"
    
class SmartBoardView(TemplateView):
    template_name = "smartboard.html"
    
class HostelView(TemplateView):
    template_name = "hostel.html"
    
class TransportView(TemplateView):
    template_name = "transport.html"
    
class NoRaggingView(TemplateView):
    template_name = "no_ragging.html"
    
class SportsView(TemplateView):
    template_name = "sports.html"
    
class CanteenView(TemplateView):
    template_name = "canteen.html"

class InfrastructureView(TemplateView):
    template_name = "infrastructure.html"
    
class PlacementsView(TemplateView):
    template_name = 'placements.html'
    
    
def admission_view(request):
    if request.method == "POST":
        Admission.objects.create(
            parent_name=request.POST.get('parent_name'),
            student_name=request.POST.get('student_name'),
            student_email=request.POST.get('student_email'),
            mobile_number=request.POST.get('mobile_number'),
            date_of_birth=request.POST.get('date_of_birth'),
            gender=request.POST.get('gender'),
            department=request.POST.get('department'),
        )
        return redirect('admission_success')

    return render(request, 'admission.html')



def admission_success(request):
    return render(request, 'admission_success.html')


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('contact_success')

    return render(request, 'contact_us.html')




def contact_success(request):
    return render(request, 'contact_success.html')