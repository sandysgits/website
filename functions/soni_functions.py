# Funktion zur Bestimmung der Jahreszeit basierend auf dem Datum
def get_season(date_str):
    month = int(date_str[4:6])  # Extrahiere den Monat
    if 3 <= month <= 5:
        return 'spring'  # Frühling (E-Dur)
    elif 6 <= month <= 8:
        return 'summer'  # Sommer (g-moll)
    elif 9 <= month <= 11:
        return 'autumn'  # Herbst (F-Dur)
    else:
        return 'winter'  # Winter (f-moll)
 
# Bestimme die Tonart basierend auf der Jahreszeit
def get_scale(season):
    scales = {
        'spring': 'E major',
        'summer': 'G minor',
        'autumn': 'F major',
        'winter': 'F minor'
    }
    return scales[season]

# Gebe Töne der Tonart aus:
def get_notes(scale):
    notes = {
        'E major': ['E1','E2','G#2',
                    'E3', 'F#3','G#3','B3', 'C#4',
                    'E4', 'F#4','G#4','B4', 'C#5',
                    'E5', 'F#5','G#5','B5', 'C#6',
                    'E6', 'F#6','G#6','B6', 'C#7'],
        'G minor': ['G1','G2','C3',
                    'G3', 'A#3','C4','D4', 'F4',
                    'G4', 'A#4','C5','D5', 'F5',
                    'G5', 'A#5','C6','D6', 'F6',
                    'G6', 'A#6','C7','D7', 'F7'],
        'F major': ['F1','F2','A2',
                    'F3', 'G3','A3','C4', 'D4',
                    'F4', 'G4','A4','C5', 'D5',
                    'F5', 'G5','A5','C6', 'D6',
                    'F6', 'G6','A6','C7', 'D7',],
        'F minor': ['F1','F2','A#2',
                    'F3', 'G#3','A#3','C4', 'D#4',
                    'F4', 'G#4','A#4','C5', 'D#5',
                    'F5', 'G#5','A#5','C6', 'D#6',
                    'F6', 'G#6','A#6','C7', 'D#7',]
    }
    return notes[scale]


# function maps value (which is inbetween min_value and max_value) into new range from min_result to max_result
def map_value(value,min_value,max_value,min_result,max_result):
    '''maps value (or array of values) from one range to another'''
    result = min_result + (value - min_value)/(max_value-min_value)*(max_result - min_result)
    return result


def get_midi_instrument_number(instrument_name):
    # Dictionary mapping instrument names to MIDI numbers (General MIDI)
    INSTRUMENTS = {
        "acoustic grand piano": 0,
        "bright acoustic piano": 1,
        "electric grand piano": 2,
        "honky-tonk piano": 3,
        "electric piano 1": 4,
        "electric piano 2": 5,
        "harpsichord": 6,
        "clavinet": 7,
        "celesta": 8,
        "glockenspiel": 9,
        "music box": 10,
        "vibraphone": 11,
        "marimba": 12,
        "xylophone": 13,
        "tubular bells": 14,
        "dulcimer": 15,
        "drawbar organ": 16,
        "percussive organ": 17,
        "rock organ": 18,
        "church organ": 19,
        "reed organ": 20,
        "accordion": 21,
        "harmonica": 22,
        "tango accordion": 23,
        "acoustic guitar (nylon)": 24,
        "acoustic guitar (steel)": 25,
        "electric guitar (jazz)": 26,
        "electric guitar (clean)": 27,
        "electric guitar (muted)": 28,
        "overdriven guitar": 29,
        "distortion guitar": 30,
        "guitar harmonics": 31,
        "acoustic bass": 32,
        "electric bass (finger)": 33,
        "electric bass (pick)": 34,
        "fretless bass": 35,
        "slap bass 1": 36,
        "slap bass 2": 37,
        "synth bass 1": 38,
        "synth bass 2": 39,
        "violin": 40,
        "viola": 41,
        "cello": 42,
        "contrabass": 43,
        "tremolo strings": 44,
        "pizzicato strings": 45,
        "orchestral harp": 46,
        "timpani": 47,
        "string ensemble 1": 48,
        "string ensemble 2": 49,
        "synth strings 1": 50,
        "synth strings 2": 51,
        "choir aahs": 52,
        "voice oohs": 53,
        "synth choir": 54,
        "orchestra hit": 55,
        "trumpet": 56,
        "trombone": 57,
        "tuba": 58,
        "muted trumpet": 59,
        "french horn": 60,
        "brass section": 61,
        "synth brass 1": 62,
        "synth brass 2": 63,
        "soprano sax": 64,
        "alto sax": 65,
        "tenor sax": 66,
        "baritone sax": 67,
        "oboe": 68,
        "english horn": 69,
        "bassoon": 70,
        "clarinet": 71,
        "piccolo": 72,
        "flute": 73,
        "recorder": 74,
        "pan flute": 75,
        "blown bottle": 76,
        "shakuhachi": 77,
        "whistle": 78,
        "ocarina": 79,
        "lead 1 (square)": 80,
        "lead 2 (sawtooth)": 81,
        "lead 3 (calliope)": 82,
        "lead 4 (chiff)": 83,
        "lead 5 (charang)": 84,
        "lead 6 (voice)": 85,
        "lead 7 (fifths)": 86,
        "lead 8 (bass + lead)": 87,
        "pad 1 (new age)": 88,
        "pad 2 (warm)": 89,
        "pad 3 (polysynth)": 90,
        "pad 4 (choir)": 91,
        "pad 5 (bowed)": 92,
        "pad 6 (metallic)": 93,
        "pad 7 (halo)": 94,
        "pad 8 (sweep)": 95,
        "fx 1 (rain)": 96,
        "fx 2 (soundtrack)": 97,
        "fx 3 (crystal)": 98,
        "fx 4 (atmosphere)": 99,
        "fx 5 (brightness)": 100,
        "fx 6 (goblins)": 101,
        "fx 7 (echoes)": 102,
        "fx 8 (sci-fi)": 103,
        "sitar": 104,
        "banjo": 105,
        "shamisen": 106,
        "koto": 107,
        "kalimba": 108,
        "bagpipe": 109,
        "fiddle": 110,
        "shanai": 111,
        "tinkle bell": 112,
        "agogo": 113,
        "steel drums": 114,
        "woodblock": 115,
        "taiko drum": 116,
        "melodic tom": 117,
        "synth drum": 118,
        "reverse cymbal": 119,
        "guitar fret noise": 120,
        "breath noise": 121,
        "seashore": 122,
        "bird tweet": 123,
        "telephone ring": 124,
        "helicopter": 125,
        "applause": 126,
        "gunshot": 127
    }
    instrument_name = instrument_name.lower()
    if instrument_name in INSTRUMENTS:
        return INSTRUMENTS[instrument_name]
    else:
        print(f"Error: '{instrument_name}' is not a valid instrument name.")
        sys.exit(1)