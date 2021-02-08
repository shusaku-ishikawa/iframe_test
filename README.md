# project1
iframeで埋め込まれる対象のdjangoアプリ

起動方法(オレオレ証明書をもちいたTLS通信のためfoobar.crtを信頼するルート証明書として要インストール)
python manage.py runsslserver 0.0.0.0:8001 --certificate foobar.crt --key foobar.key

# project2
iframeでproject1を読み込むためのdjangoアプリ

起動方法
python manage.py runsslserver --certificate ../project1/foobar2.crt --key ../project1/foobar2.key




