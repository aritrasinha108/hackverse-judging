from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

from .forms import NewUserCreationForm, SubmissionForm, JudgementForm
from .models import Submissions

import csv
# Create your views here.

@staff_member_required
def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('View')
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
            return redirect('View')
    else:
        form = SubmissionForm()
    args = {
        'form': form,
    }
    return render(request, 'accounts/create_submission.html', args)


def view_all_submissions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    submissions = Submissions.objects.all
    return render(request,'accounts/view_submissions.html', {'submissions': submissions})

@staff_member_required
def edit_submission(request,sub_id):
    sub = Submissions.objects.get(pk = sub_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance= sub)
        if form.is_valid():
            form.save() 
            return redirect('View')
    form = SubmissionForm(instance= sub)
    args = {
        'form': form,
    }
    return render(request, 'accounts/create_submission.html', args)

@staff_member_required
def delete_submission(request, sub_id):
    Submissions.objects.filter(id=sub_id).delete()
    return redirect('/auth/submissions')

def view_submission(request,sub_id):
  submission = Submissions.objects.get(pk = sub_id)
  if request.method == 'POST':
        judgeform = JudgementForm(request.POST, instance=submission) 
        if judgeform.is_valid():
            submission.total = judgeform.cleaned_data['param1'] + judgeform.cleaned_data['param2'] + judgeform.cleaned_data['param3'] 
            judgeform.save() 
            submission.save()
            return redirect('View')
  form = JudgementForm(instance= submission)
  return render(request, 'accounts/view_submission.html', {'submission': submission,'form':form})

@staff_member_required
def download_csv(request):
    submissions = Submissions.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="submissions.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'title', 'description', 'devfolio_link', 'codebase_link', 'team_name', 'member_name', 'member_email', 'member_phone', 'judge', 'param1', 'param2', 'param3', 'total'])
    subs = submissions.values_list('id', 'title', 'description', 'devfolio_link', 'codebase_link', 'team_name', 'member_name', 'member_email', 'member_phone', 'judge', 'param1', 'param2', 'param3', 'total')
    for s in subs:
        writer.writerow(s)
    return response