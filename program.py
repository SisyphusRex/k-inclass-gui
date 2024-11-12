"""Program code"""

# David Barnes
# CIS 226
# 05-28-23

# Internal imports.
from beverage import BeverageCollection
from user_interface import UserInterface
from utils import CSVProcessor
from gui_user_interface import BeverageListWindow


def main(*args):
    """Method to run program"""

    # Set a constant for the path to the CSV file
    PATH_TO_CSV = "./datafiles/beverage_list.csv"

    # Create an instance of User Interface class
    ui = UserInterface()

    # Create an instance of the BeverageCollection class.
    beverage_collection = BeverageCollection()

    # Create an instance of the CSVProcessor class.
    csv_processor = CSVProcessor()

    # Create and run main window
    main_window = BeverageListWindow(beverage_collection, csv_processor, PATH_TO_CSV)
    main_window.run()
