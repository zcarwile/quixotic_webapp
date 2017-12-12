from rest_framework.routers import DefaultRouter
from quixotic_api.views import EventViewSet, TimeblockViewSet, ProjectViewSet, UserViewSet

router = DefaultRouter()
router.register(prefix='events', viewset=EventViewSet, base_name="events")
router.register(prefix='timeblocks', viewset=TimeblockViewSet, base_name="timeblocks")
router.register(prefix='projects', viewset=ProjectViewSet, base_name="projects")
router.register(prefix='users', viewset=UserViewSet, base_name="users")

urlpatterns = router.urls
