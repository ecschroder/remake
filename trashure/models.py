from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.translation import ugettext_lazy as _


ERA_CHOICES = (
    ('Childhood', _('Childhood')),
    ('High_School', _('High School')),
    ('College', _('College')),
    ('Adult', _('Adult')),
    ('unknown', _('unknown')),
)


class KnickKnack(models.Model):
    name = models.CharField(max_length=200)
    photo = ImageField(upload_to='../media', height_field=None, width_field=None)
    description = models.TextField()
    memory = models.TextField()
    year = models.DateField('year acquired')
    era = models.CharField(max_length=20, choices=ERA_CHOICES)
    pub_date = models.DateTimeField('date published', auto_now=True)
    votes_treasure = models.IntegerField(default=0)
    votes_trash = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.score = self.votes_treasure - self.votes_trash
        super(KnickKnack, self).save(*args, **kwargs)
