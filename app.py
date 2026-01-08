import pygame, graphics


class Manager:
    def __init__(self, master):
        self.master = master
        self.inputs = {}
        self.frames = {"Dummy": graphics.Frame(self.master), "MENU" : graphics.Menu(self.master)}
        del(self.frames["Dummy"])
        self.dim = master.get_width(), master.get_height()
        self.layers = ["MENU"]

    def check_input(self, input_type):
        return input_type in self.inputs and self.inputs[input_type]

    def is_running(self):
        return not self.check_input(pygame.QUIT)

    def set_inputs(self, inputs):
        for event_type in self.inputs.keys():
            self.inputs[event_type] = False
        for event in inputs:
            self.inputs[event.type] = True

    def handle(self):
        t = {}
        for k in self.frames.keys():
            t[k] = [frame.name for frame in self.frames[k].get_touched(*pygame.mouse.get_pos())]
        if self.check_input(pygame.MOUSEBUTTONDOWN):
            x = pygame.mouse.get_pressed()
            if x[0]:
                if "file_b" in t["MENU"]:
                    self.frames["CONTEXT"] = graphics.ContextFrame(self.master, ["New", "Open", "Save"], (1, 22, 50, 20))
                    if "CONTEXT" not in self.layers:
                        self.layers.append("CONTEXT")
                elif "edit_b" in t["MENU"]:
                    self.frames["CONTEXT"] = graphics.ContextFrame(self.master, ["New", "Open", "Save"], (37, 22, 50, 20))
                    if "CONTEXT" not in self.layers:
                        self.layers.append("CONTEXT")
                else:
                    del(self.frames["CONTEXT"])
                    print(t["CONTEXT"])

    def update(self):
        self.layers = [layer for layer in self.layers if layer in self.frames.keys()]
        if self.dim[0] != self.master.get_width() or self.dim[1] != self.master.get_height():
            for frame in self.frames.values():
                frame.__init__(self.master)
            self.dim = self.master.get_width(), self.master.get_height()
        self.frames["MENU"].log_t.set_label(text = f"{self.master.get_width()}, {self.master.get_height()}")
        for frame_name in self.layers:
            self.frames[frame_name].update()