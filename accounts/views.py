from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewUserCreationForm

# Create your views here.

@staff_member_required
def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewUserCreationForm()
    args = {
        'form': form,
    }
    return render(request, 'accounts/register.html', args)