#!/usr/bin/env python

import os
import subprocess
import sys

from app import create_app # noqa

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2, failfast=True).run(tests)


@app.cli.command()
def lint():
    """Runs the code linter"""
    lint = subprocess.call(['flake8', '--ignore=E402',
                            'manage.py', 'tests/', 'app/']) == 0
    if lint:
        print('OK')
    sys.exit(lint)
