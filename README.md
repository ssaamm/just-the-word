just-the-word
=============

A simple site which displays a different Bible passage every day

Check it out at [CoffeeAndTheWord.tk](http://coffeeandtheword.tk/)

Installation
------------

* Clone repo
* ```pip install flask```
* ```pip install requests```
* Run these functions in ```tools/db.py```:
  * ```init_db()```
  * ```init_plan()``` (reads from stdin; make sure you pipe in a ```plan.txt```)
* Move the ```plan.db``` file into the same directory as ```app.py```

### ```plan.txt```

A ```plan.txt``` file should contain a series of Bible references, with each
line containing the readings for one day. If more than one passage should be
read on a day, separate each passage with a semicolon.
