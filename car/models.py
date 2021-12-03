from django.db import models


class Car(models.Model):
    """Model definition for Car."""

    id = models.AutoField(primary_key=True)
    make = models.CharField(verbose_name="Make", max_length=200)
    model = models.CharField(verbose_name="Model", max_length=200)

    class Meta:
        """Meta definition for Car."""

        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        """Unicode representation of Car."""
        return f"{self.make} {self.model}"
