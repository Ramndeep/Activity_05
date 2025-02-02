""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Ramandeep Kaur
Date: 01-12-2024
"""
from sports_app.sports_app import SportsApp

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = SportsApp()
    window.show()
    sys.exit(app.exec())