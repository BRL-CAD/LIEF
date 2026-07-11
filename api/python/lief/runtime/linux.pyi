import os
from typing import (
    Any,
    ClassVar,
    Final,
    Iterator,
    Optional,
    Union,
    overload
)

import lief.ELF
import lief.runtime


class Module(lief.runtime.Module):
    @property
    def handle(self) -> Any: ...

    def dlsym(self, name: str) -> Any: ...

    @staticmethod
    def from_handle(handle: Any) -> Optional[Module]: ...

    @overload
    def parse_from_path(self) -> Optional[lief.ELF.Binary]: ...

    @overload
    def parse_from_path(self, config: lief.ELF.ParserConfig) -> Optional[lief.ELF.Binary]: ...

    @overload
    def parse_from_memory(self) -> Optional[lief.ELF.Binary]: ...

    @overload
    def parse_from_memory(self, config: lief.ELF.ParserConfig) -> Optional[lief.ELF.Binary]: ...

def dlopen(name: Union[str, os.PathLike]) -> Optional[Module]: ...

class Host:
    sys_name: ClassVar[Final[str]] = ...

    sys_release: ClassVar[Final[str]] = ...

    sys_version: ClassVar[Final[str]] = ...

    hardware: ClassVar[Final[str]] = ...

class Process(lief.runtime.Process):
    cmdline: ClassVar[Final[str]] = ...

    glibc_version: ClassVar[Final[str]] = ...
