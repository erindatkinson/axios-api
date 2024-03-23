FROM node:alpine as build
RUN apk add nginx

RUN mkdir /opt/app
WORKDIR /opt/app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
COPY --from=build /opt/app/dist /usr/share/nginx/html





