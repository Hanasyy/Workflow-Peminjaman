class WorkflowState:
    def __init__(self):
        self.resources = {}
        self.counter = 1

    def new_id(self):
        rid = f"R{self.counter:03}"
        self.counter += 1
        return rid
