FROM mongo:6

# Copy initialization scripts to the Docker container
COPY init-db.js /docker-entrypoint-initdb.d/

# Expose MongoDB port
EXPOSE 27017

