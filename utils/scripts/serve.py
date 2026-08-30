#!/usr/bin/env python3
"""
===============================================================================
LearningCpp - Servidor de Desarrollo Local de Alto Rendimiento
===============================================================================
Inicia un servidor HTTP local optimizado para servir el portal educativo
web/, soportando rutas SPA, páginas de error 404 y activos multimedia de módulos.
Uso:
  python utils/scripts/serve.py
===============================================================================
"""

import http.server
import socketserver
import os
import sys

PORT = 8000
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
WEB_DIR = os.path.join(REPO_ROOT, "web")

class LearningCppServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        # Limpiar parámetros de query string y anclas
        clean_path = self.path.split('?')[0].split('#')[0]
        if clean_path.startswith('/'):
            clean_path = clean_path[1:]

        # 1. Intentar resolver en web/
        target_file = os.path.normpath(os.path.join(WEB_DIR, clean_path))

        # 2. Si apunta a un módulo raíz (ej: 01_GettingStarted/... o ../01_...) resolver en REPO_ROOT
        if not os.path.exists(target_file) or os.path.isdir(target_file):
            alt_path = os.path.normpath(os.path.join(REPO_ROOT, clean_path.replace("..", "")))
            if os.path.exists(alt_path) and not os.path.isdir(alt_path):
                target_file = alt_path

        if os.path.isdir(target_file):
            index_path = os.path.join(target_file, "index.html")
            if os.path.exists(index_path):
                target_file = index_path

        # 3. Manejo de error 404 con página personalizada
        if not os.path.exists(target_file) or os.path.isdir(target_file):
            target_file = os.path.join(WEB_DIR, "404.html")
            status_code = 404
        else:
            status_code = 200

        try:
            with open(target_file, "rb") as f:
                content = f.read()

            ctype = self.guess_type(target_file)
            self.send_response(status_code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache, must-revalidate")
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Server Error: {e}")

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    print(f"\n{'='*70}")
    print(f"🚀 Servidor Web LearningCpp Activo en: http://localhost:{PORT}")
    print(f"📁 Directorio Web: {WEB_DIR}")
    print(f"🛑 Presiona Ctrl+C para detener el servidor")
    print(f"{'='*70}\n")
    try:
        with socketserver.TCPServer(("", PORT), LearningCppServer) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
