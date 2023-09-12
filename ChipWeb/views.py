from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from .models import Cars_Info
from .forms import Cars
from .forms import CarsS
from django.views.generic import ListView
import datetime
from django.template import Context
from django.db.models.query import QuerySet
from django.template.loader import render_to_string, get_template

class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
          subject= f"{name} from PowerSeekers.",
          body=message,
          from_email=settings.EMAIL_HOST_USER,
          to=[settings.EMAIL_HOST_USER],
          reply_to=[email]
        )
        email.send()
        return HttpResponseRedirect(request.path)

class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"
    
    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")
        
        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Ačiū {fname}, už laiko rezervavimą, greitu metu atsiusime visą informaciją į jūsų el. paštą su jums priskirtu laiku.")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by= 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "Dėl jūsų automobilio programavimo darbų",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"{appointment.first_name} 'o prašymas sėkmingai patvirtintas")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title":"Manage Appointments"
        })
        return context

def exsisting(request):
    title = "Cars Specs"
    QuerySet = Cars_Info.objects.all()

    context={
        "title":title,
        "QuerySet":QuerySet,
    }
    return render(request,'search.html',context)

def search(request):
    title = "Cars Specs"
    form = CarsS(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Marke']
        QuerySet = Cars_Info.objects.filter(Marke=name)
        context={
            'title':title,
            'form':form,
            'QuerySet':QuerySet
        }
        return render(request,'search.html',context)
    
    context={
        'title':title,
        'form':form,
    }
    return render(request,'search1.html',context)    