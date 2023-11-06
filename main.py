import sys

from gui.containers.app import MvgCalcApplication
from gui.containers.window import MvgCalcMainWindow

def main():
    try:
        app = MvgCalcApplication(sys.argv)
        window = MvgCalcMainWindow(app)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        # Handle the exception gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
 