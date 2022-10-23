from typing import Dict
from kedro_projetaai.packing.environment import Environment
from kedro_projetaai.packing.compiler import Compiler
from kedro_projetaai.packing.naming import get_experiment_name, get_pipeline_name
from kedro.framework.project import PACKAGE_NAME
from kedro.pipeline import Pipeline


class Packager:
    DEFAULT_PIPELINE = "__default__"

    def __init__(
        self,
        pipeline: str = None,
        experiment: str = None,
        tags: Dict[str, str] = None,
        branch: str = None,
    ):
        self._tags = tags or {}
        self._pipeline = pipeline
        self._experiment = experiment
        self._branch = branch

    @property
    def pipeline(self) -> str:
        return self._pipeline or self.DEFAULT_PIPELINE

    @property
    def project(self) -> str:
        if PACKAGE_NAME:
            return PACKAGE_NAME
        raise RuntimeError("Tried to run outside of a Kedro project")

    @property
    def experiment(self) -> str:
        return get_experiment_name(self.project, self._experiment, self._branch)

    @property
    def name(self) -> str:
        return get_pipeline_name(self.project, self.pipeline, self.experiment)

    @property
    def tags(self) -> Dict[str, str]:
        tags = {
            **self._tags,
            "pipeline": self.pipeline,
        }
        if self.experiment:
            tags["experiment"] = self.experiment
        return tags

    @property
    def environment(self) -> Environment:
        return Environment(self.name)

    @property
    def compiler(self) -> Compiler:
        return Compiler(self.pipeline)
