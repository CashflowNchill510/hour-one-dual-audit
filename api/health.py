from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "ok": True,
            "desk": "hour-one-dual-audit",
            "stamp": "SHX-20260903-0206",
            "note": "add-only health. not a new product.",
        }).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return
