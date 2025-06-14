import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img1, True, False)
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True , False)
    tmr = 0
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    move = [0,0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img1, [-tmr, 0])
        screen.blit(bg_img_flip, [-tmr+1600, 0])
        screen.blit(bg_img2, [-tmr+3200, 0])
        screen.blit(kk_img,kk_rct)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move = [-1,-1]
        elif key_lst[pg.K_DOWN]:
            move = [-1,1]
        elif key_lst[pg.K_RIGHT]:
            move = [1,0]
        elif key_lst[pg.K_LEFT]:
            move = [-2,0]
        else:
            move = [-1,0]
        
        kk_rct.move_ip((move))

        if tmr > 3199:
            tmr = 0
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()