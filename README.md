# simple-sspanel  |  [中文](https://github.com/Sarerus/simple-sspanel/blob/main/docs/README_CN.md)

The Internet is still strictly controlled in many areas of the world today. In order to resist illegal blocking and monitoring, peace-loving people in the world should act to protect our freedom of communication.

## Why choose us？

The popular way to resist network censorship is [v2ray](https://github.com/v2fly/v2ray-core), but using it requires some professional computer knowledge. There are also some systems developed based on [v2ray](https://github.com/v2fly/v2ray-core), such as: [SSPanel-Uim](https://github.com/Anankke/SSPanel-Uim), [django-sspanel](https://github.com/Ehco1996/django-sspanel), etc., which have beautiful and easy-to-use interfaces, but deploying this service still requires Very cumbersome steps, the emergence of this project is to allow ordinary people to easily deploy [v2ray](https://github.com/v2fly/v2ray-core) server

## How to use?

requirements: docker, a domain name

1. `git clone https://github.com/Sarerus/simple-sspanel`
1. `cd simple-sspanel`
1. `cp .env.sample .env` edit .env change "DOMAIN" to your domain name
1. `docker compose up -d`
1. `docker compose exec web python manage.py createsuperuser` create a super administrator
1. use administrator login https://{yourdomain}/admin to accounts create a account, copy clash to your client

## project planning

- ✅ Multi-subscription support
- ❌ Multi-user support
- ❌ Multi-node automatic main-worker architecture
- ❌ Integrated [soft-ui-dashboard-django](https://github.com/creativetimofficial/soft-ui-dashboard-django) admin ui

---

If you are also interested in this project, welcome to comment or contribute code
