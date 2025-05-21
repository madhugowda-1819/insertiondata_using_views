from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField()
    url=models.URLField()
    email=models.EmailField(default='msm875990@gmail.com')

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    author=models.CharField()
    date=models.DateField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.author
 