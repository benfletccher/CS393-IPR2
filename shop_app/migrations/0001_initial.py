# Generated by Django 5.1.2 on 2024-11-17 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('adminid', models.IntegerField(db_column='adminId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'administrator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('cadetid', models.IntegerField(db_column='cadetId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=2, null=True)),
                ('gradyear', models.TextField(blank=True, db_column='gradYear', null=True)),
                ('roomnumber', models.IntegerField(blank=True, db_column='roomNumber', null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('venmo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cadet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listingid', models.IntegerField(db_column='listingId', primary_key=True, serialize=False)),
                ('listingname', models.CharField(db_column='listingName', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('listingdate', models.DateField(blank=True, db_column='listingDate', null=True)),
                ('listingimage', models.CharField(blank=True, db_column='listingImage', max_length=255, null=True)),
            ],
            options={
                'db_table': 'listing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('noteid', models.IntegerField(db_column='noteId', primary_key=True, serialize=False)),
                ('notetext', models.TextField(blank=True, db_column='noteText', null=True)),
            ],
            options={
                'db_table': 'note',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(db_column='productId', primary_key=True, serialize=False)),
                ('prodname', models.CharField(blank=True, db_column='prodName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transactiontable',
            fields=[
                ('transactionid', models.IntegerField(db_column='transactionId', primary_key=True, serialize=False)),
                ('dateofsale', models.DateField(db_column='dateOfSale')),
                ('finalprice', models.DecimalField(db_column='finalPrice', decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'transactiontable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cadet', models.OneToOneField(db_column='cadet', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop_app.cadet')),
                ('shoppingpreference', models.CharField(blank=True, db_column='shoppingPreference', max_length=255, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('cadet', models.OneToOneField(db_column='cadet', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop_app.cadet')),
                ('dodid', models.IntegerField(blank=True, db_column='DODId', null=True)),
            ],
            options={
                'db_table': 'vendor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listingdeletebyadmin',
            fields=[
                ('listingid', models.OneToOneField(db_column='listingId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop_app.listing')),
                ('datedeleted', models.DateField(blank=True, db_column='dateDeleted', null=True)),
            ],
            options={
                'db_table': 'listingdeletebyadmin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productinlisting',
            fields=[
                ('productid', models.OneToOneField(db_column='productId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop_app.product')),
            ],
            options={
                'db_table': 'productinlisting',
                'managed': False,
            },
        ),
    ]
