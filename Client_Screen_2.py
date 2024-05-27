import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Client__Screen import Ui_ClientMainWindow


class Client(QtWidgets.QMainWindow, Ui_ClientMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # SAVE BUTTON "ADD ITEM IN FILE.TXT"
        self.Save_btn.clicked.connect(self.save_click)
        self.Search_btn.clicked.connect(self.search_click)
        self.Delete_btn.clicked.connect(self.delete_click)

    def save_click(self):
        with open("Client_Data.txt", "a") as file_data:
            file_data.write(self.Client.text() + "," +
                            self.Product.text() + "," + self.Quantity.text() + "\n")

        # SEARCH BUTTON "SEARCH ITEM IN FILE.TXT"

    def search_click(self):
        product_found = False
        with open("Client_Data.txt", "r") as file_data:
            lines = file_data.readlines()
            for line in lines:
                if (self.Client.text() + "," + self.Product.text() + "," + self.Quantity.text() + "\n") == line:
                    product_found = True

            if product_found:
                print("Product Found")
            else:
                print("Product Not Found")

        # DELETE BUTTON "DELETE ITEM IN FILE.TXT"

    def delete_click(self):
        with open("Client_Data.txt", "r") as file_data:
            lines = file_data.readlines()

        if (self.Client.text() + "," + self.Product.text() + "," + self.Quantity.text() + "\n") in lines:
            lines.remove(self.Client.text() + "," +
                         self.Product.text() + "," + self.Quantity.text() + "\n")

        with open("Client_Data.txt", "w") as file_data:
            for line in lines:
                file_data.write(line)


        self.Client.clear()
        self.Product.clear()
        self.Quantity.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Client()
    main_window.show()
    sys.exit(app.exec_())
