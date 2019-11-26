import numpy as np
import random
from star import *

"""
generates a file containing positions and velocities of stars
in a cluster
"""

class King:
    def psi(self, W):
        """
        function psi(W) from the King's article
        """
        x = 0.0
        psi = 0.0
        for x in np.arange(0.0, W, W/100.0):
            psi += np.exp(-x) * x**1.5 * W/100.0
        return psi * np.exp(W)
    
    def __init__(self, _W0=0.5, _rc=2e5, _rho0=2e-14):
        """
        initializes parameters of the cluster
        """
        self.G = 4.0 * np.pi * np.pi
        self.W0 = _W0
        self.rc = _rc
        self.rho0 = _rho0
        self.psi0 = self.psi(self.W0)
        self.j = np.sqrt(9.0/8.0/np.pi/self.G/self.rc/self.rc/self.rho0)
    
    def randr(self, r):
        """
        Generates a random 3D vector of length r
        """
        lambd = random.uniform(0, np.pi*2)
        sinphi = random.uniform(-1, 1)

        phi = np.arcsin(sinphi)
    
        x = np.cos(lambd) * np.cos(phi)
        y = np.sin(lambd) * np.cos(phi)
        z = np.cos(phi)
        return (r*x, r*y, r*z)
    
    def IMFKroupa(self, m):
        """
        Initial Mass Function
        """
        if m < 0.01:
            return 0
        if m >= 0.01 and m < 0.08:
            return m**(-0.3)
        if m >= 0.08 and m < 0.5:
            return m**(-1.3)
        if m >= 0.5:
            return m**(-2.3)
        return 0

    def generatemass(self):
        """
        generates mass of a star according to IMF
        """
        arr = np.zeros(10000)
        i = 1
        for m in np.arange(0.01, 100, 0.01):
            arr[i] = arr[i-1] + self.IMFKroupa(m)*0.01
            i += 1
        x = random.uniform(0.0, 1.0)
        for j in range(10000):
            arr[j] = arr[j]/arr[9999]
            if arr[j] > x:
                return float(j) / 100.0
        return 1

    def f(self, v, W):
        """
        function f from the King's article
        """
        return np.exp(W - self.W0) * (np.exp(- self.j**2 * v**2) - np.exp(-W))

    def generateVelocity(self, W):
        """
        generates velocity of a star
        """
        ve = np.sqrt(W / self.j**2)
        arr = np.zeros(100000)
        i = 1
        for v in np.arange(0.0, ve, 0.001):
            arr[i] = arr[i-1] + self.f(v, W)*0.001
            i += 1
        x = random.uniform(0.0, 1.0)
        for j in range(100000):
            arr[j] = arr[j]/arr[1000*int(ve) - 1]
            if arr[j] > x:
                return self.randr(float(i)/1000.0)
        return randr(1)

    def generateStar (self, idnumber, r, W):
        return Star(self.generatemass(), idnumber, self.randr(r), self.generateVelocity(W))


meanmass = 0.768642

W0 = 0.6
rc = 2e5
rho0 = 2e-14
generator = King(W0, rc, rho0)

file = open('initial.txt', 'w')

rho = generator.rho0
psi0 = generator.psi(W0)
R = 0.001
W = generator.W0
dW = -3.0 * R
ddW = -3.0
step = 0.001
cnt = 0
while W > 0:
    rho = rho0 * generator.psi(W) / psi0
    ddW = -9.0 * rho/rho0 - 2.0 / R * dW
    dW += ddW * step
    W += dW * step + ddW * step**2/2.0
    x = random.uniform(0.0, 1.0) * meanmass
    for i in range(int((4*np.pi * (R*rc)**2 * step * rc * rho) / x)):
        tmpStar = generator.generateStar(cnt, R*rc, W)
        file.write(str(tmpStar.idnumber) + ' ' + str(tmpStar.m) + ' ' + \
                   str(tmpStar.r[0]) + ' ' + str(tmpStar.r[1]) + ' ' + str(tmpStar.r[2]) + ' ' + \
                   str(tmpStar.v[0]) + ' ' + str(tmpStar.v[1]) + ' ' + str(tmpStar.v[2]) + '\n')
        print(R*rc/206264.8, cnt, W, tmpStar.m)
        cnt += 1
    R += step

print(cnt)

file.close()

















    


