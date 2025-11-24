#!/usr/bin/env python3
import re
from typing import Dict, List, Optional, Tuple
from enum import Enum

class RuneSystem(Enum):
    """Available runic writing systems"""
    ELDER_FUTHARK = "Elder Futhark (24 runes, 2nd-8th century)"
    YOUNGER_FUTHARK = "Younger Futhark (16 runes, 9th-11th century)"
    SHORT_TWIG = "Short-Twig/Rök (Swedish-Norwegian variant)"
    ANGLO_SAXON = "Anglo-Saxon Futhorc (28-33 runes, 5th-11th century)"
    MEDIEVAL = "Medieval/Latinized Futhark (post-1100)"
    STAVELESS = "Staveless/Hälsinge (simplified forms)"

class RuneConverter:
    """
    Convert modern English text to various historical runic alphabets.
    Each system represents a different historical period and region.
    """
    
    def __init__(self):
        """Initialize the converter with all runic alphabets"""
        self._init_elder_futhark()
        self._init_younger_futhark()
        self._init_short_twig()
        self._init_anglo_saxon()
        self._init_medieval()
        self._init_staveless()
        
    def _init_elder_futhark(self):
        """
        Elder Futhark (Proto-Germanic)
        The oldest runic alphabet, 24 runes, used 2nd-8th century CE
        """
        self.elder_futhark = {
            # First Aett (Freyr's Aett)
            'f': 'ᚠ',  # fehu - cattle, wealth
            'u': 'ᚢ',  # uruz - aurochs, strength
            'th': 'ᚦ', # thurisaz - giant, thorn
            'þ': 'ᚦ',  # thorn
            'ð': 'ᚦ',  # eth (same as thorn in Elder Futhark)
            'a': 'ᚨ',  # ansuz - god, Odin
            'r': 'ᚱ',  # raidho - ride, journey
            'k': 'ᚲ',  # kenaz - torch
            'c': 'ᚲ',  # c as k sound
            'g': 'ᚷ',  # gebo - gift
            'w': 'ᚹ',  # wunjo - joy
            'v': 'ᚹ',  # v as w sound
            
            # Second Aett (Heimdall's Aett)
            'h': 'ᚺ',  # hagalaz - hail
            'n': 'ᚾ',  # nauthiz - need
            'i': 'ᛁ',  # isa - ice
            'j': 'ᛃ',  # jera - year, harvest
            'y': 'ᛇ',  # eihwaz - yew tree
            'ï': 'ᛇ',  # eihwaz variant
            'p': 'ᛈ',  # perthro - dice cup, fate
            'z': 'ᛉ',  # algiz - elk, protection
            's': 'ᛊ',  # sowilo - sun
            
            # Third Aett (Tyr's Aett)
            't': 'ᛏ',  # tiwaz - Tyr, justice
            'b': 'ᛒ',  # berkano - birch
            'e': 'ᛖ',  # ehwaz - horse
            'm': 'ᛗ',  # mannaz - man
            'l': 'ᛚ',  # laguz - water
            'ng': 'ᛜ', # ingwaz - Ing/Freyr
            'ŋ': 'ᛜ',  # ingwaz
            'd': 'ᛞ',  # dagaz - day
            'o': 'ᛟ',  # othala - heritage
            
            # Special combinations and alternatives
            'q': 'ᚲᚹ', # kw combination
            'x': 'ᚲᛊ', # ks combination
            'æ': 'ᚨ',  # using ansuz for ae
            'ø': 'ᛟ',  # using othala
            'ö': 'ᛟ',  # using othala
            
            # Punctuation/spacing
            ' ': ' ',   # preserve spaces
            '.': '᛬',   # single dot separator
            ',': '᛬',   # single dot separator
            ':': '᛭',   # double dot separator
        }
        
    def _init_younger_futhark(self):
        """
        Younger Futhark (Viking Age)
        Simplified to 16 runes, used 9th-11th century in Scandinavia
        """
        self.younger_futhark = {
            # The 16 runes of Younger Futhark
            'f': 'ᚠ',  # fé - wealth
            'u': 'ᚢ',  # úr - slag/drizzle
            'v': 'ᚢ',  # merged with u
            'w': 'ᚢ',  # merged with u
            'th': 'ᚦ', # thurs - giant
            'þ': 'ᚦ',
            'ð': 'ᚦ',
            'o': 'ᚬ',  # óss - god (replaces ansuz)
            'ą': 'ᚬ',  # merged with o
            'a': 'ᛅ',  # ár - year
            'æ': 'ᛅ',  # merged with a
            'r': 'ᚱ',  # reið - ride
            'k': 'ᚴ',  # kaun - ulcer
            'g': 'ᚴ',  # merged with k
            'c': 'ᚴ',  # merged with k
            'q': 'ᚴ',  # merged with k
            'h': 'ᚼ',  # hagall - hail
            'n': 'ᚾ',  # nauðr - need
            'i': 'ᛁ',  # ísa - ice
            'e': 'ᛁ',  # merged with i
            'j': 'ᛁ',  # merged with i
            'y': 'ᛁ',  # merged with i
            's': 'ᛋ',  # sól - sun
            'z': 'ᛋ',  # merged with s
            'x': 'ᚴᛋ', # ks combination
            't': 'ᛏ',  # Týr - the god Tyr
            'd': 'ᛏ',  # merged with t
            'b': 'ᛒ',  # bjarkan - birch
            'p': 'ᛒ',  # merged with b
            'm': 'ᛘ',  # maðr - man
            'l': 'ᛚ',  # lögr - water
            'ʀ': 'ᛦ',  # yr - yew bow (for final R)
            
            # Punctuation
            ' ': ' ',
            '.': '᛬',
            ',': '᛬',
            ':': '᛭',
        }
        
    def _init_short_twig(self):
        """
        Short-Twig/Rök Runes
        Swedish-Norwegian variant of Younger Futhark with simplified forms
        """
        self.short_twig = {
            'f': 'ᚠ',
            'u': 'ᚢ', 
            'v': 'ᚢ',
            'w': 'ᚢ',
            'th': 'ᚦ',
            'þ': 'ᚦ',
            'ð': 'ᚦ',
            'o': 'ᚭ',  # short-twig o
            'a': 'ᛆ',  # short-twig a
            'æ': 'ᛆ',
            'r': 'ᚱ',
            'k': 'ᚴ',
            'g': 'ᚴ',
            'c': 'ᚴ',
            'h': 'ᚽ',  # short-twig h
            'n': 'ᚿ',  # short-twig n
            'i': 'ᛁ',
            'e': 'ᛁ',
            'j': 'ᛁ',
            'y': 'ᛁ',
            's': 'ᛌ',  # short-twig s
            'z': 'ᛌ',
            't': 'ᛐ',  # short-twig t
            'd': 'ᛐ',
            'b': 'ᛓ',  # short-twig b
            'p': 'ᛓ',
            'm': 'ᛙ',  # short-twig m
            'l': 'ᛚ',
            'ʀ': 'ᛧ',  # short-twig yr
            
            ' ': ' ',
            '.': '᛬',
            ',': '᛬',
        }
        
    def _init_anglo_saxon(self):
        """
        Anglo-Saxon Futhorc
        Extended runic alphabet used in England, 28-33 runes, 5th-11th century
        """
        self.anglo_saxon = {
            # Core 28 runes
            'f': 'ᚠ',  # feoh - cattle
            'u': 'ᚢ',  # ur - aurochs
            'th': 'ᚦ', # thorn
            'þ': 'ᚦ',
            'ð': 'ᚦ',
            'o': 'ᚩ',  # os - god (replaces ansuz)
            'r': 'ᚱ',  # rad - ride
            'c': 'ᚳ',  # cen - torch
            'k': 'ᚳ',  # same as c
            'g': 'ᚷ',  # gyfu - gift
            'w': 'ᚹ',  # wynn - joy
            'h': 'ᚻ',  # hægl - hail
            'n': 'ᚾ',  # nyd - need
            'i': 'ᛁ',  # is - ice
            'j': 'ᛄ',  # ger - year
            'eo': 'ᛇ', # eoh - yew
            'p': 'ᛈ',  # peorð
            'x': 'ᛉ',  # eolhx - elk sedge
            's': 'ᛋ',  # sigel - sun
            't': 'ᛏ',  # tir - Tiw/Tyr
            'b': 'ᛒ',  # beorc - birch
            'e': 'ᛖ',  # eh - horse
            'm': 'ᛗ',  # mann - man
            'l': 'ᛚ',  # lagu - water/sea
            'ng': 'ᛝ', # ing - hero
            'ŋ': 'ᛝ',
            'd': 'ᛞ',  # dæg - day
            'œ': 'ᛟ',  # ethel - homeland
            
            # Additional Anglo-Saxon runes
            'a': 'ᚪ',  # ac - oak
            'æ': 'ᚫ',  # æsc - ash tree
            'y': 'ᚣ',  # yr - bow
            'ia': 'ᛡ', # ior - beaver
            'ea': 'ᛠ', # ear - grave/earth
            
            # Alternatives
            'q': 'ᚳᚹ', # cw combination
            'v': 'ᚠ',  # as f
            'z': 'ᛉ',  # as x
            
            # Punctuation
            ' ': ' ',
            '.': '᛬',
            ',': '᛬',
            ':': '᛭',
        }
        
    def _init_medieval(self):
        """
        Medieval/Latinized Futhark
        Post-Viking Age runic alphabet adapted for Latin, post-1100
        """
        self.medieval = {
            'a': 'ᛆ',
            'b': 'ᛒ',
            'c': 'ᛍ',
            'd': 'ᛑ',
            'th': 'ᚦ',
            'e': 'ᛂ',
            'f': 'ᚠ',
            'g': 'ᚵ',
            'h': 'ᛡ',
            'i': 'ᛁ',
            'j': 'ᛁ',
            'k': 'ᚴ',
            'l': 'ᛚ',
            'm': 'ᛉ',
            'n': 'ᚿ',
            'o': 'ᚮ',
            'p': 'ᛔ',
            'q': 'ᚴ',
            'r': 'ᚱ',
            's': 'ᛍ',
            't': 'ᛐ',
            'u': 'ᚢ',
            'v': 'ᚡ',
            'w': 'ᚡ',
            'x': 'ᛉ',
            'y': 'ᚤ',
            'z': 'ᛋ',
            'æ': 'ᛅ',
            'ø': 'ᚯ',
            'å': 'ᛆ',
            
            ' ': ' ',
            '.': '᛬',
            ',': '᛬',
        }
        
    def _init_staveless(self):
        """
        Staveless/Hälsinge Runes
        Simplified forms used in Hälsingland, Sweden
        """
        self.staveless = {
            # Basic simplified mappings
            'f': 'ᛙ',
            'u': '╮',
            'v': '╮',
            'w': '╮',
            'th': 'ו',
            'þ': 'ו',
            'o': 'ˎ',
            'r': '◟',
            'k': 'ᛍ',
            'g': 'ᛍ',
            'c': 'ᛍ',
            'h': 'ᚽ',
            'n': '⸜',
            'i': 'ᛁ',
            'e': 'ᛁ',
            'y': 'ᛁ',
            'j': 'ᛁ',
            'a': '⸝',
            'ʀ': '⡄',
            's': '╵',
            'z': '╵',
            't': '⸍',
            'd': '⸍',
            'b': 'ި',
            'p': 'ި',
            'm': '⠃',
            'l': '⸌',
            
            ' ': ' ',
            '.': '×',
        }
    
    def _preprocess_text(self, text: str, system: RuneSystem) -> str:
        """
        Preprocess text for runic conversion
        - Handle special letter combinations
        - Convert to lowercase
        - Apply system-specific transformations
        """
        text = text.lower()
        
        # Common preprocessing for all systems
        replacements = [
            ('qu', 'kw'),  # qu -> kw
            ('x', 'ks'),   # x -> ks
        ]
        
        # System-specific preprocessing
        if system in [RuneSystem.ELDER_FUTHARK, RuneSystem.YOUNGER_FUTHARK]:
            # Historical sound changes
            replacements.extend([
                ('ph', 'f'),   # Greek ph -> f
                ('ch', 'k'),   # Greek ch -> k (when hard)
                ('ck', 'k'),   # ck -> k
                ('ee', 'e'),   # double vowels
                ('oo', 'o'),
                ('ll', 'l'),   # double consonants simplified
                ('tt', 't'),
                ('ss', 's'),
                ('mm', 'm'),
                ('nn', 'n'),
            ])
            
        if system == RuneSystem.ANGLO_SAXON:
            # Anglo-Saxon specific digraphs
            replacements.extend([
                ('sh', 'sc'),  # sh sound
                ('ch', 'c'),   # ch sound  
            ])
        
        # Apply replacements
        for old, new in replacements:
            text = text.replace(old, new)
            
        return text
    
    def convert(self, text: str, system: RuneSystem) -> str:
        """
        Convert text to specified runic system
        
        Args:
            text: The text to convert
            system: The runic system to use
            
        Returns:
            Converted runic text
        """
        # Get the appropriate runic alphabet
        runic_map = {
            RuneSystem.ELDER_FUTHARK: self.elder_futhark,
            RuneSystem.YOUNGER_FUTHARK: self.younger_futhark,
            RuneSystem.SHORT_TWIG: self.short_twig,
            RuneSystem.ANGLO_SAXON: self.anglo_saxon,
            RuneSystem.MEDIEVAL: self.medieval,
            RuneSystem.STAVELESS: self.staveless,
        }
        
        runes = runic_map.get(system)
        if not runes:
            raise ValueError(f"Unknown runic system: {system}")
        
        # Preprocess the text
        processed = self._preprocess_text(text, system)
        
        # Convert to runes
        result = []
        i = 0
        while i < len(processed):
            # Try two-character combinations first
            if i < len(processed) - 1:
                two_char = processed[i:i+2]
                if two_char in runes:
                    result.append(runes[two_char])
                    i += 2
                    continue
            
            # Single character
            char = processed[i]
            if char in runes:
                result.append(runes[char])
            elif char.isdigit():
                # Keep numbers as-is
                result.append(char)
            elif char in '!?()[]{}@#$%^&*+=/<>\\|`~':
                # Keep special characters as-is
                result.append(char)
            else:
                # Unknown character - keep as-is with marker
                result.append(f'[{char}]')
            
            i += 1
        
        return ''.join(result)
    
    def convert_all_systems(self, text: str) -> Dict[str, str]:
        """Convert text to all available runic systems"""
        results = {}
        for system in RuneSystem:
            try:
                results[system.value] = self.convert(text, system)
            except Exception as e:
                results[system.value] = f"Error: {str(e)}"
        return results
    
    def transliterate_runes(self, runic_text: str) -> str:
        """
        Attempt to transliterate runic text back to Latin alphabet
        Note: This is approximate as many runes represent multiple sounds
        """
        # Create reverse mapping (rune -> letter)
        reverse_map = {}
        
        # Build from Elder Futhark as base
        for letter, rune in self.elder_futhark.items():
            if rune not in reverse_map and len(letter) == 1:
                reverse_map[rune] = letter
        
        # Transliterate
        result = []
        for char in runic_text:
            if char in reverse_map:
                result.append(reverse_map[char])
            elif char == ' ':
                result.append(' ')
            elif char in '᛬᛭':
                result.append('.')
            else:
                result.append(f'[{char}]')
        
        return ''.join(result)
