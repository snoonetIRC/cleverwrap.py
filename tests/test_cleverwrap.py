import pytest

from cleverwrap import CleverWrap
from cleverwrap.errors import UnknownAPIError


def test_init():
    cw = CleverWrap("API_KEY")

    assert cw.key == "API_KEY"


def test_say(mock_requests):
    mock_requests.add(
        mock_requests.GET,
        'https://www.cleverbot.com/getreply?input=Hello&key=API_KEY&cs=&conversation_id=&wrapper=CleverWrap.py',
        match_querystring=True,
        json={
            'cs': 'AAAABBCCDD',
            'output': 'Hello.',
            'interaction_count': "2",
            'conversation_id': "foobar",
            'time_taken': "15",
            'time_elapsed': "13",
        },
    )
    cw = CleverWrap("API_KEY")

    assert cw.say("Hello") == "Hello."

    assert cw.default_conversation.convo_id

    cw.reset()

    assert not cw.default_conversation.convo_id


def test_api_error(mock_requests):
    cw = CleverWrap("API_KEY")

    with pytest.raises(UnknownAPIError):
        cw.say("Hello")
