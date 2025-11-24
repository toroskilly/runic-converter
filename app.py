from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging

from runic_converter import RunicConverter, RuneSystem

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Configure logging
logging.basicConfig(level=logging.INFO)

class RunicConverterAPI:
    def __init__(self):
        # Initialize your converter here
        # self.converter = RunicConverter()
        pass
    
    def convert_text(self, text, system=None):
        """Convert text to runic script(s)"""
        try:
            if system:
                # Convert to specific runic system
                return self.converter.convert(text, system)
            else:
                # Convert to all systems as shown in your script [1]
                return self.converter.convert_all_systems(text)
        except Exception as e:
            raise Exception(f"Conversion error: {str(e)}")

# Initialize converter
converter_api = RunicConverterAPI()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """API endpoint for text conversion"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'Text is required'}), 400
        
        text = data['text'].strip()
        system = data.get('system')  # Optional specific system
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        # Convert text using your existing logic [1]
        results = converter_api.convert_text(text, system)
        
        return jsonify({
            'success': True,
            'original_text': text,
            'conversions': results
        })
        
    except Exception as e:
        app.logger.error(f"Conversion error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/systems', methods=['GET'])
def get_systems():
    """Get available runic systems"""
    try:
        # Return available RuneSystem options from your script
        systems = [system.value for system in RuneSystem]
        return jsonify({'systems': systems})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get converter information"""
    # Based on the info displayed in your script [1]
    info = {
        'note': 'Runic writing was phonetic - spell words as they sound!',
        'examples': [
            "The letter 'X' becomes 'KS'",
            "'TH' is a single rune"
        ]
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
