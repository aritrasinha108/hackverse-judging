from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewUserCreationForm, SubmissionForm
from .models import Submissions
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

@staff_member_required
def create_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubmissionForm()
    args = {
        'form': form,
    }
    return render(request, 'accounts/create_submission.html', args)


def view_all_submissions(request):
    if not request.user.is_authenticated:
        return redirect('/admin')
    
    submissions = Submissions.objects.all
    return render(request,'accounts/view_submissions.html', {'submissions': submissions})

@staff_member_required
def edit_submission(request,sub_id):
    sub = Submissions.objects.get(pk = sub_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance= sub)
        if form.is_valid():
            form.save() 

    form = SubmissionForm(instance= sub)
    args = {
        'form': form,
    }
    return render(request, 'accounts/create_submission.html', args)

@staff_member_required
def delete_submission(request, sub_id):
    Submissions.objects.filter(id=sub_id).delete()
    return redirect('/auth/submissions')