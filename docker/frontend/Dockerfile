# syntax=docker/dockerfile:1

FROM node:22-alpine AS builder

WORKDIR /app

# Copy package.json and package-lock.json to leverage Docker layer caching
COPY frontend/package*.json ./

# Install dependencies cleanly
RUN npm ci

# Copy the rest of the frontend application code, including the .env file
# (Note: Ensure your .dockerignore excludes frontend/node_modules and frontend/dist)
COPY frontend/ .

# Build the Vite application (outputs to /app/dist)
RUN npm run build


# --- Production Nginx Stage ---
FROM nginx:alpine

# Copy the built assets from the builder stage to Nginx's serving directory
COPY --from=builder \
    /app/dist \
    /usr/share/nginx/html

EXPOSE 80

CMD [
    "nginx",
    "-g",
    "daemon off;"
]