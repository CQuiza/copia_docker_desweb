#/bin/bash
docker exec api_dj_project_1-dj_project_1-1 sh -c "python manage.py shell < createTables.py"


