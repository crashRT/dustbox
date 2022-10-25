# dustbox

悪いことなどをこっそりつぶやくためのwebアプリ

内容をUTF8でエンコードされた16進数に変換して投稿することができるSNS的な何か．
16進数の変換は [utf8-encode-decode](https://github.com/crashRT/utf8-encode-decode/tree/c75a572ca769e83046f7a6b97418a931a55c6527) を使っている．

## 使い方

docker engine, docker-compose-plugin が必要．

https://docs.docker.com/engine/install/ubuntu/ などを参考に．

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
python3.10, django 4.1 を使っている．

### 開発用サーバー起動
```
python manage.py runserver --settings dustbox.local_settings
```
