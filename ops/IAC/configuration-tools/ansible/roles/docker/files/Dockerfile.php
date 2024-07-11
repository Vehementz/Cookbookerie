# Use the official PHP image with FPM
FROM php:7.4-fpm

# Install any additional extensions you need
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Copy your PHP scripts into the default directory for PHP FPM
COPY src/ /var/www/html/
