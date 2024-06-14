from django.db import models


class DocumentApiModel(models.Model):
    title = models.CharField(max_length=70)
    url = models.URLField()
    description = models.TextField()
    code = models.TextField()

    def __str__(self):
        return f"{self.title}"
