from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('country',CounrtyViewsets,basename='country')
router.register('league',LeagueViewsets,basename='league')
router.register('characteristic',CharacteristicViewsets,basename='characteristic')
router.register('footballClub',FootballClubViewsets,basename='footballClub')

urlpatterns = router.urls