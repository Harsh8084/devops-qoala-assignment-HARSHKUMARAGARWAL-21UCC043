# Corrected Dockerfile
FROM nginx:latest
RUN apt-get update && apt-get install -y iputils-ping 
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
