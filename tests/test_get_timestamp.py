from datetime import datetime
from invisibleroads_macros_log import get_timestamp


def test_get_timestamp_variable():
    when = datetime.now()
    assert get_timestamp().startswith(str(when.year))


def test_get_timestamp_fixed():
    when = datetime.now()
    assert get_timestamp(when).startswith(str(when.year))
