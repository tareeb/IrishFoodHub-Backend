# Generated by Django 4.2.4 on 2023-08-03 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('rec', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.writer'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('delivery', 'Delivery'), ('received', 'Received')], default='pending', max_length=20)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user')),
            ],
        ),
    ]
