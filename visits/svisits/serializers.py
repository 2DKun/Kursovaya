from rest_framework import serializers
from svisits.models import Student, Visits


class SSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        friends = ('student_id', 'name', 'surname', 'patronymic', 'group', 'gender')


class VSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        friends = ('visits_id', 'student_id', 'date')