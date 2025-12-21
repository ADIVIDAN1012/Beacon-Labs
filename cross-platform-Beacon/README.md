# Beacon Programming Language (Cross-Platform)

Implementation of the Beacon Programming Language designed for cross-platform deployment, specifically Android.

## Quick Start (Interpreter)

You can run Beacon code directly using the Python interpreter:

```bash
# General usage
python main.py run <your_file.bpl>

# Example
python main.py run test.bpl
```

## Android Build (APK)

This project is configured for [Buildozer](https://github.com/kivy/buildozer). To generate an APK:

1.  **Install Buildozer**:
    ```bash
    pip install buildozer
    ```
    *Note: Buildozer requires a Linux environment (or WSL on Windows).*

2.  **Build the APK**:
    Run the following command in the project root:
    ```bash
    buildozer android debug
    ```

3.  **Deploy**:
    Once built, you can deploy to a connected Android device:
    ```bash
    buildozer android deploy run
    ```
