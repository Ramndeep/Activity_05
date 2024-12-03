import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from player.player import Player

class SportsApp(QWidget):
    """
    A class to maintain Sports Players.

    Attributes:
        table (QTableWidget): Displays a table of players.
        button (QPushButton): A button to trigger a welcome message.
    """
    def __init__(self):
        """
        Initializes the SportsApp class.
        """
        super().__init__()
        self.__initialize_widgets()

        self.button.clicked.connect(self.__show_message)

    def __initialize_widgets(self):
        """
        Performs specific gui initialization.
        """
        self.setWindowTitle("Sports League")

        layout = QVBoxLayout()

        # Create the table
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Position"])

        # Hard-coded data
        players = [
            Player("John Doe", 25, "Forward"),
            Player("Jane Smith", 28, "Midfielder"),
            Player("Jim Brown", 22, "Defender")
        ]

        for i, player in enumerate(players):
            self.table.setItem(i, 0, QTableWidgetItem(player.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(player.age)))
            self.table.setItem(i, 2, QTableWidgetItem(player.position))

        self.table.resizeColumnsToContents()
        
        layout.addWidget(self.table)

        # Create the button
        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.setLayout(layout)

    def __show_message(self):
        """
        Displays a welcome message to the user.
        """
        QMessageBox.information(self, "Welcome", "Welcome to the Team!")
