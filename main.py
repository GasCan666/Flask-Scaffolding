from App import App
import os

App.initialize()

for root, dirnames, filenames in os.walk("./BluePrint/"):
    for dirname in dirnames:
        path = str(os.path.join(root, dirname))
        if path[-3:] == "_bp":
            # In case you are using windows
            path = path.replace("\\", "/")
            __import__(path.replace("/", ".")[2:] + ".setup")

if __name__ == '__main__':
    App.run_instance()

print("___")

