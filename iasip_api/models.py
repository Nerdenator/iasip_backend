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
