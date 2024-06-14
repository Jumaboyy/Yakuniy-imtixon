from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, Lesson, LessonVideo, Comment, Like, Teacher,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ You can manage the parameters of the course model by displaying them in the admin panel here"""
    list_display = ('id', 'title', 'teacher', 'price',)
    list_display_links = ('id', 'title', 'teacher', 'price',)
    list_filter = ('title', 'teacher', 'price',)
    search_fields = ('title', 'teacher', 'price',)
    ordering = ('pk',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ You can manage the parameters of the lesson model by displaying them in the admin panel here"""
    list_display = ('id', 'course', 'title', 'get_video')
    list_display_links = ('id', 'course', 'title')
    list_filter = ('course', 'title')
    search_fields = ('course__title', 'title')
    ordering = ('pk',)

    def get_video(self, lesson):
        if lesson.video:
            return mark_safe(f'''
                <video width="50" height="50" controls>
                    <source src="{lesson.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return 'No Video'

    get_video.short_description = 'Video'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ You can manage the parameters of the comment model by displaying them in the admin panel here"""
    list_display = ('id', 'author', 'lesson',)
    list_display_links = ('id', 'author', 'lesson',)
    list_filter = ('author', 'lesson', )
    search_fields = ('author', 'lesson',)
    ordering = ('pk',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """ You can manage the parameters of the teacher model by displaying them in the admin panel here"""
    list_display = ('id', 'full_name', 'get_image', 'experience', 'level',)
    list_display_links = ('id', 'full_name', 'get_image', 'experience', 'level',)
    list_filter = ('full_name','experience', 'level',)
    search_fields = ('full_name', 'experience', 'level',)
    ordering = ('pk',)

    def get_image(self, teacher):
        if teacher.photo:
            return mark_safe(f'<img src="{teacher.photo.url}" width="50" height="50" />')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ You can manage the parameters of the category model by displaying them in the admin panel here"""
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('pk',)
