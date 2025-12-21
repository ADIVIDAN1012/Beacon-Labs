#!/bin/bash
set -e

echo "Updating system..."
sudo apt-get update

echo "Installing system dependencies for Buildozer and Kivy..."
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    build-essential

echo "Instaling Buildozer..."
pip3 install --user --upgrade buildozer cython

# Add user bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "Adding ~/.local/bin to PATH..."
    echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
    export PATH=$HOME/.local/bin:$PATH
fi

echo "--------------------------------------------------------"
echo "Setup complete!"
echo "To build the APK, run the following command in this directory:"
echo "buildozer android debug"
echo "--------------------------------------------------------"
