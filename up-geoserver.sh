#!/bin/sh
echo "### Starting PostGIS. Port 5440"
docker-compose -f postgis/docker-compose.yml up -d
echo
echo "### Starting GeoServer. Port 8083"
docker-compose -f geoserver/docker-compose.yml up -d
echo
echo "### Starting PgAdmin4. Port 5050"
docker-compose -f pgadmin4/docker-compose.yml up -d
echo Hecho