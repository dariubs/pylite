pylite
====
Intract with sqlite3 in python as simple as it can be.

Install
-------

```shell
pip install pylite
```

Tips
----

Import pylite :

```python
from pylite import Pylite
```

Create a new database or open an existing database :

```python
db = Pylite('dbname')
```

Add a table :

```python
db.add_table('table_name',column1='datatype',column2='datatype',...,columnN='datatype')
```

Insert data :

```python
db.insert('table_name','column1_value','column2_value',...,'columnN_value')
```

Remove items :

```python
db.remove('table_name','condition')
```

Retrieve items :

```python
db.get_items('table_name','condition')
```

Get all tables name :

```python
db.get_tables()
```
Execute your sqlite queries:

```python
db.query('your query')
```

Close connection :

```python
db.close_connection()
```
