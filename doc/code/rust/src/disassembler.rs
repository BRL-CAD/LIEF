use lief::generic::Binary;

pub fn disassemble(some_elf: &lief::elf::Binary) {
    // lief-doc: disassemble-start
    let elf: &lief::elf::Binary = some_elf;

    for inst in elf.disassemble_address(0x400) {
        println!("{}", inst);
    }
    // lief-doc: disassemble-end
}

// lief-doc: downcast-start
pub fn check_opcode(some_inst: &lief::assembly::Instructions) {
    let inst: &lief::assembly::Instructions = some_inst;

    if let lief::assembly::Instructions::RiscV(riscv) = inst {
        println!("{:?}", riscv.opcode());
    }
}
// lief-doc: downcast-end

pub fn dsc_disassemble(some_dyld_cache: &lief::dsc::DyldSharedCache) {
    // lief-doc: dsc-disassemble-start
    let dyld_cache: &lief::dsc::DyldSharedCache = some_dyld_cache;

    for inst in dyld_cache.disassemble(0x1886f4a44) {
        println!("{}", inst);
    }
    // lief-doc: dsc-disassemble-end
}

pub fn dwarf_function() {
    // lief-doc: dwarf-func-start
    let elf = lief::elf::Binary::parse("/bin/ls").unwrap();
    if let Some(lief::DebugInfo::Dwarf(dwarf)) = elf.debug_info()
        && let Some(func) = dwarf.function_by_name("main")
    {
        for inst in func.instructions() {
            println!("{}", inst);
        }
    }
    // lief-doc: dwarf-func-end
}
