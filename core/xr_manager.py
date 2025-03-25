import os
import logging
from gi.repository import GObject, Gdk, Xfce

class XRManager(GObject.Object):
    __gsignals__ = {
        'device-connected': (GObject.SignalFlags.RUN_FIRST, None, (bool,)),
        'display-distance-changed': (GObject.SignalFlags.RUN_FIRST, None, (float,)),
        'widescreen-mode-changed': (GObject.SignalFlags.RUN_FIRST, None, (bool,)),
    }

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('xfce4_xr_desktop.xr_manager')
        self._device_connected = False
        self._display_distance = 1.05  # Default distance in meters
        self._widescreen_mode = False
        self._follow_mode = True
        self._follow_threshold = 0.1  # Default threshold in radians
        
        # Paths for XR driver communication
        self._control_path = '/dev/shm/xr_driver_control'
        self._state_path = '/dev/shm/xr_driver_state'
        self._cli_path = os.path.expanduser('~/.local/bin/xr_driver_cli')

    def initialize(self):
        """Initialize the XR manager and check for device connection."""
        try:
            # Check if XR driver CLI exists
            if not os.path.exists(self._cli_path):
                self.logger.error(f"XR driver CLI not found at {self._cli_path}")
                return False

            # Check if device is connected
            self._check_device_connection()
            
            # Set up initial state
            self._write_control('display_distance', str(self._display_distance))
            self._write_control('follow_mode', 'true' if self._follow_mode else 'false')
            self._write_control('follow_threshold', str(self._follow_threshold))
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize XR manager: {str(e)}")
            return False

    def cleanup(self):
        """Clean up resources and disable XR mode."""
        try:
            self._write_control('disable_xr', 'true')
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}")

    def _check_device_connection(self):
        """Check if a supported XR device is connected."""
        try:
            if not os.path.exists(self._state_path):
                self._device_connected = False
                return

            with open(self._state_path, 'r') as f:
                state = dict(line.strip().split('=') for line in f if '=' in line)
            
            self._device_connected = state.get('device_connected', 'false').lower() == 'true'
            self.emit('device-connected', self._device_connected)
            
        except Exception as e:
            self.logger.error(f"Error checking device connection: {str(e)}")
            self._device_connected = False

    def _write_control(self, key, value):
        """Write a control command to the XR driver."""
        try:
            with open(self._control_path, 'w') as f:
                f.write(f"{key}={value}\n")
        except Exception as e:
            self.logger.error(f"Error writing control command: {str(e)}")
            raise

    def _read_state(self):
        """Read the current state from the XR driver."""
        try:
            if not os.path.exists(self._state_path):
                return {}
            
            with open(self._state_path, 'r') as f:
                return dict(line.strip().split('=') for line in f if '=' in line)
        except Exception as e:
            self.logger.error(f"Error reading state: {str(e)}")
            return {}

    def set_display_distance(self, distance):
        """Set the display distance in meters."""
        try:
            self._display_distance = float(distance)
            self._write_control('display_distance', str(self._display_distance))
            self.emit('display-distance-changed', self._display_distance)
        except Exception as e:
            self.logger.error(f"Error setting display distance: {str(e)}")

    def toggle_widescreen_mode(self):
        """Toggle widescreen mode."""
        try:
            self._widescreen_mode = not self._widescreen_mode
            self._write_control('widescreen_mode', 'true' if self._widescreen_mode else 'false')
            self.emit('widescreen-mode-changed', self._widescreen_mode)
        except Exception as e:
            self.logger.error(f"Error toggling widescreen mode: {str(e)}")

    def toggle_follow_mode(self):
        """Toggle smooth follow mode."""
        try:
            self._follow_mode = not self._follow_mode
            self._write_control('follow_mode', 'true' if self._follow_mode else 'false')
        except Exception as e:
            self.logger.error(f"Error toggling follow mode: {str(e)}")

    def set_follow_threshold(self, threshold):
        """Set the follow threshold in radians."""
        try:
            self._follow_threshold = float(threshold)
            self._write_control('follow_threshold', str(self._follow_threshold))
        except Exception as e:
            self.logger.error(f"Error setting follow threshold: {str(e)}")

    def recenter_display(self):
        """Recenter the display position."""
        try:
            self._write_control('recenter', 'true')
        except Exception as e:
            self.logger.error(f"Error recentering display: {str(e)}")

    @property
    def device_connected(self):
        return self._device_connected

    @property
    def display_distance(self):
        return self._display_distance

    @property
    def widescreen_mode(self):
        return self._widescreen_mode

    @property
    def follow_mode(self):
        return self._follow_mode 