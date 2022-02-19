from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewUserCreationForm, SubmissionForm, JudgementForm,AssignmentForm
from .models import Submissions, User
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
        return redirect('/')
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
        submission = Submissions.objects.get(pk = sub_id) 
        form = AssignmentForm(request.POST)
        if form.is_valid():
            j1 = form.cleaned_data['judge1']
            j2 = form.cleaned_data['judge2']
            try:
                judge1 = User.objects.get(username = j1)
                judge2 = User.objects.get(username = j2)
            except DoesNotExist:
                return redirect(request, '/auth/submissions')

            submission.judges_assigned.clear()
            submission.judges_assigned.add(judge1,judge2)
            submission.save()
  form = JudgementForm(instance= submission)
  judges = submission.judges_assigned.all()
  if len(judges) > 0:
    assign_form = AssignmentForm(initial={'judge1': judges[0].username, 'judge2': judges[1].username})
  return render(request, 'accounts/view_submission.html', {'submission': submission,'form':form, 'assign_form': assign_form})


# @staff_member_required
# def assign_judge(request, sub_id):
#     if request.method == "POST":
#         submission = Submissions.objects.get(pk = sub_id) 
#         form = AssignmentForm(request.POST)
#         if form.is_valid():
#             j1 = form.cleaned_data['judge1']
#             j2 = form.cleaned_data['judge2']
#             try:
#                 judge1 = User.objects.get(username = j1)
#                 judge2 = User.objects.get(username = j2)
#             except DoesNotExist:
#                 return redirect(request, '/auth/submissions')
#             submission.judges_assigned.add(judge1,judge2)
#             submission.save()
#             return redirect(request, "/auth/submissions/"+ str(sub_id))
    
#     return redirect(request, "/auth/submissions/"+ str(sub_id))
