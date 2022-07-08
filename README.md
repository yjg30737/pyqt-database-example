# pyqt-database-example
PyQt Database (mainly SQLite) basic use example

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-database-examp
le.git --upgrade`

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_database_example import createConnection, QtDatabaseExample

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    # initDatabase()
    ex = QtDatabaseExample()
    ex.show()
    sys.exit(app.exec_())
