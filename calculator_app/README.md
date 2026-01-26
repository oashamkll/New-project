# Calculator App

A beautiful calculator application built with Kivy for cross-platform deployment.

## Features

- Basic arithmetic operations (+, -, *, /)
- Percentage calculations
- Clear (C) and Clear Entry (CE) functions
- Responsive design suitable for both mobile and desktop
- Color-coded buttons for better UX

## Installation

To run this application locally:

```bash
pip install -r requirements.txt
python main.py
```

## Building for Android

This project includes support for building an Android APK using Buildozer:

```bash
# Install buildozer
pip install buildozer

# Initialize buildozer (creates buildozer.spec if needed)
cd calculator_app
buildozer init

# Build the APK
buildozer android debug
```

## Project Structure

```
calculator_app/
├── main.py          # Main application entry point
├── requirements.txt # Python dependencies
├── buildozer.spec   # Buildozer configuration
├── ui/              # UI components (if needed)
├── utils/           # Utility functions (if needed)
├── assets/          # Images and other assets (if needed)
└── README.md        # This file
```

## GitHub Actions

The project includes a GitHub Actions workflow in `.github/workflows/build.yml` that automatically builds the Android APK when changes are pushed to the repository.