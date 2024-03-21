from PyQt5.QtWidgets import QApplication
from pyqt_database_example import createConnection, initTable, addSample, QtDatabaseExample

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    initTable() # Create table. After create table, you don't need to do it unless you want to make the table to empty.
    # addSample()
    # Add sample records (Joe, Lara, David, Jane. See result image below.)
    ex = QtDatabaseExample()
    ex.show()
    sys.exit(app.exec_())