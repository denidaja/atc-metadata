#!/usr/bin/env python3
"""
Simple HTTP Server for Albania Travel Metadata Editor
Serves the JSON editor and data files to avoid CORS issues
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 8080
EDITOR_FILE = "json-editor.html"

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Request Handler with CORS headers enabled"""
    
    def end_headers(self):
        # Add CORS headers to allow local file access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        # Custom logging to show cleaner messages
        timestamp = self.log_date_time_string()
        client_ip = self.client_address[0]
        
        # Only log actual file requests, not favicon etc.
        if not args[0].endswith('favicon.ico'):
            print(f"[{timestamp}] {client_ip} - {format % args}")

def find_available_port(start_port=8080, max_attempts=10):
    """Find an available port starting from start_port"""
    import socket
    
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    
    return None

def main():
    # Change to the script's directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if the editor file exists
    if not Path(EDITOR_FILE).exists():
        print(f"❌ Error: {EDITOR_FILE} not found in {script_dir}")
        print("Make sure you're running this from the atc-metadata directory.")
        sys.exit(1)
    
    # Find available port
    port = find_available_port(PORT)
    if port is None:
        print(f"❌ Error: Could not find an available port starting from {PORT}")
        sys.exit(1)
    
    # Start the server
    try:
        with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
            server_url = f"http://localhost:{port}"
            editor_url = f"{server_url}/{EDITOR_FILE}"
            
            print("🚀 Albania Travel Metadata Editor Server Starting...")
            print("=" * 60)
            print(f"📁 Serving directory: {script_dir}")
            print(f"🌐 Server URL: {server_url}")
            print(f"📝 Editor URL: {editor_url}")
            print("=" * 60)
            print("🎯 Opening editor in your default browser...")
            print("⏹️  Press Ctrl+C to stop the server")
            print()
            
            # Open the editor in the default browser
            try:
                webbrowser.open(editor_url)
                print("✅ Browser opened successfully!")
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"👉 Please open manually: {editor_url}")
            
            print()
            print("📊 Server Activity:")
            print("-" * 30)
            
            # Serve forever
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("🛑 Server stopped by user")
        print("👋 Thanks for using the Albania Travel Metadata Editor!")
        print("=" * 60)
    except OSError as e:
        print(f"❌ Error starting server: {e}")
        if "Address already in use" in str(e):
            print(f"💡 Port {port} is already in use. Try closing other applications or restart your computer.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()