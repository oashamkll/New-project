[app]

title = Pong Game
package.name = ponggame
package.domain = ru.pacehoz

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = VIBRATE
android.accept_sdk_license = True
android.skip_update = False

log_level = 2
warn_on_root = 1

[buildozer]

build_dir = ./.buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 1
