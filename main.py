import os, webview
from Extensions.handler import *

if not os.path.exists('.assets/config.json'):
    window = webview.create_window('Setup', f'file://{os.path.join(os.path.dirname(__file__), '#assets', 'setup.html')}')
    webview.start()
else:
    # run the actual client
    pass
