from flask.ext.script import Manager
from pastebin import app, db
import os

manager = Manager(app)


@manager.command
def initdb():
    """Creates all database tables."""
    db.create_all()


@manager.command
def dropdb():
    """Drops all database tables."""
    db.drop_all()


if __name__ == '__main__':
    # Builds the server configuration
    if os.getenv('IP'):
      IP    = os.getenv('IP')
    else:
      IP    = '0.0.0.0'
    
    if os.getenv('PORT'):
      PORT  = int(os.getenv('PORT'))
    else:
      PORT  = 8080
    
    # Print statements go to your log file in production; to your console while developing
    print ("Running server at http://{0}:{1}/".format(IP, PORT))
    app.run(host = IP, port = PORT, debug = True, threaded = True)
