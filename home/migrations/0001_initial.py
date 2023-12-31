# Generated by Django 3.2.9 on 2023-07-23 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.BooleanField(default=False)),
                ('raw_material', models.BooleanField(default=False)),
                ('product_cost', models.IntegerField(default=0)),
                ('raw_material_cost', models.IntegerField(default=0)),
                ('category_1', models.BooleanField(default=False)),
                ('category_2', models.BooleanField(default=False)),
                ('category_3', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_1', models.BooleanField(default=False)),
                ('season_2', models.BooleanField(default=False)),
                ('season_3', models.BooleanField(default=False)),
                ('season_4', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tax', models.IntegerField(default=0)),
                ('lat', models.CharField(default='0', max_length=50)),
                ('lng', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SpotRawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('raw_material', models.ForeignKey(blank=True, limit_choices_to={'raw_material': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.item')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.spot')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distace', models.IntegerField()),
                ('from_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to='home.spot')),
                ('to_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To', to='home.spot')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(blank=True, limit_choices_to={'product': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product', to='home.item')),
                ('raw_material', models.ForeignKey(blank=True, limit_choices_to={'raw_material': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RawMaterial', to='home.item')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=0)),
                ('spot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.spot')),
            ],
        ),
    ]
