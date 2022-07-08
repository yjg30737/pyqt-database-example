# pyqt-database-example
PyQt Database (mainly SQLite) basic use example

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-database-example.git --upgrade`

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
    initTable() # Create table
    addSample() # Add sample records
    ex = QtDatabaseExample()
    ex.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/177899335-92eaaa55-62e6-4072-ad35-f22af6a53ea3.png)

## See Also

* <a href="https://realpython.com/python-pyqt-database/#reader-comments">Handling SQL Databases With PyQt: The Basics</a> - I made this thanks to this article.
