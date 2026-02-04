[app]
title = Pong
package.name = pong
package.domain = org.pacehoz

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf,wav,mp3,json

version = 1.0.0

orientation = landscape
fullscreen = 1

requirements = python3,kivy

# Android настройки
android.minapi = 21
android.api = 33
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

# Собираем самые популярные ABI
android.archs = arm64-v8a,armeabi-v7a

# p4a
p4a.branch = master

# Разрешения
android.permissions =

# Логи
log_level = 2

[buildozer]
warn_on_root = 1
