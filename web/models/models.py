from __future__ import unicode_literals

from django.db import models


class OrderModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    user_id = models.BigIntegerField()
    order_num = models.CharField(max_length=100)

    # model的字符串表现形式 类似java的.toString
    def __str__(self):
        return '订单号:'+self.order_num

    # 在Model中
    class Meta:
        db_table = "order_model"  # 更改表名

class article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    # model的字符串表现形式
    def __str__(self):
        return '标题:'+self.title
    # 在Model中
    class Meta:
        db_table = "article"  # 更改表名