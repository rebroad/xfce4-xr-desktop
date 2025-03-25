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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/xfce4-xr-desktop.git
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

4. Configure XFCE4:
```bash
./configure_xfce4.sh
```

## Usage

1. Start the XR desktop:
```bash
xfce4-xr-desktop
```

2. Use keyboard shortcuts:
- `Ctrl+Super+\`: Toggle XR effect
- `Ctrl+Super+Space`: Recenter display
- `Ctrl+Super+Enter`: Toggle display distance
- `Ctrl+Super+F`: Toggle follow mode

## Configuration

Configuration can be done through the XFCE4 Settings Manager under the XR Desktop section.

## Development

This project is under active development. Contributions are welcome!

## License

This project is licensed under the GNU General Public License v3 or later - see the LICENSE file for details. 