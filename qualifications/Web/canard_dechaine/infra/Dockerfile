FROM busybox:1.35

# Create a non-root user to own the files and run our server
RUN adduser -D challenge
USER challenge
WORKDIR /home/challenge

# Copy the static website
# Use the .dockerignore file to control what ends up inside the image!
COPY ./infra/site .

# Run BusyBox httpd
CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]

