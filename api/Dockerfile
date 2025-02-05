FROM node:20-slim

WORKDIR /usr/src/app

# Install dependencies first (better caching)
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Copy .env.example to .env if .env doesn't exist
RUN cp -n .env.example .env 2>/dev/null || true

# Build the application
RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start:prod"]
