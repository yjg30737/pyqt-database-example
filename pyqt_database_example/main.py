from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QStyledItemDelegate, QMainWindow, QLabel, QTableView, QAbstractItemView, QPushButton, \
    QHBoxLayout, QWidget, QVBoxLayout, QMessageBox, QComboBox

from pyqt_database_example.instantSearchBar import InstantSearchBar


# for search feature
class FilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.__searchedText = ''

    @property
    def searchedText(self):
        return self.__searchedText

    @searchedText.setter
    def searchedText(self, value):
        self.__searchedText = value
        self.invalidateFilter()


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter


class QtDatabaseExample(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle("Qt Database Example")

        # table name
        tableName = "contacts"

        # label
        lbl = QLabel(tableName.capitalize())

        columnNames = ['ID', 'Name', 'Job', 'Email', 'City Escape', 'Wild Canyon', 'Prison Lane']

        # database table
        # set up the model
        self.__tableModel = QSqlTableModel(self)
        self.__tableModel.setTable(tableName)
        self.__tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        for i in range(len(columnNames)):
            self.__tableModel.setHeaderData(i, Qt.Orientation.Horizontal, columnNames[i])
        self.__tableModel.select()

        # init the proxy model
        self.__proxyModel = FilterProxyModel()

        # set the table model as source model to make it enable to feature sort and filter function
        self.__proxyModel.setSourceModel(self.__tableModel)

        # set up the view
        self.__view = QTableView()
        self.__view.setModel(self.__proxyModel)

        # align to center
        delegate = AlignDelegate()
        for i in range(self.__tableModel.columnCount()):
            self.__view.setItemDelegateForColumn(i, delegate)

        # set selection/resize policy
        self.__view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.__view.resizeColumnsToContents()
        self.__view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        # sort (ascending order by default)
        self.__view.setSortingEnabled(True)
        self.__view.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        # add/delete buttons
        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.__add)
        delBtn = QPushButton('Delete')
        delBtn.clicked.connect(self.__delete)

        # instant search bar
        self.__searchBar = InstantSearchBar()
        self.__searchBar.setPlaceHolder('Search...')
        self.__searchBar.searched.connect(self.__showResult)

        # combo box to make it enable to search by each column
        self.__comboBox = QComboBox()
        items = ['All'] + columnNames
        for i in range(len(items)):
            self.__comboBox.addItem(items[i])
        self.__comboBox.currentIndexChanged.connect(self.__currentIndexChanged)

        # set layout
        lay = QHBoxLayout()
        lay.addWidget(lbl)
        lay.addWidget(self.__searchBar)
        lay.addWidget(self.__comboBox)
        lay.addWidget(addBtn)
        lay.addWidget(delBtn)
        lay.setContentsMargins(0, 0, 0, 0)
        btnWidget = QWidget()
        btnWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(btnWidget)
        lay.addWidget(self.__view)

        # main widget
        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        # show default result (which means "show all")
        self.__showResult('')

    def __add(self):
        r = self.__tableModel.record()
        r.setValue("name", '')
        r.setValue("job", '')
        r.setValue("email", '')
        self.__tableModel.insertRecord(-1, r)
        self.__tableModel.select()

    def __delete(self):
        self.__tableModel.removeRow(self.__view.currentIndex().row())
        self.__tableModel.select()

    def __showResult(self, text):
        # index -1 will be read from all columns
        # otherwise it will be read the current column number indicated by combobox
        self.__proxyModel.setFilterKeyColumn(self.__comboBox.currentIndex()-1)
        # regular expression can be used
        self.__proxyModel.setFilterRegularExpression(text)

    def __currentIndexChanged(self, idx):
        self.__showResult(self.__searchBar.getSearchBar().text())

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

def initTable():
    table = 'contacts'

    dropTableQuery = QSqlQuery()
    dropTableQuery.prepare(
        f'DROP TABLE {table}'
    )
    dropTableQuery.exec()

    createTableQuery = QSqlQuery()
    createTableQuery.prepare(
        f"""
        CREATE TABLE {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL,
            city_escape TIME,
            wild_canyon TIME,
            prison_lane TIME
        )
        """
    )
    createTableQuery.exec()

def addSample():
    table = 'contacts'

    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
        f"""
        INSERT INTO {table} (
            name,
            job,
            email,
            city_escape,
            wild_canyon,
            prison_lane
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """
    )

    # Sample data
    data = [
        ("Joe", "Senior Web Developer", "joe@example.com", "2:51", "1:12", "3:15"),
        ("Lara", "Project Manager", "lara@example.com", "3:25", "2:31", "4:27"),
        ("David", "Data Analyst", "david@example.com", "3:41", "7:33", "5:02"),
        ("Jane", "Senior Python Developer", "jane@example.com", "3:10", "2:43", "3:43"),
    ]

    # Use .addBindValue() to insert data
    for name, job, email, city_escape, wild_canyon, prison_lane in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.addBindValue(city_escape)
        insertDataQuery.addBindValue(wild_canyon)
        insertDataQuery.addBindValue(prison_lane)
        insertDataQuery.exec()