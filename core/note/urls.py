from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('tag',TagView)
router.register('',NoteView)

urlpatterns = [
] + router.urls