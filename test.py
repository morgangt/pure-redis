import pytest
from unittest import mock 

from redis import Redis


class TestRedis:

    def setup(self):
        pass

    def test_method_ping(self):
        """Testing method ping."""
        with mock.patch("socket.socket") as mock_server:
            mock_server.return_value.recv.return_value = b"+PONG\r\n"
            redis = Redis()
            result = redis.ping()
        
        assert result == "PONG"

    def test_method_set(self):
        """Testing method get."""
        with mock.patch("socket.socket") as mock_server:
            mock_server.return_value.recv.return_value = b"+OK\r\n"
            redis = Redis()
            result = redis.set("test_key", "test_value")

            assert result == True

    def test_method_get(self):
        """Testing method get."""
        with mock.patch("socket.socket") as mock_server:
            mock_server.return_value.recv.return_value = b"$5\r\nHello\r\n"
            redis = Redis()
            result = redis.get("mykey")
            print("[result]", result)
            assert result == "Hello"
