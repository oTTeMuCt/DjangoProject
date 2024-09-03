from django.db import models


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    photo = models.ImageField(upload_to='reviews_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.name} - Rating: {self.rating}'

    def get_rating_display(self):
        return "★" * self.rating
