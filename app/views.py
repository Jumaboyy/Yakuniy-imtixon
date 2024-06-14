from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .serializers import TeacherSerializers, CommentSerializers, CourseSerializers, LessonSerializers, LikeSerializer, LessonVideoSerializers, MailSerializers
from.models import Teacher, Comment, Course, Lesson, Like, LessonVideo
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication



class TeacherView(viewsets.ModelViewSet):
    """ TeacherView """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [permissions.IsAdminUser]

class CommentView(viewsets.ModelViewSet):
    """ CommentView """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.DjangoObjectPermissions]


class CourseView(viewsets.ModelViewSet):
    """ CourseView """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [permissions.IsAdminUser]

class LessonView(viewsets.ModelViewSet):
    """ LessonView """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [permissions.DjangoModelPermissions]
    search_fields = ['title', 'content']
    ordering_fields = ['title']


class LikeAPIview(APIView):
    """ LikeAPIview """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = LikeSerializer()
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data.get('like') == True:
            value = True
        else:
            value = False
        lesson_id = serializer.validated_data.get('lesson')
        lesson = Lesson.objects.get(pk=lesson_id)


        try:
            like = Like.objects.get(
                lesson=lesson,
                user=request.user
            )
            like.delete()
        except:
            pass

        Like.objects.create(
            lesson=lesson,
            user=request.user,
            like_or_dislike=value
        )

        return Response({'success': "Accepted !!!"})





class LessonVideoView(viewsets.ModelViewSet):
    """ LessonVideoView """
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializers
    authentication_classes = (TokenAuthentication,)

class Search(APIView):
    """ Search """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request: Request):
        word=str(request.query_params.get('title',))
        queryset=Lesson.objects.filter(title__icontains=word)
        return Response({'lossons': LessonSerializers(queryset, many=True).data})

class Sendmail(APIView):

    """ Sendmail """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request:Request):
        serializer = MailSerializers()
        return Response(serializer.data)



    def post (self, request: Request):
        serializer = MailSerializers(data=request.data)
        serializer.is_valid()

        users = User.objects.all()

        for user in users:
            subject = serializer.validated_data.get('name')
            message = f'{user.username}{serializer.validated_data.get('email')}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            send_mail(subject, message, email_from, recipient_list)

        return Response({'success': 'Emailga xabar yuborildi !!!'})