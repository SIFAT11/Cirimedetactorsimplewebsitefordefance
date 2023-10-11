from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import GDForm, Profile
from django.contrib import auth
from django.contrib.auth import login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid

def home(request):
    totalGd = GDForm.objects.all().count()
    totalacceptedGd = GDForm.objects.filter(status='Taken').count()
    totalrejectedGd = GDForm.objects.filter(status='Rejected').count()
    totalpendingGd = GDForm.objects.filter(status='Pending').count()
    return render(request,'index.html',locals())

def loginoption(request):
    return render(request,'userdash/loginoption.html')



@login_required(login_url='login')
def GD(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        full_name = request.POST.get('full_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        email = request.POST.get('email')
        district = request.POST.get('district')
        sub_district = request.POST.get('sub_district')
        village = request.POST.get('village')
        national_id = request.POST.get('national_id')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        gd_date = request.POST.get('gd_date')
        subject = request.POST.get('subject')
        incident_details = request.POST.get('incident_details')

        # Create a new GDForm object and save it
        gd_form = GDForm(
            full_name=full_name,
            father_name=father_name,
            mother_name=mother_name,
            email=email,
            district=district,
            sub_district=sub_district,
            village=village,
            national_id=national_id,
            birth_date=birth_date,
            gender=gender,
            gd_date=gd_date,
            subject=subject,
            incident_details=incident_details,
        )
        gd_form.save()

        # Generate a success message
        messages.success(request, 'GD Form submitted successfully!')
        return redirect('GD') 
    else:
        # Render the GDForm template
        return render(request, 'userdash/Gd.html')



def Register(request):
    if request.method == 'POST':
        # Get user registration data from the form
        username = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST.get('email')
        age = request.POST['age']
        phone = request.POST['phone']
        image = request.FILES.get('image') 
        gender = request.POST['gender']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        # Check if passwords match and meet length requirements
        if password != repassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        elif len(password) < 8 or len(password) > 10:
            messages.error(request, 'Password must be between 8 and 10 characters.')
            return redirect('register')

        # Check if the email already exists
        if Profile.objects.filter(email=email).exists():
            messages.error(request, 'This email address is already registered. Please use a different email.')
            return redirect('register')

        try:
            # Create a new user and profile
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile(
                user=user,
                email=email,
                full_name=full_name,
                age=age,
                phone=phone,
                image=image,
                gender=gender
            )
            profile.save()

            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('register')
    return render(request,'userdash/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed auth_login function
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'userdash/login.html')



def log_out(request):
    logout(request)
    messages.error(request, 'logout success.')
    return redirect('loginoption')

def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        new_pass = request.POST['new_pass']

        try:
            user = User.objects.get(username=username)
            if user.email == email:
                user.set_password(new_pass)
                user.save()
                update_session_auth_hash(request, user)
                print(new_pass)
                messages.success(request, 'Reset password is successful')
                return redirect('login')
            else:
                messages.error(request, 'Email does not match.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
    return render(request, 'userdash/reset.html')


@login_required(login_url='login')
def TotalGD(request):
    gd_list = GDForm.objects.all()
    return render(request, 'userdash/TotalGD.html', {'gd_list': gd_list})