import bge
from math import radians
from datetime import datetime
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
hora = obj['ponteiro_horas']
minuto = obj['ponteiro_minutos']
segundo = obj['ponteiro_segundos']
class relogioApp():
    def tick(self):
        now = datetime.now()
        sec = now.second
        hor = now.hour
        min = now.minute
        micro = now.microsecond
        hrot = minuto.localOrientation.to_euler()
        hrot.z = -radians(hor*30 + min/2 + sec/120)
        hora.localOrientation = hrot
        mrot = minuto.localOrientation.to_euler()
        mrot.z = -radians(min*6 + sec*0.1)
        minuto.localOrientation = mrot        
        srot = segundo.localOrientation.to_euler()
        srot.z = -radians(sec*6 + micro*6*10**(-6))
        segundo.localOrientation = srot                    
def tempo():
    r = relogioApp()
    r.tick()