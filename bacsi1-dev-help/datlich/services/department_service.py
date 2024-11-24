# from datetime import date, timedelta
# from ..serializers import *
#
# class DepartmentService:
#     @staticmethod
#     def create_department(data):
#         serializer = DepartmentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return serializer.data
#         return serializer.errors
#
#     @staticmethod
#     def get_all_departments():
#         departments = Department.objects.all()
#         return DepartmentSerializer(departments, many=True).data
#
#     @staticmethod
#     def get_department_by_id(department_id):
#         try:
#             department = Department.objects.get(id=department_id)
#             return DepartmentSerializer(department).data
#         except Department.DoesNotExist:
#             return None
#
#     @staticmethod
#     def get_doctors_by_department(department_id, add_schedule=False):
#         try:
#             department = Department.objects.get(id=department_id)
#             doctors = department.doctors.all()
#             doctor_data = DoctorSerializer(doctors, many=True).data
#
#             if add_schedule:
#                 for doctor in doctor_data:
#                     doctor['schedules'] = ScheduleSerializer(
#                         Schedule.objects.filter(doctor_id=doctor['id']),
#                         many=True
#                     ).data
#
#             return doctor_data
#         except Department.DoesNotExist:
#             return []
#
#     @staticmethod
#     def list_doctors_today(department_id):
#         today = date.today()
#         now = date.today()
#
#         doctors = DepartmentService.get_doctors_by_department(department_id, add_schedule=True)
#         available_doctors = []
#
#         for doctor in doctors:
#             schedules_today = [schedule for schedule in doctor['schedules'] if schedule['date'] == today]
#             if any(shift['time_start'] > now for shift in schedules_today):
#                 available_doctors.append(doctor)
#
#         return available_doctors
#
#     @staticmethod
#     def list_doctors_tomorrow(department_id):
#         tomorrow = date.today() + timedelta(days=1)
#         doctors = DepartmentService.get_doctors_by_department(department_id, add_schedule=True)
#
#         available_doctors = [
#             doctor for doctor in doctors
#             if any(schedule['date'] == tomorrow for schedule in doctor['schedules'])
#         ]
#
#         return available_doctors
from datlich.models import Department

class DepartmentService:
    def get_all_departments(self):
        return Department.objects.all()

    def get_department_by_id(self, department_id):
        try:
            return Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            return None
    def get_doctors_by_department(self, department_id, search_query=None):
        try:
            department = Department.objects.get(id=department_id)

            doctors = department.list_doctors.select_related('user', 'department').all()

            if search_query:
                doctors = doctors.filter(user__fullname__icontains=search_query)

            return [
                {
                    "id": doctor.id,
                    "position": doctor.position,
                    "description": doctor.description,
                    "room_address": doctor.room_address,
                    "service_prices": doctor.service_prices,
                    "department": {
                        "id": doctor.department.id,
                        "name": doctor.department.name_department
                    },
                    "user": {
                        "id": doctor.user.id,
                        "fullname": doctor.user.fullname,
                        "email": doctor.user.email,
                        "telephone": doctor.user.telephone,
                        "gender": doctor.user.gender,
                    }
                }
                for doctor in doctors
            ]
        except Department.DoesNotExist:
            return []