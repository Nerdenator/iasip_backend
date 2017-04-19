from django.db import models


class Crimes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    criminal_charge = models.CharField(max_length=500, blank=False, default='')
    degree = models.CharField(max_length=50, blank=True, default='')
    charge_type = models.CharField(max_length=50, blank=True, default='')
    jurisdiction = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        super(Crimes, self).save(*args, **kwargs)

    def __str__(self):
        return self.criminal_charge

    class Meta:
        ordering = ('criminal_charge',)


class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    preferred_name = models.CharField(max_length=100, blank=False, default='')
    crimes = models.ManyToManyField(Crimes, null=True, through='CharacterCrime')

    def save(self, *args, **kwargs):
        super(Character, self).save(*args, **kwargs)

    def __str__(self):
        return self.preferred_name

    class Meta:
        ordering = ('preferred_name',)


class CharacterCrime(models.Model):
    """Crime as committed by a character"""
    character = models.ForeignKey(Character)
    crime = models.ForeignKey(Crimes)
    season = models.IntegerField()
    episode = models.IntegerField()

    def __str__(self):
        return '{}.{}: {}- {}'.format(self.season, self.episode, self.character, self.crime)

    def save(self, *args, **kwargs):
        super(CharacterCrime, self).save(*args, **kwargs)