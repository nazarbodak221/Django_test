from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TimeEntryViewSet


router=DefaultRouter()

router.register("timeentries", TimeEntryViewSet, basename='timeentry')

urlpatterns = [
    path('api/', include(router.urls)),
]