#Source: https://stackoverflow.com/questions/50411547/peewee-attributeerror-when-select-with-more-than-one-join
import peewee as pw


# Conection to mydbname database
dbn = 'mydbname'
user = 'myusername'
pwd = '******'
host = 'localhost'
prt = 3306

db = pw.MySQLDatabase(dbn, user=user,
                  password=pwd,  host=host, port=prt)


class MySqlDbModel(pw.Model):
    class Meta:
        database = db


class AgeCitas(MySqlDbModel):
    CIT_ID = pw.BigIntegerField()
    AGE_ID = pw.BigIntegerField()
    FECHAHORA = pw.DateTimeField()
    ACT_ID = pw.BigIntegerField()
    PAC_ID = pw.BigIntegerField()
    ASIGNADA = pw.CharField()
    IND_ID = pw.BigIntegerField()
    ACUDIO = pw.DoubleField()
    ORDEN = pw.DoubleField()

class Meta:
    table_name = 'AGE_CITAS'


class AgeAgendas(MySqlDbModel):
    AGE_ID = pw.DecimalField()
    CODIGO = pw.CharField()
    CEN_ID = pw.DecimalField()
    PER_ID = pw.DecimalField()
    NPR_ID = pw.DecimalField()
    DESCRIPCION = pw.CharField()
    COLOR = pw.CharField()

class Meta:
    table_name = 'AGE_AGENDAS'


class StkPersonas(MySqlDbModel):
    PER_ID = pw.BigIntegerField()
    DOCUMENTO = pw.CharField()
    NOMBRE = pw.CharField()
    APELLIDO1 = pw.CharField()
    APELLIDO2 = pw.CharField()
    FECHA_ALTA = pw.DateTimeField()
    FECHA_BAJA = pw.DateTimeField()
    EMAIL = pw.CharField()
    TELEFONO1 = pw.CharField()
    TELEFONO2 = pw.CharField()
    TELEFONO3 = pw.CharField()
    TELEFONO4 = pw.CharField()
    SEXO = pw.CharField()
    NACIMIENTO = pw.DateTimeField()
    ES_PACIENTE = pw.CharField()
    ES_PROFESIONAL = pw.CharField()

class Meta:
    table_name = 'STK_PERSONAS'