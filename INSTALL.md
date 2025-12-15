# Installation Guide for XFCE4 XR Desktop

## Current Status

✅ **Code is ready to install!** I've fixed the following issues:
- Removed invalid `Xfce` import
- Added proper `gi.require_version()` calls
- Connected recenter button signal handler
- Added refresh button to UI

## Prerequisites

### 1. System Dependencies

Install required system packages:
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

Note: The `gir1.2-xfce4ui-2` package mentioned in install.sh may not be needed since we're not using XFCE4-specific bindings (the Xfce import was removed).

### 2. XR Driver Installation

**This is the critical missing piece!** The application needs the XR driver to be installed. Based on the code, it expects:

- XR driver CLI at: `~/.local/bin/xr_driver_cli`
- Shared memory files:
  - `/dev/shm/xr_driver_control` (for sending commands)
  - `/dev/shm/xr_driver_state` (for reading status)

You'll need to install **Breezy Desktop** or a similar XR driver that provides these interfaces. The driver should:
- Detect XReal AR glasses connected via DisplayPort
- Provide the shared memory communication interface
- Handle the actual display virtualization

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

2. **Install Python dependencies:**
   ```bash
   cd ~/src/xfce4-xr-desktop
   pip3 install --user -r requirements.txt
   ```

3. **Install the application:**
   ```bash
   cd ~/src/xfce4-xr-desktop
   ./install.sh
   ```

4. **Install XR Driver:**
   - You'll need to install Breezy Desktop or the XReal Linux driver
   - This should provide the `xr_driver_cli` and shared memory interfaces
   - Check if it's available at: https://github.com/breezy-team/breezy-desktop

## Testing

After installation, you can test if the application runs (even without the XR driver):

```bash
xfce4-xr-desktop
```

The application should start and show "Device: Not Connected" if the XR driver isn't running.

## Troubleshooting

### "XR driver CLI not found"
- Install the XR driver (Breezy Desktop or similar)
- Ensure `~/.local/bin/xr_driver_cli` exists

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

