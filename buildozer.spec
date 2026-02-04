[app]

title = Pong Game
package.name = ponggame
package.domain = ru.pacehoz

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3,ogg

version = 1.0.0

requirements = python3,kivy==2.3.0,pillow

orientation = landscape
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET, VIBRATE
android.accept_sdk_license = True
android.enable_androidx = True

log_level = 2
warn_on_root = 1

[buildozer]

build_dir = ./.buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 1
