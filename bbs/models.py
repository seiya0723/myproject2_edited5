from django.db import models
from django.utils import timezone

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    title = models.CharField(verbose_name="タイトル", max_length=100, default="")
    comment = models.CharField(verbose_name="コメント", max_length=2000)
    price = models.IntegerField(verbose_name="金額", null=True)
    salary = models.IntegerField(verbose_name="収入", null=True)
    spending = models.IntegerField(verbose_name="支出", null=True)
    dt = models.DateTimeField(verbose_name="投稿日", default=timezone.now)


    pay_dt  = models.DateTimeField(verbose_name="決済日")

    def __str__(self):
        return self.comment
