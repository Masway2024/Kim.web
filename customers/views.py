from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, Http404
from .forms import ContactForm
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

from django.shortcuts import render
from .forms import ContactForm

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm  # Assuming you're using a form
from .models import ContactMessage  # Assuming you have a model for storing contact messages


from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            messages.success(request, 'Message Sent Successfully!')
            return redirect('contact')  # Redirect to avoid resubmission
        else:
            messages.error(request, 'Error submitting form. Please try again.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# views.py
from django.shortcuts import render
from .models import WebsiteVisit, CVDownload
from django.http import HttpResponse
from django.utils import timezone

def track_visit(request):
    # Log visit data
    visit = WebsiteVisit.objects.create(
        user_ip=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        visit_time=timezone.now()
    )
    # Render the page (you can change this to your homepage view)
    return render(request, 'index.html')


# views.py
def download_cv(request):
    # Increment the CV download count
    cv_download = CVDownload.objects.first()  # Assuming there's only one entry for counting
    if cv_download:
        cv_download.increment_count()

    # Serve the CV file
    file_path = 'path_to_your_cv_file.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="VINCENT KIPLANGAT CV.pdf"'

    with open(file_path, 'rb') as f:
        response.write(f.read())

    return response



