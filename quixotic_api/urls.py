from rest_framework.routers import DefaultRouter
from quixotic_api.views import EventViewSet, TimeblockViewSet, ProjectViewSet, UserViewSet

router = DefaultRouter()
router.register(prefix='events', viewset=EventViewSet)
router.register(prefix='timeblocks', viewset=TimeblockViewSet)
router.register(prefix='projects', viewset=ProjectViewSet)
router.register(prefix='users', viewset=UserViewSet)

urlpatterns = router.urls
