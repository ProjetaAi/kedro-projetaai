from pathlib import PurePosixPath, Path

CWD = PurePosixPath(Path.cwd().as_posix())
REQUIREMENTS_PATH = CWD / "src" / "requirements.txt"
