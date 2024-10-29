# from django import forms
# from .models import Schedule
# from .models import Article
# from .models import Patient
# from .models import Doctor, Department, UserModel
# from django.contrib.auth.models import User
# from .models import Role
# from .models import MedicalRecord
#
# class ScheduleRequestForm(forms.ModelForm):
#     class Meta:
#         model = Schedule
#         fields = ['time', 'patient_name']
#
# class ArticleRequestForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title', 'content', 'author']
#
# class AuthenticationRequestForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#
# class DepartmentRequestForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = ['name_department', 'description_department', 'location']
#
#
# class DoctorRequestForm(forms.ModelForm):
#     department_id = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department')
#     user_id = forms.ModelChoiceField(queryset=UserModel.objects.all(), label='User')
#
#     class Meta:
#         model = Doctor
#         fields = ['position', 'description', 'room_address', 'service_prices', 'department_id', 'user_id']
#
# class MedicalRecordRequestForm(forms.ModelForm):
#     class Meta:
#         model = MedicalRecord
#         fields = ['id', 'diagnosis']
#
# class PasswordCheckRequestForm(forms.Form):
#     input_password = forms.CharField(widget=forms.PasswordInput)
#     encoded_password = forms.CharField(widget=forms.PasswordInput)
#
# class PatientUpdateRequestForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['nhommau', 'cannang', 'chieucao', 'benhnen']
#
#
# class RegisterRequestForm(forms.ModelForm):
#     role = forms.ModelChoiceField(queryset=Role.objects.all(), label='Role')
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'phone', 'role']
#         widgets = {
#             'password': forms.PasswordInput(),
#             'birthday': forms.DateInput(attrs={'type': 'date'}),
#         }
