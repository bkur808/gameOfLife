from dataclasses import dataclass
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib
    #if using python pre-v3.11 need to use pip install tomli in cli

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"
#global constant for pre-loaded patterns path, used later in get_pattern

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]] 

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )
    
    
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])
    
def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]
    