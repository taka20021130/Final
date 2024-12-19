import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        self.ballx=[0]
        self.bally=[0]
        self.angle=[pyxel.rndi(30,150)]
        self.vx=[pyxel.cos(self.angle[len(self.ballx)-1])]
        self.vy=[pyxel.sin(self.angle[len(self.ballx)-1])]
        self.speed=[1]
        self.count=0
        self.miss=0
        self.tencount=0
        pyxel.run(self.update,self.draw)

    def update(self):
        self.padx=pyxel.mouse_x
        self.StrCount=str(self.count+self.tencount*10)
        self.StrMiss=str(self.miss)
        if self.miss>=10:
            return
        for i in range(0,len(self.ballx)):
            self.ballx[i]+=self.vx[i]*self.speed[i]
            self.bally[i]+=self.vy[i]*self.speed[i]
            if self.bally[i]>200:
                self.angle[i]=pyxel.rndi(30,150)
                self.ballx[i]=pyxel.rndi(0,199)
                self.bally[i]=0
                self.speed[i]+=0.3
                self.vx[i]=pyxel.cos(self.angle[i])
                self.vy[i]=pyxel.sin(self.angle[i])
                self.miss+=1
            if (self.ballx[i]<0)or(self.ballx[i]>200):
                self.vx[i]=self.vx[i]*(-1)
            if self.padx-20<=self.ballx[i]<=self.padx+20 and 195<=self.bally[i]<=200:
                self.angle[i]=pyxel.rndi(30,150)
                self.ballx[i]=pyxel.rndi(0,199)
                self.bally[i]=0
                self.count+=1
                self.speed[i]+=0.3
                self.vx[i]=pyxel.cos(self.angle[i])
                self.vy[i]=pyxel.sin(self.angle[i])
            if self.count%10==0 and self.count>0:
                self.count=0
                self.tencount+=1
                for j in range(0,len(self.ballx)):
                    self.speed[j]=1
                self.ballx.append(pyxel.rndi(0,199))
                self.bally.append(0)
                self.angle.append(pyxel.rndi(30,150))
                self.vx.append(pyxel.cos(self.angle[len(self.ballx)-1]))
                self.vy.append(pyxel.sin(self.angle[len(self.ballx)-1]))
                self.speed.append(1)

    def draw(self):
            pyxel.cls(7)
            for i in range(0,len(self.ballx)):
                pyxel.circ(self.ballx[i],self.bally[i],10,6)
            if self.miss>=10:
                pyxel.text(100,100,'gameover',0)
            pyxel.rect(self.padx-20,195,40,5,14)
            pyxel.text(20,20,'score:'+self.StrCount,0)
            pyxel.text(20,30,'miss:'+self.StrMiss,0)

App()
