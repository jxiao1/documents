Flask Sqlite3
=============

Using Sqlite3 with Flash :
http://flask.pocoo.org/docs/0.10/patterns/sqlite3/#sqlite3

Python sqlite3 standard library :
https://docs.python.org/2/library/sqlite3.html

Module functions and constants::

    connect(db-path[, timeout, ...])

Connection Objects::

    cursor()
    commit()
    rollback()
    close()

Cursor Objects::

    execute(sql[, parameters])
    executemany(sql, seq_of_parameters)
    executescript(sql_script)
    fetchone()
    fetchmany([size=cursor.arraysize])
    fetchall()

Example::

    # -*- coding: utf-8 -*-                                                                                   
                                                                                                              
    import os                                                                                                                                                                                                           
    import sqlite3                                                                                            
    from flask import g                                                                                       
                                                                                                              
    class Sqlite3DB():                                                                                        
        app = None                                                                                            
                                                                                                              
        @classmethod                                                                                          
        def bindapp(cls, app):                                                                                
            cls.app = app                                                                                     
                                                                                                              
        @classmethod                                                                                          
        def connect(cls):                                                                                     
            if not hasattr(g, 'sqlite_db'):                                                                   
                assert cls.app is not None, 'Application is not binded to DB'                                 
                path = cls.app.config.get('DATABASE')                                                         
                assert path is not  None, 'DB path is not set!'                                               
                if not os.path.isfile(path):                                                                  
                    cls.app.logger.debug('Initialize the DB')                                                 
                    db = sqlite3.connect(path)                                                                
                    with cls.app.open_resource('../database/schema.sql', mode='r') as f:                      
                        db.cursor().executescript(f.read())                                                   
                    db.commit()                                                                               
                else:                                                                                         
                    cls.app.logger.debug('Connect the DB')                                                    
                    db = sqlite3.connect(path)                                                                
                db.row_factory = sqlite3.Row                                                                  
                                                                                                              
                g.sqlite_db = db                                                                              
            return g.sqlite_db                                                                                
                                                                                                              
        @classmethod                                                                                          
        def fetchall(cls, sql):                                                                               
            cls.app.logger.debug('Fetch all entries in the DB')                                               
            db = cls.connect()                                                                                
            cur = db.cursor().execute(sql)                                                                    
            return cur.fetchall()                                                                             
                                                                                                              
        @classmethod                                                                                          
        def addone(cls, sql, data=None):                                                                      
            db = cls.connect()                                                                                
            db.cursor().execute(sql, data)                                                                    
            db.commit()                                                                                       
                                                                                                              
        @classmethod                                                                                          
        def close(cls):                                                                                       
            db = cls.connect()                                                                                
            db.close()      
