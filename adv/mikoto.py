import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Mikoto

class Mikoto(Adv):
    a1 = ('cc',0.10,'hp70')
    a3 = ('cc',0.08)
    conf = {}

    def d_slots(this):
        if 'wand' in this.ex:
            this.conf['slots.d'] = slot.d.Sakuya()
            this.conf['slots.a'] = RR()+CE()
        else:
            this.conf['slots.d'] = slot.d.Sakuya()
            this.conf['slots.a'] = RR()+CE()
            #this.conf['slots.d'] = slot.d.Arctos()
            #this.conf['slots.a'] = RR()+LC()
        return


    def init(this):
        if this.condition('connect s1'):
            this.s1_proc = this.c_s1_proc

    def prerun(this):
        this.s1buff = Selfbuff("s1",0.0, 20)
        this.s2buff = Spdbuff("s2",0.2, 10)
        this.conf.s1.recovery = 1.4

    def s1latency(this, e):
        this.s1buff.off()
        this.s1buff.on()

    def s1_proc(this, e):
        this.s1buff.off()
        this.dmg_make('s1',5.32*2)
        this.s1buff.set(0.10).on()
        Timer(this.s1latency).on(1.5/this.speed())

    def c_s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 0:
            stance = 0
        elif buff == 0.10:
            stance = 1
        elif buff == 0.15:
            stance = 2
        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(0.10,20) #.on()
            this.conf.s1.recovery = 1.4
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(0.15,15) #.on()
            this.conf.s1.recovery = 1.63
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.s1buff.off().set(0)
            this.conf.s1.recovery = 3.07

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, x=5
        `s2, x=5
        `s3, x=5
        """


    #from module import ra
    #ra.test(module(), conf)
    #exit()

    adv_test.test(module(), conf, verbose=0, mass=0)

