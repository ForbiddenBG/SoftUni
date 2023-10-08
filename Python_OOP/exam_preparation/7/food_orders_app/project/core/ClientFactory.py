from project.client import Client


class ClientFactory:

    @staticmethod
    def create_a_client(phone_number):
        return Client(phone_number)
