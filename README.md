#### mike, here is what to do.

* in a shell, go to where your code is that you will run predictions with
* `git submodule add https://github.com/vepkenez/simple-snakemq-messaging.git control`
* `pip install snakemq`
* `cp .\control\example.py ./reeplicate.py` ( or whatever you want to call it )
* `python reeplicate.py`
