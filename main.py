#!/usr/bin/env python3
import sys
import logging
from gi.repository import Gtk, Gdk, Xfce
from core.xr_manager import XRManager
from ui.main_window import MainWindow
from utils.config import Config

class XFCE4XRDesktop:
    def __init__(self):
        self.logger = self._setup_logging()
        self.config = Config()
        self.xr_manager = XRManager()
        self.main_window = None
        
    def _setup_logging(self):
        logger = logging.getLogger('xfce4_xr_desktop')
        logger.setLevel(logging.DEBUG)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        
        logger.addHandler(ch)
        return logger

    def run(self):
        try:
            # Initialize XR manager
            if not self.xr_manager.initialize():
                self.logger.error("Failed to initialize XR manager")
                return False

            # Create and show main window
            self.main_window = MainWindow(self.xr_manager, self.config)
            self.main_window.show_all()

            # Start the GTK main loop
            Gtk.main()
            return True

        except Exception as e:
            self.logger.error(f"Error running application: {str(e)}")
            return False
        finally:
            self.cleanup()

    def cleanup(self):
        if self.xr_manager:
            self.xr_manager.cleanup()
        if self.main_window:
            self.main_window.destroy()

def main():
    app = XFCE4XRDesktop()
    success = app.run()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 