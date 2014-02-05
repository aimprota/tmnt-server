from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers

from tmnt.models import Character, Team
from tmnt.serializers import TeamSerializer

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
  model = Character
class BasicTeamViewSet(viewsets.ModelViewSet):
  model = Team
class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^team/$', BasicTeamViewSet.as_view({
    'get': 'list'
    })),
    url(r'^team/.+', TeamViewSet.as_view({
    'get': 'list'
    }))
    # Examples:
    # url(r'^$', 'smurfs.views.home', name='home'),
    # url(r'^smurfs/', include('smurfs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
