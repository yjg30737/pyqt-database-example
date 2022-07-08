from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QStyledItemDelegate, QMainWindow, QLabel, QTableView, QAbstractItemView, QPushButton, \
    QHBoxLayout, QSpacerItem, QSizePolicy, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class QtDatabaseExample(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle("Qt Database Example")

        # table name
        tableName = "contacts"

        # label
        lbl = QLabel(tableName)

        # Database table
        # Set up the model
        self.__model = QSqlTableModel(self)
        self.__model.setTable(tableName)
        self.__model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.__model.setHeaderData(0, Qt.Horizontal, "ID")
        self.__model.setHeaderData(1, Qt.Horizontal, "Name")
        self.__model.setHeaderData(2, Qt.Horizontal, "Job")
        self.__model.setHeaderData(3, Qt.Horizontal, "Email")
        self.__model.select()
        # self.__model.installEventFilter(self)

        # Set up the view
        self.__view = QTableView()
        self.__view.setModel(self.__model)
        delegate = AlignDelegate()
        self.__view.setItemDelegateForColumn(0, delegate)
        self.__view.setItemDelegateForColumn(1, delegate)
        self.__view.setItemDelegateForColumn(2, delegate)
        self.__view.setItemDelegateForColumn(3, delegate)
        self.__view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__view.resizeColumnsToContents()
        self.__view.setSelectionMode(QAbstractItemView.SingleSelection)

        # add/delete buttons
        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.__add)
        delBtn = QPushButton('Delete')
        delBtn.clicked.connect(self.__delete)

        lay = QHBoxLayout()
        lay.addWidget(lbl)
        lay.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.MinimumExpanding))
        lay.addWidget(addBtn)
        lay.addWidget(delBtn)
        lay.setContentsMargins(0, 0, 0, 0)
        btnWidget = QWidget()
        btnWidget.setLayout(lay)

        # main widget
        lay = QVBoxLayout()
        lay.addWidget(btnWidget)
        lay.addWidget(self.__view)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __add(self):
        r = self.__model.record()
        r.setValue("name", '')
        r.setValue("job", '')
        r.setValue("email", '')
        self.__model.insertRecord(-1, r)
        self.__model.select()

    def __delete(self):
        self.__model.removeRow(self.__view.currentIndex().row())
        self.__model.select()

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

def initDatabase():
    table = 'contacts'

    clearTableQuery = QSqlQuery()
    clearTableQuery.prepare(
        f'DELETE FROM {table}'
    )
    clearTableQuery.exec()

    createTableQuery = QSqlQuery()
    createTableQuery.prepare(
        f"""
        CREATE TABLE {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )
    createTableQuery.exec()

    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
        f"""
        INSERT INTO {table} (
            name,
            job,
            email
        )
        VALUES (?, ?, ?)
        """
    )

    # Sample data
    data = [
        ("Joe", "Senior Web Developer", "joe@example.com"),
        ("Lara", "Project Manager", "lara@example.com"),
        ("David", "Data Analyst", "david@example.com"),
        ("Jane", "Senior Python Developer", "jane@example.com"),
    ]

    # Use .addBindValue() to insert data
    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()