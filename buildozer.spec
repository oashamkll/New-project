[app]
title = Pong
package.name = pong
package.domain = org.pacehoz

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf,wav,mp3,json

version = 1.0.0

# Если добавишь иконку — раскомментируй и положи файл рядом, например assets/icon.png
# icon.filename = %(source.dir)s/assets/icon.png

orientation = landscape
fullscreen = 1

# Kivy + stdlib. (random/vector/clock/etc входят в stdlib/Kivy)
requirements = python3,kivy

# Если вдруг добавишь звуки/картинки/шрифты — можно собрать их в папку assets и оставить include_exts.

# Android настройки
android.minapi = 21
android.api = 33
android.ndk_api = 21

# Собираем самые популярные ABI
android.archs = arm64-v8a,armeabi-v7a

# Ускорение сборки
p4a.branch = master
p4a.use_prebuilt_dist = 0

# Разрешения (твоей игре обычно не нужны)
android.permissions =

# Логи/оптимизации
log_level = 2

[buildozer]
warn_on_root = 1
