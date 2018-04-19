# Generated by Django 2.0.3 on 2018-04-12 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MallProduct',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField()),
                ('app_html', models.CharField(blank=True, max_length=255, null=True)),
                ('available', models.IntegerField(blank=True, null=True)),
                ('cost_price', models.IntegerField(blank=True, null=True)),
                ('deleted', models.IntegerField(blank=True, null=True)),
                ('detail_html', models.CharField(blank=True, max_length=255, null=True)),
                ('down_time', models.DateTimeField(blank=True, null=True)),
                ('ext_desc1', models.CharField(blank=True, max_length=255, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('group_price', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('is_verify', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('ori_price', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('product_weight', models.IntegerField(blank=True, null=True)),
                ('short_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=255, null=True)),
                ('up_time', models.DateTimeField(blank=True, null=True)),
                ('verify_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mall_product',
            },
        ),
        migrations.CreateModel(
            name='MallProductCategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField()),
                ('deleted', models.IntegerField(blank=True, null=True)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
                ('prod_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'mall_product_category',
            },
        ),
        migrations.CreateModel(
            name='MallProductOrder',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField()),
                ('cancel_time', models.DateTimeField(blank=True, null=True)),
                ('del_field', models.IntegerField(blank=True, db_column='del', null=True)),
                ('from_way', models.IntegerField(blank=True, null=True)),
                ('group_order_id', models.BigIntegerField(blank=True, null=True)),
                ('group_status', models.IntegerField(blank=True, null=True)),
                ('order_comm', models.CharField(blank=True, max_length=255, null=True)),
                ('order_id', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('order_type', models.IntegerField(blank=True, null=True)),
                ('ori_price', models.BigIntegerField(blank=True, null=True)),
                ('over_time', models.DateTimeField(blank=True, null=True)),
                ('pay_online', models.IntegerField(blank=True, null=True)),
                ('pay_order_no', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_status', models.IntegerField(blank=True, null=True)),
                ('pay_time', models.DateTimeField(blank=True, null=True)),
                ('product_image', models.CharField(blank=True, max_length=255, null=True)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_num', models.IntegerField(blank=True, null=True)),
                ('receive_addr', models.CharField(blank=True, max_length=255, null=True)),
                ('receive_name', models.CharField(blank=True, max_length=255, null=True)),
                ('receive_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_no', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_status', models.IntegerField(blank=True, null=True)),
                ('refund_time', models.DateTimeField(blank=True, null=True)),
                ('send_code', models.CharField(blank=True, max_length=255, null=True)),
                ('send_fee', models.BigIntegerField(blank=True, null=True)),
                ('send_time', models.CharField(blank=True, max_length=255, null=True)),
                ('send_type', models.IntegerField(blank=True, null=True)),
                ('store_id', models.IntegerField(blank=True, null=True)),
                ('take_time', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.BigIntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MallProduct')),
            ],
            options={
                'db_table': 'mall_product_order',
            },
        ),
        migrations.AddField(
            model_name='mallproduct',
            name='product_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MallProductCategory'),
        ),
    ]
