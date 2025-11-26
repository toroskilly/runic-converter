from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging

from runic_converter import RuneConverter, RuneSystem

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Configure logging
logging.basicConfig(level=logging.INFO)

class RunicConverterAPI:
    def __init__(self):
        # Initialize the converter - THIS WAS THE MISSING PART
        self.converter = RuneConverter()
    
    def convert_text(self, text, system=None):
        """Convert text to runic script(s)"""
        try:
            if system:
                # Convert to specific runic system
                # First need to get the RuneSystem enum from the string
                system_enum = None
                for rs in RuneSystem:
                    if rs.value == system:
                        system_enum = rs
                        break
                
                if system_enum:
                    return {system: self.converter.convert(text, system_enum)}
                else:
                    raise ValueError(f"Unknown runic system: {system}")
            else:
                # Convert to all systems
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
    info = {
        'title': 'Historical Runic Writing Systems Converter',
        'description': 'Convert modern English text to various historical runic alphabets',
        'note': 'Runic writing was phonetic - spell words as they sound!',
        'systems': {
            'Elder Futhark': '24 runes, 2nd-8th century, Proto-Germanic',
            'Younger Futhark': '16 runes, 9th-11th century, Viking Age',
            'Short-Twig': 'Swedish-Norwegian variant of Younger Futhark',
            'Anglo-Saxon Futhorc': '28-33 runes, 5th-11th century, used in England',
            'Medieval': 'Post-1100, Latinized Futhark',
            'Staveless': 'Simplified forms used in Hälsingland, Sweden'
        },
        'examples': [
            "The letter 'X' becomes 'KS'",
            "'TH' is a single rune (þ - thorn)",
            "'QU' becomes 'KW'",
            "Double letters are often simplified",
            "Numbers and special characters are preserved"
        ],
        'tips': [
            'Try your name first!',
            'Historical inscriptions often omitted vowels',
            'Runes were carved in stone, wood, or metal',
            'Each rune had a name and symbolic meaning'
        ]
    }
    return jsonify(info)

@app.route('/api/transliterate', methods=['POST'])
def transliterate():
    """API endpoint for transliterating runes back to Latin alphabet"""
    try:
        data = request.get_json()
        
        if not data or 'runic_text' not in data:
            return jsonify({'error': 'Runic text is required'}), 400
        
        runic_text = data['runic_text'].strip()
        
        if not runic_text:
            return jsonify({'error': 'Runic text cannot be empty'}), 400
        
        # Transliterate using the converter
        result = converter_api.converter.transliterate_runes(runic_text)
        
        return jsonify({
            'success': True,
            'runic_text': runic_text,
            'transliteration': result
        })
        
    except Exception as e:
        app.logger.error(f"Transliteration error: {str(e)}")
        return jsonify({'error': str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
