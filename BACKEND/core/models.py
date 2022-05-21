from django.db import models
import secrets

# Create your models here.
class  Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    verified = models.BooleanField(defaullt = False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

        def __str__(self):
            return f"Payment: {self.amount}"

        def save(self, *args, **kwargs):
            while not self.ref:
                ref = secrets.token_urlsafe(50)
                object_with_similar_ref = Payment.objects.filter(ref = ref)
                if not object_with_similar_ref:
                    self.ref = ref
            super().save(*args, **kwargs)

        def amount_value(self) -> int:
            return self.amount * 100