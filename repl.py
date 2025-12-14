from antlr4 import *
from datetime import date
from generated.WorkflowLexer import WorkflowLexer
from generated.WorkflowParser import WorkflowParser
from visitor import ExecVisitor

def run_dsl(text, visitor):
    lexer = WorkflowLexer(InputStream(text))
    parser = WorkflowParser(CommonTokenStream(lexer))
    tree = parser.program()
    visitor.visit(tree)

def wizard_add(visitor):
    print("\n=== TAMBAH BARANG ===")
    name = input("Nama barang : ")
    type_ = input("Tipe barang : ")

    dsl = f'add resource name="{name}" type="{type_}"'
    run_dsl(dsl, visitor)

def wizard_borrow(visitor):
    print("\n=== PEMINJAMAN ===")
    rid = input("ID barang        : ")
    borrower = input("Nama peminjam    : ")
    borrow_date = input("Tanggal pinjam   : ")

    dsl = (
        f'borrow {rid} '
        f'borrower="{borrower}" '
        f'borrow_date="{borrow_date}"'
    )
    run_dsl(dsl, visitor)

def wizard_return(visitor):
    print("\n=== PENGEMBALIAN ===")
    rid = input("ID barang        : ")
    return_date = input("Tanggal kembali  : ")

    dsl = (
        f'return {rid} '
        f'return_date="{return_date}"'
    )
    run_dsl(dsl, visitor)

def run_repl(state):
    visitor = ExecVisitor(state)

    print("=== SISTEM WORKFLOW PEMINJAMAN ===")
    print("Perintah: add | borrow | return | query | exit\n")

    while True:
        cmd = input(">> ").strip().lower()

        if cmd == "exit":
            break
        elif cmd == "add":
            wizard_add(visitor)
        elif cmd == "borrow":
            wizard_borrow(visitor)
        elif cmd == "return":
            wizard_return(visitor)
        elif cmd == "query":
            run_dsl("query", visitor)
        else:
            print("Perintah tidak dikenal")
