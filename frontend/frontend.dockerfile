# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:10-alpine as build

WORKDIR /app

RUN npm install -g http-server
COPY ./package*.json ./package-lock.json /app
RUN npm install
COPY ./ /app