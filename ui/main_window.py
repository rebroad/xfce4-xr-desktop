import logging
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject
from core.xr_manager import XRManager
from utils.config import Config

class MainWindow(Gtk.Window):
    def __init__(self, xr_manager: XRManager, config: Config):
        super().__init__(title="XFCE4 XR Desktop")
        self.logger = logging.getLogger('xfce4_xr_desktop.main_window')
        self.xr_manager = xr_manager
        self.config = config
        
        self.setup_ui()
        self.setup_signals()
        self.setup_keybindings()

    def setup_ui(self):
        """Set up the user interface."""
        # Main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(main_box)

        # Status section
        status_frame = Gtk.Frame(label="Status")
        status_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        status_frame.add(status_box)
        main_box.pack_start(status_frame, False, False, 6)

        # Device status
        self.device_status = Gtk.Label(label="Device: Not Connected")
        status_box.pack_start(self.device_status, False, False, 6)

        # Controls section
        controls_frame = Gtk.Frame(label="Controls")
        controls_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        controls_frame.add(controls_box)
        main_box.pack_start(controls_frame, False, False, 6)

        # Display distance
        distance_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        distance_label = Gtk.Label(label="Display Distance (m):")
        self.distance_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL,
            adjustment=Gtk.Adjustment(
                value=self.config.display_distance,
                lower=0.5,
                upper=3.0,
                step_increment=0.05
            )
        )
        distance_box.pack_start(distance_label, False, False, 6)
        distance_box.pack_start(self.distance_scale, True, True, 6)
        controls_box.pack_start(distance_box, False, False, 6)

        # Widescreen mode
        self.widescreen_switch = Gtk.Switch()
        self.widescreen_switch.set_active(self.config.widescreen_mode)
        widescreen_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        widescreen_label = Gtk.Label(label="Widescreen Mode:")
        widescreen_box.pack_start(widescreen_label, False, False, 6)
        widescreen_box.pack_start(self.widescreen_switch, False, False, 6)
        controls_box.pack_start(widescreen_box, False, False, 6)

        # Follow mode
        self.follow_switch = Gtk.Switch()
        self.follow_switch.set_active(self.config.follow_mode)
        follow_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        follow_label = Gtk.Label(label="Follow Mode:")
        follow_box.pack_start(follow_label, False, False, 6)
        follow_box.pack_start(self.follow_switch, False, False, 6)
        controls_box.pack_start(follow_box, False, False, 6)

        # Follow threshold
        threshold_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        threshold_label = Gtk.Label(label="Follow Threshold:")
        self.threshold_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL,
            adjustment=Gtk.Adjustment(
                value=self.config.follow_threshold,
                lower=0.01,
                upper=0.5,
                step_increment=0.01
            )
        )
        threshold_box.pack_start(threshold_label, False, False, 6)
        threshold_box.pack_start(self.threshold_scale, True, True, 6)
        controls_box.pack_start(threshold_box, False, False, 6)

        # Buttons
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.recenter_button = Gtk.Button(label="Recenter Display")
        self.refresh_button = Gtk.Button(label="Refresh")
        button_box.pack_start(self.recenter_button, True, True, 6)
        button_box.pack_start(self.refresh_button, True, True, 6)
        controls_box.pack_start(button_box, False, False, 6)

        # Keybindings section
        keybindings_frame = Gtk.Frame(label="Keybindings")
        keybindings_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        keybindings_frame.add(keybindings_box)
        main_box.pack_start(keybindings_frame, False, False, 6)

        # Add keybinding labels
        keybindings = [
            ("Toggle XR", "toggle_xr"),
            ("Recenter Display", "recenter"),
            ("Toggle Distance", "toggle_distance"),
            ("Toggle Follow", "toggle_follow")
        ]

        for label_text, action in keybindings:
            keybinding_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
            keybinding_label = Gtk.Label(label=f"{label_text}:")
            keybinding_value = Gtk.Label(label=self.config.get_keybinding(action))
            keybinding_box.pack_start(keybinding_label, False, False, 6)
            keybinding_box.pack_start(keybinding_value, True, True, 6)
            keybindings_box.pack_start(keybinding_box, False, False, 6)

        # Set window properties
        self.set_default_size(400, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

    def setup_signals(self):
        """Set up signal connections."""
        # Connect window close event to quit properly
        self.connect('delete-event', self._on_window_delete)

        # Connect to XR manager signals
        self.xr_manager.connect('device-connected', self._on_device_connected)
        self.xr_manager.connect('display-distance-changed', self._on_display_distance_changed)
        self.xr_manager.connect('widescreen-mode-changed', self._on_widescreen_mode_changed)

        # Connect UI signals
        self.distance_scale.connect('value-changed', self._on_distance_changed)
        self.widescreen_switch.connect('notify::active', self._on_widescreen_toggled)
        self.follow_switch.connect('notify::active', self._on_follow_toggled)
        self.threshold_scale.connect('value-changed', self._on_threshold_changed)
        self.recenter_button.connect('clicked', self._on_recenter_clicked)
        self.refresh_button.connect('clicked', self._on_refresh_clicked)

    def setup_keybindings(self):
        """Set up global keybindings."""
        # TODO: Implement XFCE4 keybinding integration
        pass

    def _on_device_connected(self, xr_manager, connected):
        """Handle device connection status changes."""
        self.device_status.set_text(f"Device: {'Connected' if connected else 'Not Connected'}")

    def _on_display_distance_changed(self, xr_manager, distance):
        """Handle display distance changes."""
        self.distance_scale.set_value(distance)

    def _on_widescreen_mode_changed(self, xr_manager, enabled):
        """Handle widescreen mode changes."""
        self.widescreen_switch.set_active(enabled)

    def _on_distance_changed(self, scale):
        """Handle display distance slider changes."""
        distance = scale.get_value()
        self.xr_manager.set_display_distance(distance)
        self.config.display_distance = distance

    def _on_widescreen_toggled(self, switch, param):
        """Handle widescreen mode toggle."""
        enabled = switch.get_active()
        self.xr_manager.toggle_widescreen_mode()
        self.config.widescreen_mode = enabled

    def _on_follow_toggled(self, switch, param):
        """Handle follow mode toggle."""
        enabled = switch.get_active()
        self.xr_manager.toggle_follow_mode()
        self.config.follow_mode = enabled

    def _on_threshold_changed(self, scale):
        """Handle follow threshold slider changes."""
        threshold = scale.get_value()
        self.xr_manager.set_follow_threshold(threshold)
        self.config.follow_threshold = threshold

    def _on_recenter_clicked(self, button):
        """Handle recenter button click."""
        self.xr_manager.recenter_display()

    def _on_refresh_clicked(self, button):
        """Handle refresh button click."""
        self.xr_manager._check_device_connection()

    def _on_window_delete(self, widget, event):
        """Handle window close event."""
        self.logger.info("Window closing, cleaning up...")
        if self.xr_manager:
            self.xr_manager.cleanup()
        Gtk.main_quit()
        return False  # Allow the window to be destroyed
