"""CLI constants."""
import sys


CLI_MODULES = [
    'model',
    'pipeline',
    'credential',
    'catalog',
    'datastore',
    'run',
    'new',
    'starter',
]

CLI_MODULES_HELP = {
    'credential': 'Credentials YML management.',
    'datastore': 'Storage pointers management.',
    'model': 'Model deploy and registration management.',
}

ENTRY_POINTS = {
    'CLI': 'projetaai.cli',
    'CI': 'projetaai.starters.ci',
}

PYTHON_VERSION = (f'{sys.version_info.major}.{sys.version_info.minor}.'
                  f'{sys.version_info.micro}')
