FROM node:20-alpine

WORKDIR /app/apps/web-dashboard
COPY apps/web-dashboard/package.json apps/web-dashboard/package-lock.json* ./
RUN npm install
COPY apps/web-dashboard ./
