# dustbox

悪いことなどをこっそりつぶやくためのwebアプリ

内容をUTF8でエンコードされた16進数に変換して投稿することができるSNS的な何か．
16進数の変換は [utf8-encode-decode](https://github.com/crashRT/utf8-encode-decode/tree/c75a572ca769e83046f7a6b97418a931a55c6527) を使っている．

## 使い方

`docker engine`, `docker-compose-plugin` が必要．

https://docs.docker.com/engine/install/ubuntu/ などを参考に．

### .env などの準備
- `.env.example` を複製して名前を `.env` にする．
- `SECRET_KEY`には仮の値が入っている．そのままでも動くが，セキュリティ的によくないので変更する．
  - django, python3 を導入済みであれば`python3 get_secret_key.py`
  - そうでなければ，[Django 秘密鍵ジェネレーター](https://miniwebtool.com/ja/django-secret-key-generator/)などを用いて生成し，置き換える．


- Docker の設定がまだちゃんとできていないので，django を入れて `python manage.py migrate` `python manage.py collectstatic` を事前に実行しないといけない状態になっている．

### イメージのビルド

```
sudo docker compose build
```

### コンテナの起動
```
sudo docker compose up -d
```

### コンテナの停止
```
sudo docker compose down
```

## 開発について
`python3.10` を使っている．

### pull submodule (初回のみ)
```
git submodule update --init --recursive
```

### 開発用サーバー起動
```
sh local_start.sh
```
