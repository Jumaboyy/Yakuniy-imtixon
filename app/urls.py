from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import TeacherView, CommentView, CourseView, LikeAPIview, LessonView, LessonVideoView,Search, Sendmail


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register('teacher', TeacherView)
router.register('comment', CommentView)
router.register('course', CourseView)
router.register('lesson', LessonView)
router.register('lesson-video', LessonVideoView)


schema_view = get_schema_view(
   openapi.Info(
      title="Kurslar API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jumaboynematov280@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('djoser-auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('search/', Search.as_view()),
    path('send-mail/', Sendmail.as_view()),
    path('like/', LikeAPIview.as_view()),
 ]

