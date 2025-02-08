__url__ = "https://github.com/RuanMiguel-DRD/NoMedia"
__description__ = "Script to hide and unhide media from the cell phone gallery"

__license__ = "Unlicense"
__version__ = "0.1.0"


__author__ = "RuanMiguel-DRD"
__maintainer__ = __author__
__credits__ = __author__

__email__ = "ruanmigueldrd@outlook.com"


__keywords__ = [
    "android", "termux", "media"
]


__all__ = [
    "check_directory", "media_control"
]

from .__main__ import check_directory
from .__main__ import media_control
