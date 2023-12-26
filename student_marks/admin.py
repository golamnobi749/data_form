from django.contrib import admin
from .models import Student_info

# Register your models here.
class Student_Info(admin.ModelAdmin):
   
   list_display = ('student_name', 'father_name','mother_name','bangla','math','english','social_science','general_science','religion','point','email','password','confirm_password','text_area')

admin.site.register(Student_info, Student_Info)

    

