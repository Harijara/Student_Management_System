from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import students
from .form import student_form
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import students, Attendance, Marks
from .form import AttendanceForm, MarksForm

@login_required
def student_dashboard(request):
    if request.user.is_superuser:
        return redirect('std_lst') 
    current_user = request.user
    try:
        student = students.objects.get(user=current_user)  # assuming you linked student to user
        marks = Marks.objects.filter(student=student)
        present_count = Attendance.objects.filter(student=student, status="Present").count()
        absent_count = Attendance.objects.filter(student=student, status="Absent").count()

    
    except students.DoesNotExist:
        return HttpResponse("no user")  # optional fallback

    context = {
        'student': student,
        'present': present_count,
        'absent': absent_count,
        'marks': marks,
    }
    return render(request, 'dashboard.html', context)

@staff_member_required
def add_attendance(request, student_id):
    student = students.objects.get(id=student_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = student
            attendance.save()
            messages.success(request, 'Attendance added successfully!')
            return redirect('std_lst')
    else:
        form = AttendanceForm()
    return render(request, 'add_attendance.html', {'form': form, 'student': student})

@staff_member_required
def add_marks(request, student_id):
    student = students.objects.get(id=student_id)
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.student = student
            mark.save()
            messages.success(request, 'Marks added successfully!')
            return redirect('std_lst')
    else:
        form = MarksForm()
    return render(request, 'add_marks.html', {'form': form, 'student': student})


def is_admin(user):
    return user.is_superuser

@login_required
def students_lst(request):
    query = request.GET.get('search', '')
    student_data = students.objects.all()

    if query:
        student_data = student_data.filter(
            Q(name__icontains=query) |
            Q(roll__icontains=query) |
            Q(branch__icontains=query)
        )

    paginator = Paginator(student_data, 10)
    page = request.GET.get('page')
    student_data = paginator.get_page(page)

    return render(request, 'students_list.html', {
        'students': student_data,
        'search_query': query
    }
    )
@user_passes_test(is_admin)
def add_student(request):
    if request.method=="POST":
        form=student_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully!")
            return redirect("std_lst")
        else:
            messages.error(request, 'Form is invalid. Please check again.')
            return render(request, 'students_list.html', {'form': form}) 
        
    else:
        form=student_form()
        return render(request,"student_form.html",{'form':form ,'action':'add_data'})

def edit_student(request,id):
    student=get_object_or_404(students,id=id)
    if request.method=='POST':
        form=student_form(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect("std_lst")
    else:
        form=student_form(instance=student)
        return render(request,"student_form.html",{'form':form,'action':'edit_data'})
    
def delete(request,id):
    dlt=get_object_or_404(students,id=id)
    dlt.delete()
    messages.success(request, "Student Deleted Successfully!")
    return redirect("std_lst")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully! Please login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})













            

