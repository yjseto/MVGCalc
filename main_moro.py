import sys
import pickle as pk
from gui.containers.app import MvgCalcApplication
from gui.containers.window import MvgCalcMainWindow
from lib.util.persistence import load_all
SAVE_FILE = 'results.pkl'

def main():
    try:
        open(SAVE_FILE,"wb").close()
        #something that clear results on start
        app = MvgCalcApplication(sys.argv)
        window = MvgCalcMainWindow(app)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        # Handle the exception gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
 