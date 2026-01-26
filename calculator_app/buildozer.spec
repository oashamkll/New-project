[app]

# Application identifier
package.name = calculator
package.domain = org.example

# Application name
title = Calculator
package.name = calculator

# Version
version = 0.1

# Source files/dirs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Requirements
requirements = python3,kivy==2.1.0

# Permissions
android.permissions = INTERNET

# Services
services = 

# Build settings
android.add_compile_options = 
android.add_gradle_repositories = 
android.gradle_dependencies = 
android.setup_py_requirements = 

# Icons and splash
icon.filename = %(source.dir)s/assets/icon.png
splash.filename = %(source.dir)s/assets/splash.png

# Presplash and orientation
presplash.color = #FFFFFF
orientation = portrait

# Log level
log_level = 2

# Buildozer settings
[buildozer]

# Log level (0 = verbose, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical)
log_level = 2

# Directory to store build artifacts
bin_dir = bin

# Directory to store temporary build files
build_dir = build

[app]

# Application name (human readable)
title = Calculator App

# Package name (unique across the system)
package.name = calc

# Package domain (com.example for example)
package.domain = com.yourdomain

# Version of the application
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# The file to execute
source.file = main.py

# List of source code excludes
source.exclude_patterns = .git,*.pyc,*.pyo,__pycache__,build,dist,*buildozer*

# List of Java or Kotlin classes to add to the application
java.src.files = 

# Extra Java jars to add to the application
javac.libs.dir = 

# Extra jar files to add to the application
android.add_jars = 

# Extra aar files to add to the application
android.add_aars = 

# Assets to add (formatted as [(<src>, <dst>), ...])
android.add_assets = 

# Custom activity (e.g. KivyActivity) to use
android.activity_class_name = org.kivy.android.PythonActivity

# Custom service class (e.g. MyService) to use
android.service_class_name = org.kivy.android.PythonService

# Custom application class (e.g. MyApplication) to use
android.application_class_name = org.kivy.android.PythonApplication

# Custom manifest template (new style only)
android.billing_pub_key = 

# Whether to accept SDK licenses
android.accept_sdk_license = True