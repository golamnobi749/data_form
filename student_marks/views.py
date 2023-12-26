from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import Student_Registration
from . models import Student_info

# Create your views here.
def student(request):
    if request.method == 'POST':
        student = Student_Registration(request.POST)
        if student.is_valid():
            print('valid form')
            student_name = student.cleaned_data['student_name']
            father_name = student.cleaned_data['father_name']
            mother_name = student.cleaned_data['mother_name']
            bangla = student.cleaned_data['bangla']
            english = student.cleaned_data['english']
            math = student.cleaned_data['math']
            social_science = student.cleaned_data['social_science']
            general_science = student.cleaned_data['general_science']
            religion = student.cleaned_data['religion']
            point = student.cleaned_data['point']
            email = student.cleaned_data['email']
            password = student.cleaned_data['password']
            confirm_password = student.cleaned_data['confirm_password']
            text_area = student.cleaned_data['text_area']
            info_student = Student_info (student_name=student_name,father_name=father_name,mother_name=mother_name,bangla=bangla,english=english,math=math,social_science=social_science,general_science=general_science,religion=religion,point=point,email=email,password=password,confirm_password=confirm_password,text_area=text_area)
            info_student.save()


            return HttpResponseRedirect('/successfully/')
    else:
        student = Student_Registration(auto_id = True)
        print(student)
        print('Excute GET')
    return render(request,'students/student.html',{'student':student})
def submit(request):
    return render(request, 'students/submit.html')
