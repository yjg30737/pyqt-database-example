# pyqt-database-example
PyQt Database (SQLite) basic use example

## Requirements
* PyQt5 >= 5.8

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

![image](https://user-images.githubusercontent.com/55078043/177899335-92eaaa55-62e6-4072-ad35-f22af6a53ea3.png)

'contacts' is table's name.

Add button literally adds new empty record.

Delete button deletes selected row. (Only one row can be selected currently)

## See Also

* <a href="https://realpython.com/python-pyqt-database/#reader-comments">Handling SQL Databases With PyQt: The Basics</a> - I made this thanks to this article.
