from typing import List, Dict, Any

from allenact.base_abstractions.experiment_config import ExperimentConfig

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Callback:
    def setup(
        self,
        name: str,
        config: ExperimentConfig,
        mode: Literal["train", "valid", "test"],
        **kwargs,
    ) -> None:
        """Called once before training begins."""

    def on_train_log(
        self,
        metrics: List[Dict[str, Any]],
        metric_means: Dict[str, float],
        step: int,
        tasks_data: List[Any],
        **kwargs,
    ) -> None:
        """Called once train is supposed to log."""

    def on_valid_log(
        self,
        metrics: Dict[str, Any],
        metric_means: Dict[str, float],
        checkpoint_file_name: str,
        tasks_data: List[Any],
        step: int,
        **kwargs,
    ) -> None:
        """Called after validation ends."""

    def on_test_log(
        self,
        checkpoint_file_name: str,
        metrics: Dict[str, Any],
        metric_means: Dict[str, float],
        tasks_data: List[Any],
        step: int,
        **kwargs,
    ) -> None:
        """Called after test ends."""

    def after_save_project_state(self, base_dir: str) -> None:
        """Called after saving the project state in base_dir."""
