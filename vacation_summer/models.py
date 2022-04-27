from django.db import models


class Vacations(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    web_url = models.CharField(max_length=500)
    image = models.CharField(max_length=260)

    def __str__(self):
        return self.title, self.description, self.phone, self.web_url, self.image

    class Meta:
        db_table = 'sites_vacation'
