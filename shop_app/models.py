# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Administrator(models.Model):
    adminid = models.IntegerField(db_column='adminId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrator'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cadet(models.Model):
    cadetid = models.IntegerField(db_column='cadetId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(max_length=2, blank=True, null=True)
    gradyear = models.TextField(db_column='gradYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    roomnumber = models.IntegerField(db_column='roomNumber', blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(max_length=200, blank=True, null=True)
    venmo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.firstname

    class Meta:
        managed = False
        db_table = 'cadet'


class Customer(models.Model):
    cadet = models.OneToOneField(Cadet, models.DO_NOTHING, db_column='cadet', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model
    shoppingpreference = models.CharField(db_column='shoppingPreference', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Listing(models.Model):
    listingid = models.AutoField(db_column='listingId', primary_key=True)  # Field name made lowercase.
    vendorid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='vendorId')  # Field name made lowercase.
    listingname = models.CharField(db_column='listingName', max_length=255)  # Field name made lowercase.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    listingdate = models.DateField(db_column='listingDate', blank=True, null=True)  # Field name made lowercase.
    listingimage = models.CharField(db_column='listingImage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'listing'


class Listingdeletebyadmin(models.Model):
    listingid = models.OneToOneField(Listing, models.DO_NOTHING, db_column='listingId', primary_key=True)  # Field name made lowercase. The composite primary key (listingId, adminId) found, that is not supported. The first column is selected.
    adminid = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='adminId')  # Field name made lowercase.
    datedeleted = models.DateField(db_column='dateDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listingdeletebyadmin'
        unique_together = (('listingid', 'adminid'),)


class Note(models.Model):
    noteid = models.IntegerField(db_column='noteId', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productId')  # Field name made lowercase.
    notetext = models.TextField(db_column='noteText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'note'


class Product(models.Model):
    productid = models.IntegerField(db_column='productId', primary_key=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='prodName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.prodname

    class Meta:
        managed = False
        db_table = 'product'


class Productinlisting(models.Model):
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productId', primary_key=True)  # Field name made lowercase. The composite primary key (productId, listingId) found, that is not supported. The first column is selected.
    listingid = models.ForeignKey(Listing, models.DO_NOTHING, db_column='listingId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productinlisting'
        unique_together = (('productid', 'listingid'),)


class Transactiontable(models.Model):
    transactionid = models.IntegerField(db_column='transactionId', primary_key=True)  # Field name made lowercase.
    dateofsale = models.DateField(db_column='dateOfSale')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerId')  # Field name made lowercase.
    finalprice = models.DecimalField(db_column='finalPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    listing = models.ForeignKey(Listing, models.DO_NOTHING, db_column='listing')

    class Meta:
        managed = False
        db_table = 'transactiontable'


class Vendor(models.Model):
    cadet = models.OneToOneField(Cadet, models.DO_NOTHING, db_column='cadet', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model
    dodid = models.IntegerField(db_column='DODId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vendor'
