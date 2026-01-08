import pygame

class Widget(pygame.sprite.Sprite):
    def __init__(self, name, image, rect):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = rect
    def is_touched(self, x, y):
        return 0 <= x - self.rect[0] <= self.rect[2] and 0 <= y - self.rect[1] <= self.rect[3]


class Label(Widget):
    def __init__(self, font, text, color, rect):
        self.font = font
        self.text = text
        self.color = color
        label = font.render(text, False, color)
        super().__init__(text, label, rect)
    def is_touched(self, x, y):
        return False
    def set_label(self, font = None, text = None, color = None):
        if font is not None:
            self.font = font
        if text is not None:
            self.text = text
        if color is not None:
            self.color = color
        self.update_image()
    def update_image(self):
        self.image = self.font.render(self.text, False, self.color)


class Frame:
    def __init__(self, master):
        self.image = pygame.sprite.Group()
        self.rect = 0, 0, 0, 0
        self.master = master
    def get_touched(self, x, y):
        touched = []
        end = len(self.image)
        widgets = iter(self.image)
        for _ in range(end):
            widget = next(widgets)
            if widget.is_touched(x, y):
                touched.append(widget)
        return touched
    def update(self):
        self.image.draw(self.master)


class Menu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.font = pygame.font.SysFont("JetbrainMono", 25)
        # file button
        self.file_b = Widget("file_b", pygame.Surface((35, 20)), (1, 1, 35, 20))
        self.file_b.image.fill("white")
        self.file_b.add(self.image)
        self.file_l = Label(self.font, "File", (0, 0, 0), (3, 3, 1, 1))
        self.file_l.add(self.image)
        # edit button
        self.edit_b = Widget("edit_b", pygame.Surface((40, 20)), (37, 1, 40, 20))
        self.edit_b.image.fill("white")
        self.edit_b.add(self.image)
        self.edit_l = Label(self.font, "Edit", (0, 0, 0), (40, 3, 1, 1))
        self.edit_l.add(self.image)
        # filler
        filler_width = self.master.get_width()-79
        if filler_width > 0:
            self.filler = Widget("filler", pygame.Surface((filler_width, 20)), (78, 1, filler_width, 20))
            self.filler.image.fill("white")
            self.filler.add(self.image)
        # log line
        if self.master.get_width() > 3 and self.master.get_height() > 20:
            self.log_l = Widget("log_l", pygame.Surface((self.master.get_width(), 20)), (1, self.master.get_height() - 21, self.master.get_width(), 20))
            self.log_l.image.fill("white")
            self.log_l.add(self.image)
            self.log_t = Label(self.font, "_", (0, 0, 0), (3, self.master.get_height() - 19, 1, 1))
            self.log_t.add(self.image)


class ContextFrame(Frame):
    def __init__(self, master, buttons, rect):
        super().__init__(master)
        self.rect = rect
        self.font = pygame.font.SysFont("JetbrainMono", 25)
        self.create_buttons(buttons)

    def create_buttons(self, names):
        i = 0
        for name in names:
            button = Widget(name, pygame.Surface((self.rect[2], self.rect[3])), (self.rect[0], self.rect[1] + i, self.rect[2], self.rect[3]))
            button.image.fill("white")
            button.add(self.image)
            label = Label(self.font, name, (0, 0, 0), (self.rect[0] + 2, self.rect[1] + i + 2, 1, 1))
            label.add(self.image)
            i += self.rect[3]
