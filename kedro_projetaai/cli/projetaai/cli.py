import click

from kedro_projetaai.utils.plugins import get_plugins


@click.group()
def projetaai():
    """ProjetaAi CLI for production context."""


def _import_plugins() -> Dict[str, ProjetaAiCLIPlugin]:
    # Imports CLI plugins and sorts them into dict keys <plugin_name> : <plugin_cli>
    get_plugins(ENTRY_POINTS["run"])
