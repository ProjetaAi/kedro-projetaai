from typing import List, Tuple
from kedro.pipeline import Pipeline
from kedro.pipeline.node import Node
from kedro.framework.project import pipelines


# TODO: add prune option
class Compiler:
    def __init__(
        self,
        plugin: str,
        pipeline: str,
    ):
        self._pipeline_name = pipeline
        self._plugin = plugin

    @property
    def pipeline(self) -> Pipeline:
        return pipelines[self._pipeline_name]

    def command(self, node: Node) -> Tuple[str, ...]:
        return ("projetaai", "run", "--plugin", self._plugin, "--pipeline", self._pipeline_name, "--node", node.name)

    @property
    def commands(self) -> List[Tuple[str, ...]]:
        return [self.command(node) for node in self.pipeline.nodes]
