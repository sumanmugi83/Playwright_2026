from flask import Flask, request, jsonify, render_template_string
import os
import sys

# Add current directory to path to import converter
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from convert_gherkin import convert_gherkin_to_playwright

app = Flask(__name__)

# Basic embedded HTML UI for simplicity
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gherkin to Playwright Converter</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a1a1a; color: #ffffff; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; display: flex; gap: 20px; height: 90vh; }
        .column { flex: 1; display: flex; flex-direction: column; }
        textarea { flex: 1; background: #2d2d2d; color: #fff; border: 1px solid #444; padding: 15px; font-family: 'Consolas', monospace; resize: none; border-radius: 5px; }
        button { margin: 10px 0; padding: 15px; background: #007acc; color: white; border: none; cursor: pointer; font-size: 16px; border-radius: 5px; transition: background 0.3s; }
        button:hover { background: #005fa3; }
        h2 { margin-top: 0; }
        pre { flex: 1; background: #2d2d2d; border: 1px solid #444; padding: 15px; margin: 0; overflow: auto; border-radius: 5px; font-family: 'Consolas', monospace; color: #a5d6ff; }
        .loading { display: none; text-align: center; color: #aaa; margin: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="column">
            <h2>Gherkin Input</h2>
            <textarea id="gherkinInput" placeholder="Feature: ..."></textarea>
            <button onclick="convert()">Convert to Playwright 🚀</button>
            <div id="loading" class="loading">Converting with CodeLlama...</div>
        </div>
        <div class="column">
            <h2>Playwright Output</h2>
            <pre id="outputCode">// Output will appear here...</pre>
        </div>
    </div>

    <script>
        async function convert() {
            const input = document.getElementById('gherkinInput').value;
            if (!input) return;
            
            document.getElementById('loading').style.display = 'block';
            document.getElementById('outputCode').textContent = "Processing...";
            
            try {
                const response = await fetch('/api/convert', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ gherkin_content: input })
                });
                
                const data = await response.json();
                
                if (data.status === 'success' && data.files.length > 0) {
                    document.getElementById('outputCode').textContent = data.files[0].content;
                } else {
                    document.getElementById('outputCode').textContent = "Error: " + (data.logs ? data.logs.join('\\n') : 'Unknown error');
                }
            } catch (e) {
                document.getElementById('outputCode').textContent = "Network Error: " + e;
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    gherkin = data.get('gherkin_content', '')
    result = convert_gherkin_to_playwright(gherkin)
    return jsonify(result)

if __name__ == '__main__':
    print("Starting B.L.A.S.T. Converter UI...")
    app.run(host='0.0.0.0', port=5000)
