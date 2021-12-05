from django.db import models

# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.name

class States(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, models.DO_NOTHING,related_name='statesofcountry', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'

    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey('States', models.DO_NOTHING,related_name='citiesofstate', blank=True, null=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

    def __str__(self):
        return self.name
