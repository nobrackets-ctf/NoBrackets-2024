FROM node:18

WORKDIR /app

# Copy web app to container
COPY src ./

# Create directory
RUN mkdir -p public/css/

# Download bulma.css
RUN wget https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css -O public/css/bulma.min.css

# Install app dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["node", "app.js"]

