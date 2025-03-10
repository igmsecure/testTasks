# Generated by Django 5.1.7 on 2025-03-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=255)),
                ('recipient_name', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('origin_index', models.IntegerField()),
                ('destination_index', models.IntegerField()),
                ('letter_type', models.IntegerField(choices=[(1, 'Письмо'), (2, 'Заказное письмо'), (3, 'Ценное письмо'), (4, 'Экспресс-письмо')])),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=255)),
                ('recipient_name', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('origin_index', models.IntegerField()),
                ('destination_index', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('package_type', models.IntegerField(choices=[(1, 'Мелкий пакет'), (2, 'Посылка'), (3, 'Посылка 1 класса'), (4, 'Ценная посылка'), (5, 'Посылка международная'), (6, 'Экспресс-посылка')])),
                ('payment_amount', models.FloatField()),
            ],
        ),
    ]
