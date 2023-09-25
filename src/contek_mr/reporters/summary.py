from typing import IO
from typing import Iterable
from typing import Optional

from rich import print as rprint

from contek_mr import AllocationRecord
from contek_mr.reporters.tui import TUI


class SummaryReporter:
    N_COLUMNS = len(TUI.KEY_TO_COLUMN_NAME)

    def __init__(self, data: Iterable[AllocationRecord], native: bool):
        super().__init__()
        self.data = data
        self._tui = TUI(pid=None, cmd_line=None, native=native)
        self._tui.update_snapshot(tuple(data))

    @classmethod
    def from_snapshot(
        cls, allocations: Iterable[AllocationRecord], native: bool = False
    ) -> "SummaryReporter":
        return cls(allocations, native=native)

    def render(
        self,
        sort_column: int,
        *,
        max_rows: Optional[int] = None,
        file: Optional[IO[str]] = None,
    ) -> None:
        self._tui.update_sort_key(sort_column)
        rprint(self._tui.get_body(max_rows=max_rows), file=file)
