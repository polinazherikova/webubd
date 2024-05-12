from .forms import QuickContactForm

def quick_contact_form(request):
    return {'quick_contact_form': QuickContactForm()}