from agent.interface_agent import IWriter

class FileWriter(IWriter):

    def send_data(self, data, machine_name) -> None:
        with open(machine_name, "a") as f:
            f.write(data)
