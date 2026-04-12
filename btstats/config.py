import os
from pathlib import Path

from tomlkit import document, table
from tomlkit.toml_file import TOMLFile

DEFAULT_PORT = 8125
DEFAULT_CONFIG_DIR = Path.home() / ".config" / "btstats"
DEFAULT_CONFIG_FILE = "config.toml"


def _default_doc():
    doc = document()
    bt = table()
    bt.add("address", "")
    bt.add("name", "")
    bt.add("characteristic_uuid", "")
    srv = table()
    srv.add("port", DEFAULT_PORT)
    doc.add("bluetooth", bt)
    doc.add("server", srv)
    return doc


def get_config_path(cli_path=None):
    if cli_path:
        return Path(cli_path)
    env_path = os.getenv("BTSTATS_CONFIG")
    if env_path:
        return Path(env_path)
    return DEFAULT_CONFIG_DIR / DEFAULT_CONFIG_FILE


def load_config(path):
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        doc = _default_doc()
        TOMLFile(path).write(doc)
        return doc
    return TOMLFile(path).read()


def save_config(doc, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    TOMLFile(path).write(doc)
