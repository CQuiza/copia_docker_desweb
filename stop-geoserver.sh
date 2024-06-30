#!/bin/sh
echo "### Stopping PostGIS"
docker-compose -f postgis/docker-compose.yml stop
echo
echo "### Stopping GeoServer"
docker-compose -f geoserver/docker-compose.yml stop
echo
echo "### Stopping PgAdmin4"
docker-compose -f pgadmin4/docker-compose.yml stop
echo Hecho