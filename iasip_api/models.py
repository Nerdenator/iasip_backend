from django.db import models


class Crimes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    criminal_charge = models.CharField(max_length=500, blank=False, default='')
    degree = models.CharField(max_length=50, blank=True, default='')
    charge_class = models.CharField(max_length=10, blank=True, default='')
    charge_type = models.CharField(max_length=50, blank=True, default='')
    jurisdiction = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='crime', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Crimes, self).save(*args, **kwargs)

    class Meta:
        ordering = ('criminal_charge',)


class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    preferred_name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='characters', on_delete=models.CASCADE)
    crimes = models.ManyToManyField(Crimes, null=True, through='CharacterCrime')

    def save(self, *args, **kwargs):
        super(Character, self).save(*args, **kwargs)

    class Meta:
        ordering = ('preferred_name',)


class CharacterCrime(models.Model):
    """Crimes as committed by a character"""
    character = models.ForeignKey(Character)
    crime = models.ForeignKey(Crimes)
    season = models.CharField(max_length=3)
    episode = models.CharField(max_length=3)

    def save(self, *args, **kwargs):
        super(CharacterCrime, self).save(*args, **kwargs)

