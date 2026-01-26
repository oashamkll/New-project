# Calculator App

A beautiful and functional calculator application for Android built with Kotlin.

## Features

- Clean and intuitive user interface
- Basic arithmetic operations (+, -, *, /)
- Decimal point support
- Clear (C) and backspace (⌫) functions
- Error handling for invalid operations
- Responsive design

## Technology Stack

- **Language**: Kotlin
- **UI Framework**: Android XML layouts
- **Build System**: Gradle
- **Testing**: JUnit for unit tests

## GitHub Actions CI/CD

This project includes a GitHub Actions workflow that:
- Builds the Android application
- Runs unit tests
- Generates a debug APK
- Uploads the APK as an artifact

The workflow configuration is located in `.github/workflows/android.yml`.

## Getting Started

To build the project locally:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd calculator-app

# Build the project
./gradlew build

# Generate APK
./gradlew assembleDebug
```

## Project Structure

```
app/
├── src/main/
│   ├── java/com/example/calculator/     # Kotlin source files
│   │   └── MainActivity.kt              # Main application logic
│   ├── res/                             # Resources (layouts, values, drawables)
│   │   ├── layout/
│   │   │   └── activity_main.xml        # Main UI layout
│   │   ├── values/
│   │   │   ├── strings.xml              # String resources
│   │   │   ├── colors.xml               # Color definitions
│   │   │   └── themes.xml               # Theme configurations
│   │   └── drawable/                    # Drawable resources
│   └── AndroidManifest.xml              # Application manifest
```

## License

This project is open source and available under the MIT License.