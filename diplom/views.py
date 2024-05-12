from django.shortcuts import render
from .forms import BlockForm,QuestionForm,QuickContactForm
from .models import Question,QuickContact


def index(request):
    concrete_amount = None
    volume = None
    quick_contact_form = QuickContactForm()

    if request.method == 'POST':
        block_form = BlockForm(request.POST)
        if block_form.is_valid():
            block = block_form.save(commit=False)
            volume = block.get_volume() / 1000000
            concrete_amount = block.get_concrete_amount()
    else:
        block_form = BlockForm()

    if request.method == 'POST':
        quick_contact_form = QuickContactForm(request.POST)
        if quick_contact_form.is_valid():
            quick_contact = QuickContact.objects.create(
                name=quick_contact_form.cleaned_data['name'],
                email=quick_contact_form.cleaned_data['email'],
                message=quick_contact_form.cleaned_data['message']
            )
            quick_contact_form = QuickContactForm()

    return render(request, 'diplom/index.html', {'block_form': block_form, 'quick_contact_form': quick_contact_form,
                                                 'concrete_amount': concrete_amount, 'volume': volume})
# def index(request):
#     concrete_amount = None
#     volume = None
#     if request.method == 'POST':
#         form = BlockForm(request.POST)
#         if form.is_valid():
#             block = form.save(commit=False)
#             volume = block.get_volume() / 1000000
#             concrete_amount = block.get_concrete_amount()
#     else:
#         form = BlockForm()
#     return render(request, 'diplom/index.html', {'form': form, 'concrete_amount': concrete_amount, 'volume': volume})

def contact(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                question=form.cleaned_data['question']
            )
            return render(request, 'diplom/contact.html', {'form': QuestionForm()})
    else:
        form = QuestionForm()
    return render(request, 'diplom/contact.html', {'form': form})

def aboutus(request):
    return render(request, 'diplom/about-us.html')

def gallery(request):
    return render(request, 'diplom/gallery-default.html')

def faqs(request):
    return render(request, 'diplom/faqs.html')

def portfolio(request):
    return render(request, 'diplom/portfolio-with-text.html')

def service(request):
    return render(request, 'diplom/services.html')

