from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from UserDashbord.models import GDForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/loginoption/')
def index3(request):
    totalgd = GDForm.objects.all().count()
    acceptdgd = GDForm.objects.filter(status='Taken').count()
    return render(request,'index3.html',locals())


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JudgeProfile

def jugregister(request):
    if request.method == 'POST':
        # Get user input
        jugid = request.POST['jugid']
        full_name = request.POST['full_name']
        email = request.POST['email']
        age = request.POST['age']
        phone = request.POST['phone']
        image = request.FILES.get('image')  # Use request.FILES for file uploads
        gender = request.POST['gender']
        password = request.POST['password']
        repassword = request.POST['repassword']

        # Validate password match
        if password != repassword:
            messages.error(request, "Passwords do not match")
            return redirect('jugregister')

        # Check if jugid or email already exists
        if User.objects.filter(username=jugid).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Jug ID or email already exists")
            return redirect('jugregister')

        # Create the user
        user = User.objects.create_user(username=jugid, email=email, password=password)
        user.first_name = full_name
        user.save()

        # Create the JudgeProfile
        judge_profile = JudgeProfile(jugid=user, age=age, phone=phone, gender=gender, image=image)
        judge_profile.save()

        messages.success(request, "Registration successful. You are now logged in.")
        return redirect('juglogin')

    return render(request, 'jugdash/jugregister.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login  # Import your JudgeProfile model

def juglogin(request):
    if request.method == 'POST':
        judgeid = request.POST.get('judgeid')  # Update to match the input field name
        password = request.POST.get('password')
        user = authenticate(request, username=judgeid, password=password)
        if user is not None:
            judge_profile = JudgeProfile.objects.filter(jugid=user).first()  # Retrieve the judge's profile
            if judge_profile:
                if judge_profile.status == 'Taken':
                    login(request, user)
                    # Redirect to the dashboard or any other page upon successful login
                    return redirect('index3')  # Change 'dashboard' to your desired URL
                else:
                    messages.error(request, 'Your account status is not "Taken". Please contact the administrator.')
            else:
                messages.error(request, 'No JudgeProfile found for this user.')
        else:
            messages.error(request, 'Invalid Judge ID or password. Please try again or wait for the administrator to approve your account.')

    return render(request, 'jugdash/juglogin.html')



from django.contrib.auth import authenticate, login, update_session_auth_hash,logout
def jugreset(request):
    if request.method == 'POST':
        jugid = request.POST['jugid']
        email = request.POST['email']
        new_pass = request.POST['new_pass']

        try:
            user = User.objects.get(jugid=jugid)
            if user.email == email:
                user.set_password(new_pass)
                user.save()
                update_session_auth_hash(request, user)
                print(new_pass)
                messages.success(request, 'Reset password is successful')
                return redirect('juglogin')
            else:
                messages.error(request, 'Email does not match.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
    return render(request,'jugdash/jugreset.html')

from django.contrib.auth.decorators import login_required

@login_required(login_url='/loginoption/')
def jug_logout(request):
    logout(request)
    return redirect('loginoption')

from django.shortcuts import get_object_or_404

@login_required(login_url='/loginoption/')
def acceptgd(request):
    accept_list = GDForm.objects.filter(status='Taken') 
    return render(request,'jugdash/acceptgd.html',locals())

@login_required(login_url='/loginoption/')
def gdview(request,gd_id):
    gd_instance = get_object_or_404(GDForm, gd_id=gd_id)
    return render(request, 'jugdash/gdview.html', {'gd_instance': gd_instance})
