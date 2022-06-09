# Generated by Django 4.0.3 on 2022-05-30 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantFeedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('star_rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=100)),
                ('description', models.TextField()),
                ('realtor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realtor_ids', to=settings.AUTH_USER_MODEL)),
                ('tenant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
