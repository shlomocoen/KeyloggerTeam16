from agent.interface_agent import IWriter

class FileWriter(IWriter):

    def send_data(self, data: str, machine_name: str) -> None: # הפונקציה מקבלת מחרוזת str ושם קובץ וכותבת לקובץ את המחרוזת
        with open(machine_name, "a") as f:
            f.write(data)