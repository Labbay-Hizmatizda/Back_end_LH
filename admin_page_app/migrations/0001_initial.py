# Generated by Django 5.0.2 on 2024-03-23 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cv_images/')),
                ('bio', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='passport_images/')),
                ('personal_number', models.CharField(max_length=14)),
                ('card_number', models.CharField(max_length=9)),
                ('is_approved', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('message', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobAppeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('media', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('location_link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='admin_page_app.employer')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='admin_page_app.order'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_approve', models.BooleanField(default=False)),
                ('employer_approve', models.BooleanField(default=False)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAppeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_appeals', to='admin_page_app.employer')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.order')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='admin_page_app.employee')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='proposal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.proposal'),
        ),
    ]
