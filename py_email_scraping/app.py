import os
import subprocess
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    domain = data.get('domain')

    if not domain:
        return jsonify({"error": "No domain specified"}), 400

    # Create a temporary file to store the output
    output_file = 'emails.json'
    
    # Run the Scrapy spider
    result = subprocess.run(
        ['scrapy', 'crawl', 'marketparts', '-a', f'domain={domain}', '-o', output_file],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return jsonify({"error": "Failed to run spider", "details": result.stderr}), 500

    # Read the output file
    with open(output_file, 'r') as f:
        emails = json.load(f)

    # Clean up the output file
    os.remove(output_file)

    return jsonify(emails)

if __name__ == '__main__':
    app.run(debug=True)
