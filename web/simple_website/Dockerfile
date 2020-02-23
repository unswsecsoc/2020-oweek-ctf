FROM node:13-alpine3.10

WORKDIR /app

COPY . /app

RUN npm install
EXPOSE 8000/tcp

CMD ["node", "app.js"]
