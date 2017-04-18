from django.db import models


class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    preferred_name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='characters', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Character, self).save(*args, **kwargs)

    class Meta:
        ordering = ('preferred_name',)


class Crime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    criminal_charge = models.CharField(max_length=500, blank=False, default='')
    degree = models.CharField(max_length=50, blank=True, default='')
    charge_class = models.CharField(max_length=10, blank=True, default='')
    charge_type = models.CharField(max_length=50, blank=True, default='')
    jurisdiction = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='crimes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Crime, self).save(*args, **kwargs)

    class Meta:
        ordering = ('criminal_charge',)
