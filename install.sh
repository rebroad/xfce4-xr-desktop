#!/bin/bash

# Exit on error
set -e

echo "Installing XFCE4 XR Desktop..."

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    echo "Please do not run this script as root"
    exit 1
fi

# Check Python version
python3 --version || {
    echo "Python 3 is required but not installed"
    exit 1
}

# Check for required system packages
echo "Checking for required system packages..."
REQUIRED_PACKAGES="python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-xfce4ui-2"
MISSING_PACKAGES=""

for package in $REQUIRED_PACKAGES; do
    if ! dpkg -l | grep -q "^ii  $package "; then
        MISSING_PACKAGES="$MISSING_PACKAGES $package"
    fi
done

if [ ! -z "$MISSING_PACKAGES" ]; then
    echo "Missing required packages:$MISSING_PACKAGES"
    echo "Please install them using:"
    echo "sudo apt install$MISSING_PACKAGES"
    exit 1
fi

# Install Python package
echo "Installing Python package..."
pip3 install --user -e .

# Create desktop entry
echo "Creating desktop entry..."
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/xfce4-xr-desktop.desktop << EOL
[Desktop Entry]
Version=1.0
Type=Application
Name=XFCE4 XR Desktop
Comment=XR desktop integration for XFCE4
Exec=xfce4-xr-desktop
Icon=display
Terminal=false
Categories=Settings;DesktopSettings;X-XFCE;X-XFCE-SettingsDialog;
EOL

# Create autostart entry
echo "Creating autostart entry..."
mkdir -p ~/.config/autostart
cp ~/.local/share/applications/xfce4-xr-desktop.desktop ~/.config/autostart/

echo "Installation complete!"
echo "You can now start XFCE4 XR Desktop from the applications menu or it will start automatically on login." 