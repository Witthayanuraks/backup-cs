import pyxel
import random

class CatchTheStars:
    def __init__(self):
        pyxel.init(160, 120, title="Catch the Stars")
        self.player_x = 70
        self.score = 0
        self.stars = []
        self.speed = 2
        pyxel.run(self.update, self.draw)

    def update(self):
        # Gerakan pemain
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 3, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 3, 152)
        
        # Tambahkan bintang
        if pyxel.frame_count % 30 == 0:
            self.stars.append([random.randint(0, 150), 0])
        
        # Perbarui posisi bintang
        for star in self.stars[:]:
            star[1] += self.speed
            if star[1] > 120:
                self.stars.remove(star)
            elif abs(star[0] - self.player_x) < 8 and star[1] > 100:
                self.stars.remove(star)
                self.score += 1
                
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player_x, 110, 8, 8, 9)  # Gambar pemain
        for star in self.stars:
            pyxel.circ(star[0], star[1], 2, 10)  # Gambar bintang
        pyxel.text(5, 5, f"Score: {self.score}", 7)

if __name__ == "__main__":
    CatchTheStars()
