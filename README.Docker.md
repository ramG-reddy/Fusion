# Docker Setup for Fusion

### Requirements
- Docker cli and Docker compose on the system
- A "../DB_files/db-dump.sql" (Relative path to the repo directory) file to restore DB in the container

### Commands

To Build
```bash
docker compose -p fusion up --build -d
```

To Start
```bash
docker compose -p fusion start
```

To Stop
```bash
docker compose -p fusion stop
```

To Trash the containers
```bash
docker compose -p fusion down
```
