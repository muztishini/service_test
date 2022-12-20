from django.db import models


class Kits(models.Model):
    kits_text = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Набор"
        verbose_name_plural = "Наборы"


class Riddle(models.Model):
    kits = models.ForeignKey(
        Kits, on_delete=models.CASCADE, null=True, blank=True)
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
