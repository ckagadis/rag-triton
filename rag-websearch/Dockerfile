FROM searxng/searxng:latest

COPY settings.yml /etc/searxng/settings.yml

EXPOSE 8080
CMD ["uwsgi", "--ini", "/etc/searxng/uwsgi.ini"]
