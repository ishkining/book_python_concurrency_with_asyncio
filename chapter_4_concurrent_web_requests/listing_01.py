import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


class ConnectedSocket:

    def __init__(self, server_socket):
        self._connection = None
        self._server_scoket = server_socket

    async def __aenter__(self):
        print('Looking to this hole, waiting for consent')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_scoket)
        self._connection = connection
        print('Get a consent')
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        print('After putting out a lil johnson')
        self._connection.close()
        print('Thank u next')


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)


asyncio.run(main())
