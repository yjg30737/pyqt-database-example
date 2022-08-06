# pyqt-database-example
PyQt database (SQLite) basic use example

## Requirements
* PyQt5 >= 5.12 - Because one of QSortFilterProxyModel's function(setFilterRegularExpression) requires at least 5.12. This is indeed very convinient function so you don't have to worry.

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-database-example.git --upgrade`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-instant-search-bar.git">pyqt-instant-search-bar</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_database_example import createConnection, initTable, addSample, QtDatabaseExample

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    initTable() # Create table. After create table, you don't need to do it unless you want to make the table to empty.
    # addSample() Add sample records (Joe, Lara, David, Jane. See result image below.)
    ex = QtDatabaseExample()
    ex.show()
    sys.exit(app.exec_())
```

![image](https://user-images.githubusercontent.com/55078043/177900006-31577341-84f3-4d87-bfff-36765fc3334c.png)

If you execute the script, "contacts.sqlite" SQLite database file will be made.

Result


![image](https://user-images.githubusercontent.com/55078043/183241774-786ad283-2461-4ef7-8b7e-f3c27c25ae92.png)

'contacts' is table's name.

You can search the text with search bar. (instant search)

You can also set the column to search with combobox which is placed right next to search bar.

Add button literally adds new empty record.

Delete button deletes selected row. (Only one row can be selected currently)

### Search bar example

Let's set the column to search as "Name" and search the text "Dav".

![image](https://user-images.githubusercontent.com/55078043/183241795-5cb1a0cc-a551-4f0e-add7-f01ae7e7085e.png)

## See Also

* <a href="https://realpython.com/python-pyqt-database/#reader-comments">Handling SQL Databases With PyQt: The Basics</a> - I made this thanks to this article.
