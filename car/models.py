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

    def add_rate(self, rate):
        """Add rate to car."""
        self.rates.create(rate=rate)
        self.save()


class Rate(models.Model):
    """Model definition for Rate."""

    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, verbose_name="Car", on_delete=models.CASCADE, related_name="rates")
    rate = models.SmallIntegerField(verbose_name="Rate")

    class Meta:
        """Meta definition for Rate."""

        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):
        """Unicode representation of Rate."""
        return f"{self.car} : {self.rate}"

