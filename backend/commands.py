import click
from flask.cli import with_appcontext

from .database import db
from .models import URL

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()