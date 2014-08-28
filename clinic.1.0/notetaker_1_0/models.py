from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
import django_filters


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    USER_TYPES = (
        ('P', 'PATIENT'),
        ('R', 'PROVIDER'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    
    def __unicode__(self):
        return "%s's profile" % self.user
    
def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User, dispatch_uid='autocreate_UserProfile')


        
class Patient(models.Model):
    patient_name = models.ForeignKey(UserProfile)
    adrs = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    
class Provider(models.Model):
    SPECIALITY_TYPES = (
        ('1', 'DERMATOLOGY'),
        ('2', 'ANESTHESIOLOGY'),
        ('3', 'PHYSICAL MEDICINE AND REHABILITATION'),
        ('4', 'FAMILY MEDICINE'),
        ('5', 'INTERNAL MEDICINE'),
        ('6', 'GYNECOLOGY'),
        ('7', 'PEDIATRICS'),
        ('8', 'OPHTHALMOLOGY'),
        ('9', 'RADIOLOGY'),
    )
    provider_name = models.ForeignKey(UserProfile)
    speciality = models.CharField(max_length=1, choices=SPECIALITY_TYPES)
    provider_code = models.IntegerField()
    


class Note(models.Model):
    title=models.CharField(max_length=120, null=True, blank=True)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    patient_id = models.ForeignKey(UserProfile, null=True, related_name='PATIENT')
    Provider_id = models.ForeignKey(UserProfile, null=True, related_name='PROVIDER')
    def __unicode__(self):
        return smart_unicode(self.title)

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ['patient_id', 'date', 'title']
    

    
