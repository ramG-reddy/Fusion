from applications.academic_information.api.serializers import CourseSerializer
from applications.academic_procedures.models import (
    BranchChange,
    CourseSlot,
    FinalRegistration,
    FinalRegistrations,
    InitialRegistration,
    InitialRegistrations,
    Semester,
    SemesterMarks,
    StudentRegistrationChecks,
    ThesisTopicProcess,
    course_registration,
)
from applications.programme_curriculum.models import Course
from rest_framework import serializers


class ThesisTopicProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThesisTopicProcess
        fields = "__all__"


class InitialRegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialRegistrations
        fields = "__all__"


class FinalRegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalRegistrations
        fields = "__all__"


class InitialRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialRegistration
        fields = "__all__"


class FinalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalRegistration
        fields = "__all__"


class StudentRegistrationChecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistrationChecks
        fields = "__all__"


class SemesterMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterMarks
        fields = "__all__"


class BranchChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchChange
        fields = "__all__"


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_registration
        fields = "__all__"


class CourseSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSlot
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "code", "name", "credit"]
