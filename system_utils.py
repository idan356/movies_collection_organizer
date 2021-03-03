from pathvalidate import sanitize_filepath
from pathlib import Path
import subprocess


class SystemUtils(object):

    @classmethod
    def run_command(cls, command: str) -> str:
        """Run command and return in output stream content"""
        output: str = subprocess.check_output(command, shell=True)
        return output

    @classmethod
    def sanitize_filepath(cls, path: Path) -> Path:
        """Remove invalid characters from a given path object"""
        return sanitize_filepath(path, platform="auto")
