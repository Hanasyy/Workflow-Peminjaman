from state import WorkflowState
from repl import run_repl

if __name__ == "__main__":
    state = WorkflowState()
    run_repl(state)

    print("\n=== FINAL DATA ===")
    for rid, data in state.resources.items():
        print(f"\nID Barang : {rid}")
        print(f"  Nama          : {data.get('name')}")
        print(f"  Tipe          : {data.get('type')}")
        print(f"  Status        : {data.get('status')}")
        print(f"  Peminjam      : {data.get('borrower')}")
        print(f"  Tgl Pinjam    : {data.get('borrow_date')}")
        print(f"  Tgl Kembali   : {data.get('return_date')}")

