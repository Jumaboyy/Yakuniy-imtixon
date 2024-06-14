from  rest_framework import serializers
from .models import Teacher, Course, Comment, Lesson,LessonVideo,Category,Like

class TeacherSerializers(serializers.ModelSerializer):
    """Accepts all parameters in the learner model"""
    class Meta:
        model = Teacher
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    """Accepts all parameters in the category model"""
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    """"Annotation accepts all parameters in the model"""
    class Meta:
        model = Comment
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    """Accepts all parameters in the course model"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    """Accepts all parameters in the class model"""
    class Meta:
        model = Lesson
        fields = '__all__'

class LikeSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()


class LessonVideoSerializers(serializers.ModelSerializer):
    """Accepts all parameters in the lesson video model"""
    class Meta:
        model = LessonVideo
        fields = '__all__'


class MailSerializers(serializers.Serializer):
    """Serializers for e-mail"""
    name = serializers.CharField(max_length=255)
    text = serializers.CharField()