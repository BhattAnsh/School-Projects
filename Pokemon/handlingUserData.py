import json
import os

class UserDataHandler:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def openingFilePath(self, file_path):
        empty_file = False
        data = {}

        if os.path.isfile(file_path):
            if os.stat(file_path).st_size < 0:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    empty_file = True
            else:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                
        else:
            with open(file_path, 'w') as file:
                json.dump({}, file)

        return data, empty_file

    def storingData(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def signUp(self):
        file_path = 'userData.json'
        data, empty = self.openingFilePath(file_path)

        if empty:
            data = {
                self.name: {
                    "passwords": [self.password],
                    "pokemons":[],
                    "balls":0
                }
            }
        else:
            if self.name in data:
                print("This user name already exists please choose other user name")
            else:
                data[self.name] = {
                    "passwords": [self.password],
                    "pokemons":[],
                    "balls":0
                }
        self.storingData(file_path, data)
    

    def login(self):
        file_path = 'userData.json'
        data, empty_file = self.openingFilePath(file_path)
        print(data.keys)