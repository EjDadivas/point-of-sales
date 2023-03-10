# Generated by Django 4.1.7 on 2023-03-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment_tyoe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='item_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.order')),
            ],
        ),
    ]
