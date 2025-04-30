print(">> LOADING run.py from:", __file__)
from app import app
print(">> run.app is:", app)
if __name__ == "__main__":

    app.run()