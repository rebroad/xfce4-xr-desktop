# Installation Guide for XFCE4 XR Desktop

## Current Status

✅ **Code is ready to install!** I've fixed the following issues:
- Removed invalid `Xfce` import
- Added proper `gi.require_version()` calls
- Connected recenter button signal handler
- Added refresh button to UI

## Prerequisites

### 1. System Dependencies

The `install.sh` script **checks** for required packages but does **not install them automatically**. You need to install them manually:

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

Note: The `gir1.2-xfce4ui-2` package mentioned in install.sh may not be needed since we're not using XFCE4-specific bindings (the Xfce import was removed). The install script will tell you if any packages are missing.

### 2. XR Driver Installation

**This is the critical missing piece!** The application needs an XR driver that provides the shared memory interface. Based on the code, it expects:

- XR driver CLI at: `~/.local/bin/xr_driver_cli`
- Shared memory files:
  - `/dev/shm/xr_driver_control` (for sending commands)
  - `/dev/shm/xr_driver_state` (for reading status)

**Important:** Breezy Desktop only works with GNOME/KDE, not XFCE4. This project is specifically designed to work with XFCE4, so you'll need a different XR driver solution.

The driver should:
- Detect XReal AR glasses connected via DisplayPort
- Provide the shared memory communication interface (`/dev/shm/xr_driver_control` and `/dev/shm/xr_driver_state`)
- Handle the actual display virtualization
- Work independently of desktop environment (or specifically support XFCE4)

**Note:** You may need to find or develop an XR driver that works with XFCE4, or adapt an existing one. The official XReal Linux driver may provide these interfaces - check XReal's official documentation.

### 3. Python Dependencies

Install Python packages:
```bash
cd ~/src/xfce4-xr-desktop
pip3 install --user -r requirements.txt
```

## Installation Steps

1. **Install system dependencies:**
   ```bash
   sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
   ```
   Note: The `install.sh` script will check for these and tell you if any are missing, but won't install them automatically.

2. **Install Python dependencies:**
   ```bash
   cd ~/src/xfce4-xr-desktop
   pip3 install --user -r requirements.txt
   ```
   Note: The `install.sh` script runs `pip3 install --user -e .` which installs the package itself, but you may want to install requirements.txt first to ensure all dependencies are available.

3. **Install the application:**
   ```bash
   cd ~/src/xfce4-xr-desktop
   ./install.sh
   ```
   This will:
   - Check for required system packages (and tell you to install them if missing)
   - Install the Python package with `pip3 install --user -e .`
   - Create desktop entry and autostart entry

4. **Install XR Driver:**
   - **XRLinuxDriver:** xfce4-xr-desktop uses XRLinuxDriver's native command names
   - Build and install from: `~/src/XRLinuxDriver`
   - See `~/src/XRLinuxDriver/BUILD_NOTES.md` for build instructions
   - The XRLinuxDriver provides:
	 - `~/.local/bin/xr_driver_cli`
	 - `/dev/shm/xr_driver_control` (xfce4-xr-desktop writes commands directly)
	 - `/dev/shm/xr_driver_state` (includes `device_connected` flag)
   - **Note:** Breezy Desktop only works with GNOME/KDE, but XRLinuxDriver itself is desktop-agnostic and works with XFCE4

## Testing

After installation, you can test if the application runs (even without the XR driver):

```bash
xfce4-xr-desktop
```

The application should start and show "Device: Not Connected" if the XR driver isn't running.

## Troubleshooting

### "XR driver CLI not found"
- Install an XR driver that works with XFCE4 (not Breezy Desktop, which is GNOME/KDE only)
- Ensure `~/.local/bin/xr_driver_cli` exists
- Check XReal's official Linux driver or look for XFCE4-compatible alternatives

### "ImportError: cannot import name Xfce"
- ✅ **Fixed!** This was removed in the latest changes

### Application starts but device never connects
- Check if XR driver is running: `ls -la /dev/shm/xr_*`
- Check if XReal glasses are connected: `xrandr | grep -i xreal`
- Your `fix_displays.sh` script should automatically detect XReal displays

## Next Steps

1. **Install XR Driver** - This is the main blocker
2. **Test with XReal glasses** - Connect via DisplayPort and verify detection
3. **Implement keybindings** - The TODO for XFCE4 keybinding integration remains
4. **Add error handling** - Better messages when XR driver is missing

