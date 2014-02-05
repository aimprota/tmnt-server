from django.db import models

class Team(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ('name',)

class Character(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  team = models.ForeignKey(Team, related_name='characters')
  name = models.CharField(max_length=100)

  class Meta:
    ordering = ('name',)

  def __unicode__(self):
    return u'{}'.format(self.name)
