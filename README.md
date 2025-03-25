# XFCE4 XR Desktop

A virtual desktop extension for XFCE4 that enables XR (Extended Reality) functionality with compatible AR glasses like the Xreal Air 2 Pro.

## Features

- Virtual desktop display in AR glasses
- Head tracking support
- Adjustable display distance and size
- Widescreen mode support
- Smooth follow mode
- Keyboard shortcuts for common actions

## Requirements

- XFCE4 desktop environment
- Python 3.8 or higher
- GTK3
- X11
- Compatible AR glasses (tested with Xreal Air 2 Pro)
- XR driver (installed via Breezy Desktop or similar)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rebroad/xfce4-xr-desktop.git
cd xfce4-xr-desktop
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the XR driver:
```bash
./install_xr_driver.sh
```

4. Install the XFCE4 XR Desktop application:
```bash
./install.sh
```

## Usage Instructions

### Initial Setup

1. Before plugging in your AR glasses:
   - Make sure you have the XR driver installed and working
   - Start the XFCE4 XR Desktop application from the applications menu or run:
     ```bash
     xfce4-xr-desktop
     ```
   - The application window will show "Device: Not Connected"

2. Plug in your AR glasses:
   - Connect your AR glasses via USB
   - The application should automatically detect the device and update the status
   - If not, click the "Refresh" button in the application

### Basic Usage

1. Display Controls:
   - Use the "Display Distance" slider to adjust how far away the display appears
   - Toggle "Widescreen Mode" for a wider field of view
   - Toggle "Follow Mode" to enable/disable smooth head tracking
   - Adjust "Follow Threshold" to control how sensitive the display is to head movement

2. Keyboard Shortcuts:
   - `Ctrl+Super+\`: Toggle XR effect
   - `Ctrl+Super+Space`: Recenter display
   - `Ctrl+Super+Enter`: Toggle display distance
   - `Ctrl+Super+F`: Toggle follow mode

3. Troubleshooting:
   - If the display is not showing up, try unplugging and replugging the AR glasses
   - Use the "Recenter Display" button if the display position is off
   - Check the application logs for any error messages

### Advanced Usage

1. Configuration:
   - Settings are automatically saved to `~/.config/xfce4-xr-desktop/config.json`
   - You can manually edit this file for advanced settings

2. Multiple Displays:
   - The application will use the primary display by default
   - Additional display support is planned for future releases

## Development

This project is under active development. Contributions are welcome!

### Building from Source

1. Clone the repository:
```bash
git clone https://github.com/rebroad/xfce4-xr-desktop.git
cd xfce4-xr-desktop
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Install in development mode:
```bash
pip install -e .
```

### Running Tests

```bash
python -m pytest tests/
```

## License

This project is licensed under the GNU General Public License v3 or later - see the LICENSE file for details.
