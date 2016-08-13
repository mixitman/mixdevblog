from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm, SignUpForm


def home(request):
    title = 'Welcome'

    # add a form
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "Deadpool"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank You"
        }
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     if not instance.full_name:
    #         instance.full_name = "Name Blank"
    #     instance.save()
    #     landing-context = {
    #         "title": "Thank You"
    #     }

    return render(request, "home.html", context)


def contact(request):
    title = "Contact Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # f = form.cleaned_data
        # for key, value in f.items():
        #     print(key, value)
        # for key in form.cleaned_data:
        #     print(form.cleaned_data.get(key))

        form_message = form.cleaned_data.get("message")
        form_email = form.cleaned_data.get("email")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "{}: {} via {}".format(form_full_name, form_message, form_email)
        some_html_message = """<h1>hello</h1>"""
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=False)
        # print(str(email) + ' ' + str(message) + ' ' + str(full_name))

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)

