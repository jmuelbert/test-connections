from __future__ import annotations

import os
import sys

class Application():
    """Application class."""
    def __init__(self, exit_func, *args, **kwargs):
        """Initializes the Application class."""
        super().__init__(*args, **kwargs)
        self.exit = exit_func
        # self.config_file = ConfigFile()
        
