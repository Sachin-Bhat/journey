import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QLineEdit)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt, QDateTime

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Slider")
        self.setGeometry(100, 100, 1000, 600)
        self.create_layout()

    def create_layout(self):
        # Create horizontal slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        current_datetime = QDateTime.currentDateTime()
        self.slider.setMaximum(current_datetime.toSecsSinceEpoch())
        self.slider.setValue(self.slider.maximum())
        self.slider.valueChanged.connect(self.slider_changed)

        # Create image label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create text field
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Text field")
        self.text_field.setFont(QFont("Arial", 12))

        # Create vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_field, alignment=Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    def slider_changed(self, value):
        # Convert seconds to datetime
        datetime_object = QDateTime.fromSecsSinceEpoch(value)
        time_string = datetime_object.toString("yyyy-MM-dd hh:mm:ss")
        
        # Display the slider value in the text field
        self.text_field.setText(f"Slider value: {time_string}")

        # Load and display the corresponding image based on the slider value
        image_path = f"path/to/images/{time_string}.jpg"  # Replace with your image path
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())