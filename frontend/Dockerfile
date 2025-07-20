FROM node:20-alpine AS builder

WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package.json package-lock.json ./
RUN npm install

# Копируем остальной код
COPY . .

# Собираем production-версию приложения
RUN npm run build

# --- STAGE 2: Сервер на базе Nginx ---
FROM nginx:stable-alpine

# Копируем собранные статические файлы из стадии 'builder'
COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем нашу конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Открываем порт 80, который слушает Nginx
EXPOSE 80

# Команда для запуска Nginx
CMD ["nginx", "-g", "daemon off;"]