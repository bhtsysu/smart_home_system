# Generated by Django 5.2.1 on 2025-06-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_smarthomeuser_options_device_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='设备IP地址'),
        ),
        migrations.AddField(
            model_name='device',
            name='port',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='设备端口'),
        ),
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.CharField(default='5cf40dfb-5972-40bb-9b57-21fbe0ce3139', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.CharField(default='45439c39-1816-44c5-90b4-60c396fe9504', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scene',
            name='id',
            field=models.CharField(default='1102f6f7-dd47-4828-a4f7-7a92e76f858a', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scenedeviceconfig',
            name='id',
            field=models.CharField(default='39177a2a-58be-47e0-95ff-42b667e0d0b5', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='smarthomeuser',
            name='id',
            field=models.CharField(default='a6a312a9-82a7-4e25-ab4e-cff3573bb45f', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
