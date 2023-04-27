from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    genre = models.CharField(max_length=100, blank=True, null=True)
    collection_in_mil = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'movies'




class Ratings(models.Model):
    movie = models.OneToOneField(Movies, models.DO_NOTHING, primary_key=True)
    reviewer = models.ForeignKey('Reviewers', models.DO_NOTHING)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'
        unique_together = (('movie', 'reviewer'),)


class Reviewers(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.first_name +   self.last_name )

    class Meta:
        managed = False
        db_table = 'reviewers'
