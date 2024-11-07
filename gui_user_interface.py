"""simple beverage management GUI"""

#Third_Party Downloads
import FreeSimpleGUI as sg

#First Party Imports
from errors import AlreadyImportedError

class BeverageListWindow:
    """simple Beverage List"""

    def __init__(self, beverage_collection, csv_processor, path_to_csv):
        """constructor"""
        self.beverage_collection = beverage_collection
        self.csv_processor = csv_processor
        self.path_to_csv = path_to_csv

        layout = [
            [sg.Text("Beverage List")],
        ]

        self.window = sg.Window("Beverage List", layout)