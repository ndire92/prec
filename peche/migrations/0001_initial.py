# Generated by Django 4.1.6 on 2023-02-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimPecheArtisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActPech_Artisan', models.CharField(max_length=250)),
                ('GroupPecheur', models.CharField(max_length=250)),
                ('GroupMareyeur', models.CharField(max_length=250)),
                ('TypePirogu', models.CharField(max_length=250)),
                ('TypProdPechPirogBois', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheAssure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeAssurancPech', models.CharField(max_length=25)),
                ('BesoinFormatPech', models.CharField(max_length=250)),
                ('ActeurSensibilisePech', models.CharField(max_length=250)),
                ('ActeurFormatPech', models.CharField(max_length=250)),
                ('BesoinSensibilisePech', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheCommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdVendType', models.IntegerField()),
                ('ProdVendCampgnInterSais', models.IntegerField()),
                ('ProdVendCampSaisFroid', models.IntegerField()),
                ('ProdVendCampPrintem', models.IntegerField()),
                ('Type_VentPech', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OffrServicFinancPech', models.CharField(max_length=25)),
                ('DemandApportPech', models.IntegerField()),
                ('TypGaranExige', models.CharField(max_length=250)),
                ('ActeurFormatPech', models.CharField(max_length=250)),
            ],
        ),
    ]
