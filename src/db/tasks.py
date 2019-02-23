from invoke import task
from .base import Base, engine

@task
def db_update(ctx):
    """
    Make changes to database schema.
    """

    Base.metadata.create_all(engine)
