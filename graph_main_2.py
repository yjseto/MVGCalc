import sys
from gui.app import MvgCalcApplication
from gui.displays.basic import BasicCalcDisplay
from gui.displays.graph import GraphDisplay

def main():
    try:
        app = MvgCalcApplication(sys.argv)
        window = GraphDisplay(app)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        # Handle the exception gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
