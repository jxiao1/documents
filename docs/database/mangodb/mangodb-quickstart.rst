MongonDB QuickStart
===================

Overview
--------

| https://www.mongodb.org/
| https://docs.mongodb.com/manual/
| http://docs.mongoing.com/manual-zh
| http://www.runoob.com/mongodb/mongodb-tutorial.html
|

A record in MongoDB is a document, which is a data structure composed of field and value pairs.
MongoDB documents are similar to JSON objects. The values of fields may include other documents,
arrays, and arrays of documents.

MongoDB stores documents in collections. Collections are analogous to tables in relational databases.
Unlike a table, however, a collection does not require its documents to have the same schema.


ubuntu Setup 
------------

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

.. note:: MongoDB only provides packages for 64-bit LTS (long-term support) Ubuntu releases.

**Install V3.2**::

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    sudo apt-get update
    sudo apt-get install mongodb-org


**Configuration**:

https://docs.mongodb.com/manual/reference/configuration-options/

Create sub folders::
    mkdir mongodb-simple && cd mongodb-simple
    mkdir data conf log

Create special conf file::

    cp /etc/mongod.conf ./conf/

    # vi dbpath and log path in the conf file
    storage:
        dbPath: ./data
    systemLog:
        path: ./log/mongod.log
    processManagement:
       fork: true


**Start**::

    $ mongod -f conf/mongod.conf


**Stop**::

    kill <mongod-pid>  # kill or kill -15, don't use kill -9

**Operators in JavaScript syntax compatiable Mongo shell**::

    $ mongo   # Connect "localhost:<defaultPort>/test" by default

    $ use mydb  # use database, create new one if it doesn't exist.
    $ db.user.insert({name:"xxx", age:18})  # create at first
    $ db.user.find()
    { "_id" : ObjectId("549a6cae1cdcaf3b048887b8"), "age" : 18, "name" : "xxx" }
    

| CURD Operator: http://docs.mongodb.org/manual/crud/)
| Query Operator: http://docs.mongodb.org/manual/reference/operator/
| Shell Methods: http://docs.mongodb.org/manual/reference/method/
|

Online Test
-----------

http://try.mongodb.org/?_ga=1.266362574.1339800818.1419400475
