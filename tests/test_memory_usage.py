from jsonmodels.fields import StringField
from jsonmodels.models import Base


class User(Base):

    name = StringField()


def test_garbage_collecting():
    first = len(User.name.memory)
    instance = User(name='Bob')
    second = len(User.name.memory)
    User(name='Frank')
    third = len(User.name.memory)
    del instance
    four = len(User.name.memory)

    assert first < second
    assert second == third
    assert third > four
    assert first == four
