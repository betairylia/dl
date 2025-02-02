import adv_test
import adv

def module():
    return Louise

class Louise(adv.Adv):
    a1 = ('od',0.13)

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100


    def s1_proc(this, e):
        this.afflics.poison('s1', 120, 0.582)


    def s2_proc(this, e):
        coef = (4.035-2.69)*3 * this.afflics.poison.get()
        this.dmg_make("o_s2_boost", coef)


if __name__ == '__main__':
    module().comment = 'no fs'
    conf = {}
    from slot.d import *
    conf['slot.d'] = Pazuzu()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
