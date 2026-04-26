from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QLabel, QStatusBar, QTabWidget
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("{{PROJECT_NAME}}")
        self.setMinimumSize({{WINDOW_WIDTH}}, {{WINDOW_HEIGHT}})
        self._init_ui()

    def _init_ui(self):
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        # Tab widget — add tabs here as features grow
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Placeholder tab
        placeholder = QWidget()
        p_layout = QVBoxLayout(placeholder)
        label = QLabel("{{DESCRIPTION}}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        p_layout.addWidget(label)
        self.tabs.addTab(placeholder, "Home")

        # Status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Ready")
