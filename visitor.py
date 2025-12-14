from generated.WorkflowVisitor import WorkflowVisitor

class ExecVisitor(WorkflowVisitor):
    def __init__(self, state):
        self.state = state

    def visitProgram(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    # =========================
    # ADD RESOURCE
    # =========================
    def visitAddStmt(self, ctx):
        rid = self.state.new_id()
        self.state.resources[rid] = {
            "name": None,
            "type": None,
            "status": "available",
            "borrower": None,
            "borrow_date": None,
            "return_date": None
        }

        for f in ctx.fieldList().fieldAssign():
            key = f.ID().getText()
            val = f.value().getText().strip('"')
            self.state.resources[rid][key] = val

        print(f"\n[ADD RESOURCE]")
        print(f"ID Barang   : {rid}")
        print(f"Nama Barang : {self.state.resources[rid]['name']}")
        print(f"Tipe Barang : {self.state.resources[rid]['type']}")

    # =========================
    # BORROW
    # =========================
    def visitBorrowStmt(self, ctx):
        rid = ctx.ID().getText()

        if rid not in self.state.resources:
            print("[ERROR] Barang tidak ditemukan")
            return

        item = self.state.resources[rid]

        if item["status"] == "borrowed":
            print("[ERROR] Barang sedang dipinjam")
            return

        for f in ctx.fieldList().fieldAssign():
            item[f.ID().getText()] = f.value().getText().strip('"')

        item["status"] = "borrowed"

        print(f"\n[BORROW]")
        print(f"ID Barang   : {rid}")
        print(f"Peminjam    : {item['borrower']}")
        print(f"Tgl Pinjam  : {item['borrow_date']}")

    # =========================
    # RETURN
    # =========================
    def visitReturnStmt(self, ctx):
        rid = ctx.ID().getText()

        if rid not in self.state.resources:
            print("[ERROR] Barang tidak ditemukan")
            return

        item = self.state.resources[rid]

        if item["status"] != "borrowed":
            print("[ERROR] Barang tidak sedang dipinjam")
            return

        for f in ctx.fieldList().fieldAssign():
            item[f.ID().getText()] = f.value().getText().strip('"')

        item["status"] = "available"
        item["borrower"] = None

        print(f"\n[RETURN]")
        print(f"ID Barang    : {rid}")
        print(f"Tgl Kembali  : {item['return_date']}")

    # =========================
    # QUERY 
    # =========================
    def visitQueryStmt(self, ctx):
        print("\n=== DATA PEMINJAMAN ===")

        if not self.state.resources:
            print("(Belum ada data)")
            return

        for rid, d in self.state.resources.items():
            print(f"\nID Barang : {rid}")
            print(f"  Nama Barang : {d['name']}")
            print(f"  Tipe Barang : {d['type']}")
            print(f"  Status      : {d['status']}")
            print(f"  Peminjam    : {d['borrower'] or '-'}")
            print(f"  Tgl Pinjam  : {d['borrow_date'] or '-'}")
            print(f"  Tgl Kembali : {d['return_date'] or '-'}")
