from django.db import models


class MallProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    app_html = models.CharField(max_length=255, blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    cost_price = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    detail_html = models.CharField(max_length=255, blank=True, null=True)
    down_time = models.DateTimeField(blank=True, null=True)
    ext_desc1 = models.CharField(max_length=255, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    group_price = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    is_verify = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    ori_price = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_category_id = models.ForeignKey('MallProductCategory', on_delete=models.CASCADE, )
    product_weight = models.IntegerField(blank=True, null=True)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    up_time = models.DateTimeField(blank=True, null=True)
    verify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'mall_product'


class MallProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    deleted = models.IntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField(blank=True, null=True)
    prod_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'mall_product_category'


class MallProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    cancel_time = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    from_way = models.IntegerField(blank=True, null=True)
    group_order_id = models.BigIntegerField(blank=True, null=True)
    group_status = models.IntegerField(blank=True, null=True)
    order_comm = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(unique=True, max_length=30, blank=True, null=True)
    order_type = models.IntegerField(blank=True, null=True)
    ori_price = models.BigIntegerField(blank=True, null=True)
    over_time = models.DateTimeField(blank=True, null=True)
    pay_online = models.IntegerField(blank=True, null=True)
    pay_order_no = models.CharField(max_length=255, blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    product_id = models.ForeignKey('MallProduct', on_delete=models.CASCADE,blank=False, null=False )
    product_image = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_num = models.IntegerField(blank=True, null=True)
    receive_addr = models.CharField(max_length=255, blank=True, null=True)
    receive_name = models.CharField(max_length=255, blank=True, null=True)
    receive_phone = models.CharField(max_length=255, blank=True, null=True)
    refund_no = models.CharField(max_length=255, blank=True, null=True)
    refund_reason = models.CharField(max_length=255, blank=True, null=True)
    refund_status = models.IntegerField(blank=True, null=True)
    refund_time = models.DateTimeField(blank=True, null=True)
    send_code = models.CharField(max_length=255, blank=True, null=True)
    send_fee = models.BigIntegerField(blank=True, null=True)
    send_time = models.CharField(max_length=255, blank=True, null=True)
    send_type = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    take_time = models.DateTimeField(blank=True, null=True)
    total_price = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mall_product_order'
