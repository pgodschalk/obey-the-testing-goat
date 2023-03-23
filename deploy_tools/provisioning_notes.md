# Provisoning notes

## Required packages

- httpd
- certbot
- a Compose specification compatible container runtime

eg, on RHEL 9:

```sh
sudo dnf install certbot httpd podman podman-compose
```

## Certbot provisoning

```sh
sudo certbot certonly -d superlists-staging.example.org
```

## HTTPD Virtual Host config

- see apache2.template.conf
- replace `DOMAIN` with, e.g., `staging.example.org`
- replace `PORT` with, e.g., `8001`

## Compose config

- see compose.template.yaml
- replace `IMAGE` with, e.g., `acmeinc`
- replace `REPOSITORY` with, e.g, `obey-the-testing-goat`
- replace `CONTAINER_NAME` with, e.g., `obey-the-testing-goat`

## Folder structure

Assume we have a user account at /home/username

```text
/home/username
└── DOMAIN
     ├── .env
     ├── compose.yaml
```
