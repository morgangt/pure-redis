import socket


class Redis:
    """Simple redis server, write witout external links dependes."""

    def __init__(self, host: str = '127.0.0.1', port: int = 6379, db: int =0):
        self.host = host
        self.port = port
        self.db = db
        self.coding = "utf-8"
        
        self.__bond = self.__connection()

    def __connection(self) -> object:
        """Creating connection to redis server."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, self.db)
        
        return sock

    def __preparating_string(self, command: str) -> bytes:
        """Preparating string for request."""
        requst = bytes(f"{command}\r\n", self.coding)
        return requst

    def __get_next_msg(self) -> str:
        """Geting next message from redis."""

        data = self.__bond.recv(1024).decode("utf-8")
        return data

    def check_response(self, response: bytes) -> str:
        """Check completed command."""
        res = response.decode("utf-8")
        return res == "+OK\r\n"

    def serialize_response(self, string: str):
        """Serialize response data."""
        data = string.split("\r\n")
        
        if int(data[0].replace("$", "")) == len(data[1]):
            return data[1]
            
        return False

    def set(self, key: str, value: str) -> str:
        """Command set (setting), write in redis value by key."""
        cmd = "SET"
        string = self.__preparating_string(f"{cmd} {key} \"{value}\"")        
        self.__bond.sendall(string)

        data = self.check_response(self.__bond.recv(1024))
        
        return data

    def get(self, command: str) -> (str, bool):
        """Command get on key for geting data form redis."""
        cmd = "GET"
        string = self.__preparating_string(f"{cmd} {command}")
        self.__bond.sendall(string)
        data = self.serialize_response(self.__get_next_msg())
        
        return data

    def ping(self) -> str:
        """Command ping redis server."""
        
        string = self.__preparating_string(f"PING")
        self.__bond.sendall(string)
        data = self.__bond.recv(1024).decode("utf-8")
                
        return data.replace("+", "").replace("\r\n", "")


if __name__ == "__main__":
    r = Redis()
    print(r.ping())
    print(r.set("mykey", "Hello"))
    print(r.get("myke"))
