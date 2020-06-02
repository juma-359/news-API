from app import create_app
from flask import Manager,Server

#creating app instance
app = creat_app('development')

manager = manager(app)

manager.add_command('server',Server)
@manager.command
def test():
    """run the unit tests"""
    import unittest
    test=unitnest.TestLoader().discover('tests')
    unittest.TextRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run()