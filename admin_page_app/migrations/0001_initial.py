# Generated by Django 5.0.3 on 2024-04-03 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
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
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(upload_to='cv_images/')),
                ('bio', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('owner_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=100)),
                ('card_number', models.IntegerField(default=0)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_dir', models.ImageField(upload_to='passport_images/')),
                ('is_approved', models.BooleanField(default=False)),
                ('owner_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('message', models.TextField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employer')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('message', models.TextField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employer')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobAppeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.job')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employer',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_page_app.languages'),
        ),
        migrations.AddField(
            model_name='employee',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_page_app.languages'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('media', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('location_link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='admin_page_app.category')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='admin_page_app.employer')),
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
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_appeals', to='admin_page_app.employer')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.order')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='admin_page_app.employee')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='proposal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page_app.proposals'),
        ),
    ]
