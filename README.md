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
- XR driver that provides shared memory interface (must work with XFCE4 - **NOT Breezy Desktop**, which is GNOME/KDE only)

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
   - **Important:** Breezy Desktop only works with GNOME/KDE, not XFCE4
   - You'll need an XR driver that works with XFCE4 and provides the shared memory interface
   - Check XReal's official Linux driver documentation
   - The driver must provide `xr_driver_cli` and shared memory files at `/dev/shm/xr_driver_*`

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

There are two types of installations:

1. **Regular Installation** (for users who just want to use the application):
```bash
git clone https://github.com/rebroad/xfce4-xr-desktop.git
cd xfce4-xr-desktop
pip install -r requirements.txt  # Install only the required dependencies
./install.sh
```

2. **Development Installation** (for contributors and developers):
```bash
git clone https://github.com/rebroad/xfce4-xr-desktop.git
cd xfce4-xr-desktop
pip install -r requirements.txt         # Install required dependencies
pip install -r requirements-dev.txt     # Install development tools
pip install -e .                        # Install in editable mode
```

### Development Tools

The `requirements-dev.txt` file includes tools that are only needed if you plan to contribute to the project:

- `pytest`: For writing and running unit tests
- `black`: For automatic code formatting to maintain consistent style
- `flake8`: For code linting to catch potential errors
- `mypy`: For static type checking

These development tools help maintain code quality but are not needed for regular users who just want to run the application.

### Running Tests

If you have installed the development dependencies, you can run the tests:

```bash
python -m pytest tests/
```

### Code Style

We use several tools to maintain code quality:

```bash
black .              # Format code
mypy .              # Check types
flake8              # Run linter
```

## License

This project is licensed under the GNU General Public License v3 or later - see the LICENSE file for details.
