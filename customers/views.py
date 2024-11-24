from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.utils import timezone
from .forms import ContactForm
from .models import WebsiteVisit, CVDownload
from django.core.mail import send_mail
from django.conf import settings
import os


# Index Page
def index(request):
    return render(request, 'index.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Services Page
def services(request):
    return render(request, 'services.html')


# Portfolio Page
def portfolio(request):
    return render(request, 'portfolio.html')


# Resume Page with Resume File Download
def resume(request):
    return render(request, 'resume.html')


# Contact Page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Message Sent Successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Error submitting form. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# Website visit logging
import logging
from .models import WebsiteVisit
from django.utils import timezone

logger = logging.getLogger(__name__)

def track_visit(request):
    visit = WebsiteVisit.objects.create(
        user_ip=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        visit_time=timezone.now()
    )
    logger.debug(f"Visit logged: {visit}")
    return render(request, 'index.html')



from .models import CVDownload
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download_cv(request):
    cv_download = CVDownload.objects.first()  # Assuming there's only one entry for counting
    if cv_download:
        cv_download.increment_count()

    file_path = os.path.join(settings.BASE_DIR, 'media', 'VINCENT_KIPLANGAT_CV.pdf')

    try:
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="VINCENT_KIPLANGAT_CV.pdf"'
            return response
    except FileNotFoundError:
        raise Http404("CV file not found.")

