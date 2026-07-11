import subprocess
import sys
from pathlib import Path

import lief
import pytest
from utils import address_space_limiter, get_sample, parse_elf


def test_symbols():
    target = parse_elf("ELF/ELF32_x86_library_libshellx.so")
    symbols = [
        sym
        for idx, sym in enumerate(target.dynamic_symbols)
        if idx == 0 or len(sym.name) > 0
    ]
    assert len(symbols) == 48

    assert symbols[2].name == "__cxa_atexit"


def test_relocations():
    target = parse_elf("ELF/ELF32_x86_library_libshellx.so")
    relocations = target.relocations
    assert len(relocations) == 47

    assert relocations[10].symbol is not None
    assert relocations[10].symbol.name == "strlen"


@pytest.mark.linux
@pytest.mark.private
def test_section_overflow():
    sample = Path(get_sample("private/ELF/section_overflow.elf")).absolute()

    subprocess.check_call(
        [sys.executable, "-c", f'import lief; lief.parse(r"{sample}")'],
        timeout=60.0,
        preexec_fn=address_space_limiter(),
    )


@pytest.mark.private
def test_dynamic_entries_capped():
    sample = get_sample("private/ELF/dynamic_no_null.elf")
    elf = lief.ELF.parse(sample)
    assert elf is not None
    assert len(elf.dynamic_entries) == 1000
