from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register(r'posts', views.PostViewSet)


urlpatterns = [
    
]


urlpatterns += router.urls
