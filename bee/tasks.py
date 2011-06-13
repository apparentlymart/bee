
from celery.decorators import task


@task()
def test(foo=None):
    return "Hi! You sent me %r" % foo

