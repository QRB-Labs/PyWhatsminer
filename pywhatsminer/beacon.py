import socket
from contextlib import suppress
from networkscan import Networkscan

from pywhatsminer.client import Client


class Beacon(Client):
    """
    ## This class allows you to combine groups of miners, as well as automatically find new machines.
    """
    def __init__(self, auto_find: bool = True, *clients: Client):
        self.clients: list[Client] = [*clients]
        
        if auto_find: self.find()
        
        
    def find(self, network: str = "192.168.0.0/24"):
        scan = Networkscan(network)

        scan.run()

        for ip in scan.list_of_hosts_found:
            with suppress(socket.error):
                client = Client(ip)

                if client.System.get_status():
                    self.clients.append(client)


    def __repr__(self):
        return f"Beacon({self.clients})"
