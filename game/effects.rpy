init python:
    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None, False)
        #if srf.get_width != 1280: srf = renpy.display.scale.smoothscale(srf, (1280, 720))
        return srf

    def invert():
        srf = screenshot_srf()
        inv = renpy.Render(srf.get_width(), srf.get_height()).canvas().get_surface()
        inv.fill((255,255,255,255))
        inv.blit(srf, (0,0), None, 2)
        return inv

    class Invert(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(Invert, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = self.width * 9 / 16
            self.srf = invert()
            self.delay = delay

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
              render.blit(self.srf, (0, 0))
            return render

    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled
        

init python:
    import math
    import random
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 3):
            self.sm = SpriteManager(update=self.update)
            # A list of (sprite, starting-x, speed).
            self.stars = [ ]
            self.displayable = theDisplayable
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 3
            self.timePassed = 0

            for i in range(self.numParticles):
                self.add(self.displayable, 1)
           
        def add(self, d, speed):
            s = self.sm.create(d)
            ySpeed = (random.random() - 0.5) * self.particleYSpeed
            xSpeed = (random.random() - 0.5) * self.particleXSpeed
            s.x += xSpeed * 40
            s.y += ySpeed * 40
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))
            
        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x += xSpeed
                    s.y += (ySpeed + (self.gravity * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0