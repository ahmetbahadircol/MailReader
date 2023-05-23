import os


class TextReader:

    def read(self, key: str, file_name: str, path: str = None):
        if not path:
            self.path = os.getcwd()

        with open(file_name, "r") as f:
            for line in f.readlines():
                line = line.replace(" ", "").replace("\n", "")
                splitted_key = line.split("=")

                if not len(splitted_key) == 2:
                    raise ValueError("The environment variable must be key and value pair seperated by '='")

                file_key = splitted_key[0]
                file_value = splitted_key[-1]

                if key == file_key:
                    return file_value

            f.close()

        return None
