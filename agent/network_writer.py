from interface_agent import IWriter


class  NetworkWriter(IWriter):

    def send_data(self, data: str, machine_name: str) -> None:
        pass