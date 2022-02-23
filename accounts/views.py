from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import csv
from .forms import NewUserCreationForm, SubmissionForm, JudgementForm,AssignmentForm
from .models import Submissions, User, Judgement
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@staff_member_required
def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           user = form.instance
           if user.is_organiser:
               user.is_staff = True
               user.save()
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
    if request.user.is_staff:
        submissions = Submissions.objects.all
    else:
        submissions = Submissions.objects.filter(judges_assigned = request.user)

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
        judgement,created = Judgement.objects.get_or_create(submission=submission, judge = request.user)
        print(judgement)
        judgeform = JudgementForm(request.POST) 
        if judgeform.is_valid():
            judgement.param1 = judgeform.cleaned_data['param_1'] 
            judgement.param2 = judgeform.cleaned_data['param_2'] 
            judgement.param3 = judgeform.cleaned_data['param_3'] 
            judgement.save()
            return redirect('View')
        submission = Submissions.objects.get(pk = sub_id) 
        form = AssignmentForm(request.POST)
        if form.is_valid():
            j1 = form.cleaned_data['judge1']
            j2 = form.cleaned_data['judge2']
            try:
                judge1 = User.objects.get(username = j1)
                judge2 = User.objects.get(username = j2)
            except ObjectDoesNotExist:
                return redirect('View')

            submission.judges_assigned.clear()
            submission.judges_assigned.add(judge1,judge2)
            Judgement.objects.filter(submission=submission).delete()
            judgement1 = Judgement(submission=submission, judge = judge1)
            judgement2 = Judgement(submission=submission, judge = judge2)
            submission.save()
            judgement1.save()
            judgement2.save()
  try:
    judgement = Judgement.objects.get(judge = request.user, submission=submission)
    form = JudgementForm(initial={'param_1': judgement.param1, 'param_2': judgement.param2, 'param_3': judgement.param3 }) 
  except ObjectDoesNotExist:
    form = JudgementForm() 
  judges = submission.judges_assigned.all()
  if len(judges) > 0:
    assign_form = AssignmentForm(initial={'judge1': judges[0].username, 'judge2': judges[1].username})
  else:
    assign_form = AssignmentForm()  
  return render(request, 'accounts/view_submission.html', {'submission': submission,'form':form, 'assign_form': assign_form})