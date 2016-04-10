from app import app
from flask.ext.script import Manager

manager = Manager(app)


@manager.command
def run():
    app.run(host='0.0.0.0', port=9001)


if __name__ == "__main__":
    manager.run()
