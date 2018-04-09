from django.db import models

class MallProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    app_html = models.CharField(max_length=255, blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    cost_price = models.IntegerField(blank=True, null=True)
    count_num = models.BigIntegerField(blank=True, null=True)
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
    product_category_id = models.BigIntegerField(blank=True, null=True)
    product_weight = models.IntegerField(blank=True, null=True)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    up_time = models.DateTimeField(blank=True, null=True)
    verify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_product'

    def to_dict(self):
        data = {}
        for f in self._meta.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)


class MallProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    deleted = models.IntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField(blank=True, null=True)
    prod_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_product_category'
