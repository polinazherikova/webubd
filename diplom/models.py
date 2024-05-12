from django.db import models

class Calculator(models.Model):
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    CONCRETE_CHOICES = [
        ('C8/10', 'C8/10 (3500 UAH/m³)'),
        ('C15/20', 'C15/20 (3800 UAH/m³)'),
        ('C25/30', 'C25/30 (4000 UAH/m³)'),
    ]
    concrete_type = models.CharField(max_length=50, choices=CONCRETE_CHOICES, default='C8/10')

    def get_volume(self):
        return self.width * self.height * self.length

    def get_concrete_price(self):
        for choice in self.CONCRETE_CHOICES:
            if choice[0] == self.concrete_type:
                price_str = choice[1].split('(')[-1].split(' ')[0]
                try:
                    price = float(price_str)
                    return price
                except ValueError:
                    pass
        return None

    def get_concrete_amount(self):
        volume = self.get_volume() / 1000000
        price_per_meter = self.get_concrete_price()
        if price_per_meter is not None:
            return volume * price_per_meter
        return None

    def __str__(self):
        return f"Block ({self.width}x{self.height}x{self.length}) - {self.concrete_type}"

    class Meta:
        verbose_name="Блок"
        verbose_name_plural = "Блоки"

class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    question = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name="Питання"
        verbose_name_plural = "Питання"

class QuickContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Швидкий зв'язок"
        verbose_name_plural = "Швидкий зв'язок"

class Feedback(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

