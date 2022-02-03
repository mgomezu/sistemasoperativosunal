FROM node:16.13.1-alpine as buildstep
WORKDIR  /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build 

FROM nginx:1.17.1-alpine
COPY --from=buildstep /app/dist/juego-de-la-vida /usr/share/nginx/html