from django.db import models


class Letter(models.Model):
    LETTER_TYPES = [
        (1, "Письмо"),
        (2, "Заказное письмо"),
        (3, "Ценное письмо"),
        (4, "Экспресс-письмо"),
    ]

    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    origin_index = models.IntegerField()
    destination_index = models.IntegerField()
    letter_type = models.IntegerField(choices=LETTER_TYPES)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.sender_name} -> {self.recipient_name} ({self.get_letter_type_display()})"


class Package(models.Model):
    PACKAGE_TYPES = [
        (1, "Мелкий пакет"),
        (2, "Посылка"),
        (3, "Посылка 1 класса"),
        (4, "Ценная посылка"),
        (5, "Посылка международная"),
        (6, "Экспресс-посылка"),
    ]

    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    origin_index = models.IntegerField()
    destination_index = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    package_type = models.IntegerField(choices=PACKAGE_TYPES)
    payment_amount = models.FloatField()

    def __str__(self):
        return f"{self.sender_name} -> {self.recipient_name} ({self.get_package_type_display()})"
