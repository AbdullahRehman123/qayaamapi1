# Generated by Django 4.0.3 on 2022-04-13 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('tenantsFeedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantfeedback',
            name='realtor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realtor_ids', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='tenantfeedback',
            name='tenant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_ids', to='accounts.account'),
        ),
    ]
