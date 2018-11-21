# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models




class MainRouteV1(models.Model):
    routeid = models.IntegerField(db_column='RouteId', primary_key=True)  # Field name made lowercase.
    shipcount = models.IntegerField(db_column='ShipCount', blank=True, null=True)  # Field name made lowercase.
    outset = models.CharField(db_column='Outset', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    route = models.TextField(db_column='Route', blank=True, null=True)  # Field name made lowercase.
    outsetsite = models.CharField(db_column='OutsetSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationsite = models.CharField(db_column='DestinationSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sea_flag = models.IntegerField(db_column='sea_flag',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_route_v1'


class Port(models.Model):
    port_id = models.AutoField(db_column='PORT_ID', primary_key=True)  # Field name made lowercase.
    port_name = models.CharField(db_column='PORT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    un_locode = models.CharField(db_column='UN_LOCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'port'


class PortVersion1(models.Model):
    port_id = models.AutoField(db_column='PORT_ID', primary_key=True)  # Field name made lowercase.
    port_name = models.CharField(db_column='PORT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    un_locode = models.CharField(db_column='UN_LOCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'port_version_1'


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
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'route_partial'


class RouteVersion1(models.Model):
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
    shipimo = models.TextField(db_column='ShipImo', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'route_version_1'


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
        managed = False
        db_table = 'sail_partial'


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
        managed = False
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
        managed = False
        db_table = 'ship_ais_info_static'


class ShipBaseInfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    batch_no = models.CharField(db_column='BATCH_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_name = models.CharField(db_column='SHIP_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ship_code = models.CharField(db_column='SHIP_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stauts = models.CharField(db_column='STAUTS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ship_type_id = models.CharField(db_column='SHIP_TYPE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_type_ids = models.CharField(db_column='SHIP_TYPE_IDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_size = models.DecimalField(db_column='SHIP_SIZE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dwt = models.DecimalField(db_column='DWT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gt = models.DecimalField(db_column='GT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cgt = models.DecimalField(db_column='CGT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ship_flag = models.CharField(db_column='SHIP_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_built = models.CharField(db_column='SHIP_BUILT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ship_owner_id = models.CharField(db_column='SHIP_OWNER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    group_ship_owner_id = models.CharField(db_column='GROUP_SHIP_OWNER_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ship_owner = models.CharField(db_column='SHIP_OWNER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group_ship_owner = models.CharField(db_column='GROUP_SHIP_OWNER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ship_yard_id = models.CharField(db_column='SHIP_YARD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_yard = models.CharField(db_column='SHIP_YARD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oilwear = models.DecimalField(db_column='OILWEAR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    speed = models.DecimalField(db_column='SPEED', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    engine = models.CharField(db_column='ENGINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    call_sign = models.CharField(db_column='CALL_SIGN', max_length=23, blank=True, null=True)  # Field name made lowercase.
    loa = models.DecimalField(db_column='LOA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    breadth = models.DecimalField(db_column='BREADTH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grain = models.DecimalField(db_column='GRAIN', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    draft = models.DecimalField(db_column='DRAFT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    beam = models.DecimalField(db_column='BEAM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    draught = models.DecimalField(db_column='DRAUGHT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ldt = models.DecimalField(db_column='LDT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lbp = models.DecimalField(db_column='LBP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    depth_moulded = models.DecimalField(db_column='DEPTH_MOULDED', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ballast_cap = models.DecimalField(db_column='BALLAST_CAP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_generanted_power_kw = models.DecimalField(db_column='TOTAL_GENERANTED_POWER_KW', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    capactiy = models.DecimalField(db_column='CAPACTIY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ice_notation = models.CharField(db_column='ICE_NOTATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hull_no = models.CharField(db_column='HULL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keel_laid_date = models.CharField(db_column='KEEL_LAID_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    manager_name = models.CharField(db_column='MANAGER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manager_country_id = models.CharField(db_column='MANAGER_COUNTRY_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    manager_country = models.CharField(db_column='MANAGER_COUNTRY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='OPERATOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imo_decimal = models.CharField(db_column='IMO_DECIMAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hull_type = models.CharField(db_column='HULL_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class_soc = models.CharField(db_column='CLASS_SOC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contract_date = models.CharField(db_column='CONTRACT_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    engine_decimal = models.DecimalField(db_column='ENGINE_DECIMAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    auxiliary_decimal = models.DecimalField(db_column='AUXILIARY_DECIMAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    main_power = models.DecimalField(db_column='MAIN_POWER', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    main_power_designer = models.CharField(db_column='MAIN_POWER_DESIGNER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    engine_model = models.CharField(db_column='ENGINE_MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    power_type = models.CharField(db_column='POWER_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ship_type_first_name = models.CharField(db_column='SHIP_TYPE_FIRST_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_type_first_id = models.CharField(db_column='SHIP_TYPE_FIRST_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_type_second_name = models.CharField(db_column='SHIP_TYPE_SECOND_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_type_second_id = models.CharField(db_column='SHIP_TYPE_SECOND_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_type_thrid_name = models.CharField(db_column='SHIP_TYPE_THRID_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_type_thrid_id = models.CharField(db_column='SHIP_TYPE_THRID_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_type_for_name = models.CharField(db_column='SHIP_TYPE_FOR_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_type_for_id = models.CharField(db_column='SHIP_TYPE_FOR_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ship_type_dwt_id = models.CharField(db_column='SHIP_TYPE_DWT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    built_date = models.CharField(db_column='BUILT_DATE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    exname = models.CharField(db_column='EXNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel_type = models.CharField(db_column='FUEL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    products_tankers = models.CharField(db_column='PRODUCTS_TANKERS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chemical_register = models.CharField(db_column='CHEMICAL_REGISTER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imo1 = models.CharField(db_column='IMO1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imo2 = models.CharField(db_column='IMO2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imo3 = models.CharField(db_column='IMO3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    panamax_container = models.CharField(db_column='PANAMAX_CONTAINER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gcargo = models.CharField(db_column='GCARGO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.CharField(db_column='OPERATOR_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operator_date = models.CharField(db_column='OPERATOR_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operator_name = models.CharField(db_column='OPERATOR_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ts = models.CharField(db_column='TS', max_length=23, blank=True, null=True)  # Field name made lowercase.
    ver = models.DecimalField(db_column='VER', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ds = models.CharField(db_column='DS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    free1 = models.CharField(db_column='FREE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    free2 = models.CharField(db_column='FREE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    free3 = models.CharField(db_column='FREE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    free4 = models.CharField(db_column='FREE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    free5 = models.CharField(db_column='FREE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designer = models.CharField(db_column='DESIGNER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    environmental_detail = models.CharField(db_column='ENVIRONMENTAL_DETAIL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    engine_detail = models.CharField(db_column='ENGINE_DETAIL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    auxiliary_detail = models.CharField(db_column='AUXILIARY_DETAIL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ship_design = models.CharField(db_column='SHIP_DESIGN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    propulsor_detail = models.CharField(db_column='PROPULSOR_DETAIL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nt = models.DecimalField(db_column='NT', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    main_engine_series = models.CharField(db_column='MAIN_ENGINE_SERIES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_type_app_id = models.CharField(db_column='SHIP_TYPE_APP_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fp = models.CharField(db_column='FP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tanker_type = models.CharField(db_column='TANKER_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tanker_info = models.CharField(db_column='TANKER_INFO', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_base_info'


