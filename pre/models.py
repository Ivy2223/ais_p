# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models


class RoutePartial(models.Model):
    routeid = models.AutoField(db_column='RouteId', primary_key=True)  # Field name made lowercase.
    outsetcode = models.CharField(db_column='OutsetCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationcode = models.CharField(db_column='DestinationCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    route = models.TextField(db_column='Route', blank=True, null=True)  # Field name made lowercase.
    outsetname = models.CharField(db_column='OutsetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationname = models.CharField(db_column='DestinationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outsetlon = models.CharField(db_column='OutsetLon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outsetlat = models.CharField(db_column='OutsetLat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationlon = models.CharField(db_column='DestinationLon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationlat = models.CharField(db_column='DestinationLat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipimo = models.CharField(db_column='ShipImo', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'route_partial'

    def __str__(self):
        return self.route


class SailPartial(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    imo = models.CharField(db_column='Imo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=128, blank=True, null=True)  # Field name made lowercase.
    routeid = models.IntegerField(db_column='RouteId', blank=True, null=True)  # Field name made lowercase.
    departuretime = models.DateTimeField(db_column='DepartureTime', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=128, blank=True, null=True)  # Field name made lowercase.
    arrivetime = models.DateTimeField(db_column='ArriveTime', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'sail_partial'


class Port(models.Model):
    port_id = models.AutoField(db_column='PORT_ID', primary_key=True)  # Field name made lowercase.
    port_name = models.CharField(db_column='PORT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    un_locode = models.CharField(db_column='UN_LOCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'port_version_1'


class ShipAisInfo(models.Model):
    imo = models.CharField(db_column='Imo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mmsi = models.CharField(db_column='Mmsi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    call_sign = models.CharField(db_column='Call_Sign', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=255, blank=True, null=True)  # Field name made lowercase.
    draught = models.CharField(db_column='Draught', max_length=255, blank=True, null=True)  # Field name made lowercase.
    breadth = models.CharField(db_column='Breadth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gross_tonnage = models.CharField(db_column='Gross_Tonnage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadweight = models.CharField(db_column='Deadweight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year_built = models.CharField(db_column='Year_Built', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    leave_port = models.CharField(db_column='Leave_Port', max_length=255, blank=True, null=True)  # Field name made lowercase.
    atd = models.CharField(db_column='ATD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arrive_port = models.CharField(db_column='Arrive_Port', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eta = models.CharField(db_column='ETA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_report_time = models.CharField(db_column='Last_Report_Time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ship_ais_info'


class ShipAisInfoStatic(models.Model):
    imo = models.CharField(db_column='Imo', primary_key=True, max_length=255)  # Field name made lowercase.
    mmsi = models.CharField(db_column='Mmsi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    call_sign = models.CharField(db_column='Call_Sign', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=255, blank=True, null=True)  # Field name made lowercase.
    breadth = models.CharField(db_column='Breadth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gross_tonnage = models.CharField(db_column='Gross_Tonnage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadweight = models.CharField(db_column='Deadweight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year_built = models.CharField(db_column='Year_Built', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ship_ais_info_static'


class MainRouteV1(models.Model):
    routeid = models.IntegerField(db_column='RouteId', primary_key=True)  # Field name made lowercase.
    shipcount = models.IntegerField(db_column='ShipCount', blank=True, null=True)  # Field name made lowercase.
    outset = models.CharField(db_column='Outset', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'main_route_v1'
