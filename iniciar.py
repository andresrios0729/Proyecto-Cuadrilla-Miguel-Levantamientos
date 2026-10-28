from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

root = Path(__file__).resolve().parent
with ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(root))) as server:
    url = f'http://127.0.0.1:{server.server_port}/'
    print(f'Visor Cuadrilla USabana: {url}')
    print('Mantén esta ventana abierta. Para detener el visor, pulsa Ctrl+C.')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
