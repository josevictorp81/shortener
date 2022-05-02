from django.db import models

class Links(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.short_link
