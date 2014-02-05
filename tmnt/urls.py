from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from rest_framework.response import Response

from tmnt.models import Character, Team
from tmnt.serializers import TeamSerializer

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
  model = Character
class TeamListViewSet(viewsets.ModelViewSet):
  model = Team
class TeamViewSet(viewsets.ModelViewSet):
  def list(self, request, pk):
    queryset = Team.objects.filter(id=pk)
    serializer = TeamSerializer(queryset, many=True)
    return Response(serializer.data)

router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^team/$', TeamListViewSet.as_view({
    'get': 'list'
    })),
    url(r'^team/(?P<pk>[0-9]+)/$', TeamViewSet.as_view({
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
