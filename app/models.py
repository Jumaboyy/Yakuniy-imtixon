from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """This model accepts passer parameters. That is, the teacher's degree, picture, full name and surname
        This teacher accepts work experience"""

    LEVEL_CHOICES = [
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    photo = models.ImageField(upload_to='teachers/')
    full_name = models.CharField(max_length=100, verbose_name='Full Name/Familya-Ism', blank=True)
    experience = models.IntegerField(help_text="Ish tajribasi",verbose_name='experience/ish tajribasi')
    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, verbose_name='Level/Daraja')

    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category/Kategoriya')

class Course(models.Model):
    """This model accepts the course parameters. It shows the course belonging to the category. That is, the subject
        of the course, accepts a brief explanation, which teacher gave the lesson and the price of the course"""

    title = models.CharField(max_length=255, verbose_name='Course')
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, related_name='teacher_courses', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(verbose_name='price', default=None)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Touching the course accepts the parameters of the lessons, i.e. the textbook to which the course is connected,
        accepts the topic of this lesson, a brief explanation, a lesson video """

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='title', blank=True)
    content = models.TextField()
    video = models.FileField(blank=True, null=True, verbose_name='video')


    def __str__(self):
        return self.title


class LessonVideo(models.Model):
     """This model is needed for lesson video parameters. Which lesson video (lesson topic) and
        accepted the video format (mp4 etc.) """


     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
     video = models.FileField(upload_to='lesson/videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'wmv']) ])

     def __str__(self):
        return self.lesson.title


class Comment(models.Model):
    """Comments are left for this lesson in the Commentary model. This model is linked to the Lesson model.
    Comments are accepted by whoever leaves them Depends on the user"""

    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE,verbose_name='Lesson comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.author.username} on {self.lesson.title}'


class Like(models.Model):
    """The evaluation model evaluates the lesson (likes and dislikes)
        The model parameters accept which lesson was graded, who graded it, and the grade"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} liked {self.lesson.title}'