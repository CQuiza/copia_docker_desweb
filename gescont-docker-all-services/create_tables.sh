#/bin/bash
docker exec gescont-docker-all-services-djdesweb-1 sh -c "python manage.py shell < createTables.py"


