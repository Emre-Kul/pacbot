from pacbot.app import App
from pacbot.replay import ReplayApp
import sys

if len(sys.argv) > 1 and sys.argv[1] == "replay":
    replayApp = ReplayApp()
    replayApp.start()
else:
    app = App()
    app.start()
