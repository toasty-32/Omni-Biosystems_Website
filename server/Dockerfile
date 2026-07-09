FROM node:20-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY package*.json ./
RUN npm install --omit=dev

# App source
COPY . .

ENV NODE_ENV=production
# Cloud Run provides PORT (defaults to 8080)
EXPOSE 8080

CMD ["node", "index.js"]
