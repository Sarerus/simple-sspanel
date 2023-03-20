# simple-sspanel 简单sspanel

互联网在当今世界的许多地区仍然受到严格控制。 为了抵制非法封锁和监控，世界上爱好和平的人们应该行动起来，保护我们的通信自由。

## 为什么选择我们？

流行的抵制网络审查的方法是[v2ray](https://github.com/v2fly/v2ray-core)，但是使用它需要一些专业的计算机知识。 还有一些基于[v2ray](https://github.com/v2fly/v2ray-core)开发的系统，如：[SSPanel-Uim](https://github.com/Anankke/SSPanel-Uim) , [django-sspanel](https://github.com/Ehco1996/django-sspanel)等，界面美观易用，但是部署这个服务还是需要很繁琐的步骤，这个的出现 项目是让普通人轻松部署[v2ray](https://github.com/v2fly/v2ray-core)服务器

## 如何使用？

要求: docker, 一个域名

1. `git clone https://github.com/Sarerus/simple-sspanel`
1. `cd simple-sspanel`
1. `cp .env.sample .env` 编辑 .env 将“DOMAIN”更改为您的域名
1. `docker compose up -d`
1. `docker compose exec web python manage.py createsuperuser` 创建超级管理员
1. 使用管理员登录 https://{您的域名}/admin 到帐户创建一个帐户，将 clash 复制到您的客户端

## 项目计划

- ✅ 多订阅支持
- ❌ 多用户支持
- ❌ 多节点自动主从架构
- ❌ 集成 [soft-ui-dashboard-django](https://github.com/creativetimofficial/soft-ui-dashboard-django) 管理后台

---

如果你也对本项目感兴趣，欢迎评论或贡献代码
