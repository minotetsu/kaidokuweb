# Flask(python)をdockerで動かす

```sh
# まず適当な場所でこのリポジトリをクローン
git clone git@github.com:minojiro/flask-on-docker.git

# docker立ち上げ
docker-compose up -d

# docker終了
docker-compose stop

# ログを見る（command + c で止まる）
docker-compose logs -f web
```
