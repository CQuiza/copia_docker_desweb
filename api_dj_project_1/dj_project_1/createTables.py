''' 
> este se usa para cuando no haya creado las tablas directamente desde pg admin
> este ejercicio el 27 de junio no maneja aun tablas de geometrìas
'''


from app_cq.pycode.connPOO import Conn

conn = Conn()
conn.cursor.execute('create extension postgis')
conn.cursor.execute('create schema c')
conn.cursor.execute('create table c.constructions (gid serial primary key, city varchar, days_limit integer, area double precision, org_responsible varchar, geom geometry("polygon",25830))')
conn.cursor.execute('create table c.pipes (gid serial primary key, descripcion varchar, length double precision, geom geometry (LineString,25830), material varchar, use varchar)')
conn.cursor.execute('create table c.wells (gid serial primary key, descripcion varchar, depth double precision, geom geometry (Point,25830), radius double precision, type varchar)')
print('tablas creadas')