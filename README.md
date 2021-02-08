# project1
iframeで埋め込まれる対象のdjangoアプリ

起動方法(オレオレ証明書をもちいたTLS通信のためfoobar.crtを信頼するルート証明書として要インストール)

python manage.py runsslserver 0.0.0.0:8001 --certificate foobar.crt --key foobar.key

URL: https://shusaku.ishikawa:8001


# project2

iframeでproject1を読み込むためのdjangoアプリ


起動方法

python manage.py runsslserver --certificate ../project1/foobar2.crt --key ../project1/foobar2.key

URL: https://shusaku.ishikawa2:8000

#その他環境構築

hosts に
127.0.0.1 shusaku.ishikawa
127.0.0.1 shusaku.ishikawa2
を追加してドメインアクセスできるようにする



