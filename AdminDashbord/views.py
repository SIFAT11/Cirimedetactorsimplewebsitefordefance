from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from PoliceDashbord.models import PolicProfile

from UserDashbord.models import GDForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('index2')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('index2')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'admindash/adminlogin.html')

@login_required(login_url='/loginoption/')
def admin_logout(request):
    logout(request)
    return redirect('loginoption')

from django.contrib.auth.models import User

# Create your views here.
def index2(request):
    gdlist = GDForm.objects.all()
    total_gd = gdlist.count()
    total_login_users = User.objects.count()
    accepted_gd_count = gdlist.filter(status='Taken').count()# Calculate the total GD records
    rejected_gd_amount = gdlist.filter(status='Rejected').count()
    context = {'gdlist': gdlist, 'total_gd': total_gd,'accepted_gd_count': accepted_gd_count,'rejected_gd_amount': rejected_gd_amount,'total_login_users':total_login_users}
    return render(request, 'index2.html', context)


def accept_gd(request, gd_id):
    gd_instance = get_object_or_404(GDForm, id=gd_id)
    gd_instance.status = 'Taken'  # Set status to 'Taken' for acceptance
    gd_instance.save()
    return redirect('index2')  # Redirect back to the GD list page

def reject_gd(request, gd_id):
    gd_instance = get_object_or_404(GDForm, id=gd_id)
    gd_instance.status = 'Rejected'  # Set status to 'Rejected' for rejection
    gd_instance.save()
    return redirect('index2')  # Redirect back to the GD list page



from JudjeDashbord.models import JudgeProfile
def loginrequest(request):  # Import the JudgeProfile model
    judges = JudgeProfile.objects.all()
    context = {
        'judges': judges,
    }
    print(judges)
    return render(request, 'admindash/loginrequestjug.html', context)

@login_required(login_url='/loginoption/')
def accept(request):
    accept_list = GDForm.objects.filter(status='Taken') 
    return render(request,'admindash/AcceptGd.html',locals())

@login_required(login_url='/loginoption/')
def reject(request):
    rejection_list = GDForm.objects.filter(status='Rejected')  # Modify this query based on your model structure
    return render(request,'admindash/RejectGd.html',locals())

@login_required(login_url='/loginoption/')
def gd_details(request, gd_id):
    gd_instance = get_object_or_404(GDForm, gd_id=gd_id)
    return render(request, 'admindash/gd_details.html', {'gd_instance': gd_instance})



from django.shortcuts import get_object_or_404
@login_required(login_url='/loginoption/')
def approve_judge(request,judge_id):
    judge = get_object_or_404(JudgeProfile,id=judge_id)
    judge.status = 'Taken'
    judge.save()
    return redirect('loginrequestjug')  # Redirect to the rejection list page

@login_required(login_url='/loginoption/')
def reject_judge(request,judge_id):
    judge = get_object_or_404(JudgeProfile,id=judge_id)
    judge.status = 'Rejected'
    judge.save()
    return redirect('loginrequestjug')  # Redirect to the rejection list page

from django.http import Http404


from django.http import Http404

from django.http import Http404
@login_required(login_url='/loginoption/')
def viewjudge_profile(request,judge_id):
    try:
        judge = JudgeProfile.objects.get(id=judge_id)
    except JudgeProfile.DoesNotExist:
        # If the judge doesn't exist, raise Http404 to display a 404 error page.
        raise Http404("Judge does not exist or an error occurred")

    # If the judge exists, render the judge_profile.html template.
    return render(request, 'admindash/judge_profile.html', {'judge': judge})



#Police Section
def loginrequestpo(request):
    # Retrieve a list of police profiles
    polices = PolicProfile.objects.all()
    context = {
        'polices': polices,
    }
    return render(request, 'admindash/loginpo.html', context)

@login_required(login_url='/loginoption/')
def approve_Police(request, policeid):
    police = get_object_or_404(PolicProfile, id=policeid)
    police.status = 'Taken'
    police.save()
    return redirect('loginpo')  # Redirect to the login request list page


@login_required(login_url='/loginoption/')
def reject_police(request, policeid):
    police = get_object_or_404(PolicProfile, id=policeid)
    police.status = 'Rejected'
    police.save()
    return redirect('loginpo')

from django.shortcuts import render, get_object_or_404

@login_required(login_url='/loginoption/')
def viewpolice_profile(request, policeid):
    police = get_object_or_404(PolicProfile, id=policeid)
    return render(request, 'admindash/policeprofile.html', {'police': police})
