from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from UserDashbord.models import GDForm

def polic_login(request):
    return render(request, 'policDash/polic_login.html')  # Replace 'your_template.html' with your actual login template

def polic_reset(request):
    return render(request, 'policDash/policreset.html')  # Replace 'your_template.html' with your actual password reset template

from django.contrib.auth.models import User

def index4(request):
    totalgd = GDForm.objects.all().count()
    acceptdgd = GDForm.objects.filter(status='Taken').count()
    return render(request,'index4.html',locals())


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import PolicProfile
from django.contrib import messages

def polic_register(request):
    if request.method == 'POST':
        policeid = request.POST['policeid']
        full_name = request.POST['full_name']
        email = request.POST['email']
        age = request.POST['age']
        image = request.FILES.get('image') 
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'policregister.html')

        if User.objects.filter(username=policeid).exists():
            messages.error(request, "A user with this username already exists.")
            return render(request, 'policregister.html')

        # Create a new PolicProfile
        polic_profile = PolicProfile(policeid=policeid, full_name=full_name, email=email, age=age, phone=phone, gender=gender, image=image, status='Pending')
        polic_profile.save()

        # Create a User object
        user = User.objects.create_user(username=policeid, password=password)
        
        # Save the user
        user.save()

        return redirect('policlogin')  # Redirect to the police profile page or any other desired URL   
    return render(request, 'policDash/policregist.html')  # Replace 'your_template.html' with your actual registration template


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import PolicProfile  # Import your PolicProfile model

def polic_login(request):
    if request.method == 'POST':
        policeid = request.POST.get('policeid')  # Update to match the input field name
        password = request.POST.get('password')
        user = authenticate(request, username=policeid, password=password)
        if user is not None:
            polic_profile = PolicProfile.objects.get(policeid=user)  # Retrieve the police's profile
            if polic_profile.status == 'Taken':
                login(request, user)
                # Redirect to the dashboard or any other page upon successful login
                return redirect('home4')  # Change 'index3' to your desired URL
            else:
                messages.error(request, 'Your account status is not "Taken". Please contact the administrator.')
        else:
            messages.error(request, 'Invalid Police ID or password. Please try again or wait for the administrator to approve your account.')

    return render(request, 'policDash/policlog.html')


def polic_logout(request):
    logout(request)
    return redirect('loginoption')


from django.shortcuts import get_object_or_404

@login_required(login_url='/loginoption/')
def poacceptgd(request):
    accept_list = GDForm.objects.filter(status='Taken') 
    return render(request,'policDash/poacceptgd.html', locals())


@login_required(login_url='/loginoption/')
def gdpoview(request,gd_id):
    gd_instance = get_object_or_404(GDForm, gd_id=gd_id)
    return render(request, 'policDash/gdpoview.html', {'gd_instance': gd_instance})


