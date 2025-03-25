import os
import json
import logging
from gi.repository import GObject

class Config(GObject.Object):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('xfce4_xr_desktop.config')
        self._config_dir = os.path.expanduser('~/.config/xfce4-xr-desktop')
        self._config_file = os.path.join(self._config_dir, 'config.json')
        self._default_config = {
            'display_distance': 1.05,
            'widescreen_mode': False,
            'follow_mode': True,
            'follow_threshold': 0.1,
            'keybindings': {
                'toggle_xr': '<Control><Super>backslash',
                'recenter': '<Control><Super>space',
                'toggle_distance': '<Control><Super>Return',
                'toggle_follow': '<Control><Super>f'
            }
        }
        self._config = self._load_config()

    def _load_config(self):
        """Load configuration from file or create default."""
        try:
            if not os.path.exists(self._config_dir):
                os.makedirs(self._config_dir)

            if os.path.exists(self._config_file):
                with open(self._config_file, 'r') as f:
                    config = json.load(f)
                    # Merge with default config to ensure all keys exist
                    return {**self._default_config, **config}
            else:
                self._save_config(self._default_config)
                return self._default_config.copy()

        except Exception as e:
            self.logger.error(f"Error loading config: {str(e)}")
            return self._default_config.copy()

    def _save_config(self, config):
        """Save configuration to file."""
        try:
            with open(self._config_file, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            self.logger.error(f"Error saving config: {str(e)}")

    def get(self, key, default=None):
        """Get a configuration value."""
        return self._config.get(key, default)

    def set(self, key, value):
        """Set a configuration value and save to file."""
        self._config[key] = value
        self._save_config(self._config)

    def get_keybinding(self, action):
        """Get a keybinding for a specific action."""
        return self._config['keybindings'].get(action)

    def set_keybinding(self, action, keybinding):
        """Set a keybinding for a specific action."""
        self._config['keybindings'][action] = keybinding
        self._save_config(self._config)

    @property
    def display_distance(self):
        return self.get('display_distance')

    @display_distance.setter
    def display_distance(self, value):
        self.set('display_distance', float(value))

    @property
    def widescreen_mode(self):
        return self.get('widescreen_mode')

    @widescreen_mode.setter
    def widescreen_mode(self, value):
        self.set('widescreen_mode', bool(value))

    @property
    def follow_mode(self):
        return self.get('follow_mode')

    @follow_mode.setter
    def follow_mode(self, value):
        self.set('follow_mode', bool(value))

    @property
    def follow_threshold(self):
        return self.get('follow_threshold')

    @follow_threshold.setter
    def follow_threshold(self, value):
        self.set('follow_threshold', float(value)) 