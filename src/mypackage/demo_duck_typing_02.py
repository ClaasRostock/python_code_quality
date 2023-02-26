import os
from pathlib import Path

from demo_duck_typing import print_name

print_name(os)

print_name(Path.cwd())

print_name(1.23)
