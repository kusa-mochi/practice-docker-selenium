# practice-docker-selenium

## how to run E2E test sample

```bash
cd .test-tools
docker compose up
```

Then do the following:

1. access to localhost:5900 using VNC client. (ex. Remmina, RealVNC)
1. attach shell to the selenium-hub container.
1. run the following command.

```bash
cd /app
python sample-test.py
```

## references

- [docker-selenium/GitHub](https://github.com/SeleniumHQ/docker-selenium#debugging)
- [noVNC/GitHub](https://github.com/novnc/noVNC)
- [ecomottblog.com 様](https://www.ecomottblog.com/?p=8038)
- [素人がデータサイエンスを始める 様](https://datascience-beginer.com/docker_selenium/)
