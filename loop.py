import pygame, app

class Loop:
    def __init__(self, dim = None):
        pygame.init()
        if dim is None:
            dim = pygame.display.get_desktop_sizes()[0]
        self.win = pygame.display.set_mode(dim, pygame.RESIZABLE)
        self.win.get_height()
        self.clock = pygame.time.Clock()
        self.manager = app.Manager(self.win)
    def run(self, tick_rate = 60):
        running = True
        while running:
            self.win.fill("black")

            self.manager.set_inputs(pygame.event.get())

            running = self.manager.is_running()
            self.manager.handle()

            self.manager.update()
            pygame.display.flip()

            self.clock.tick(tick_rate)

        pygame.quit()



