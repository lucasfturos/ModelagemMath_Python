from scipy import integrate
from numpy import *
import pylab as P


class Model:
    def __init__(
        self,
        equations,
        inits,
        trange,
    ):
        self.eqs = equations
        self.Inits = inits
        self.Trange = arange(0, trange, 0.1)
        self.compileEqs()

    def compileEqs(self):
        try:
            self.ceqs = [compile(i, "< equation>", "eval") for i in self.eqs]
        except SyntaxError:
            print("Há um erro de sintaxe nas equações,\nConserte-o e tente novamente")

    def Run(self):
        t_courseList = []
        t_courseList.append(integrate.odeint(self.Equations, self.Inits, self.Trange))
        return (t_courseList, self.Trange)

    def Equations(self, y, t):
        eqs = self.ceqs
        Neq = len(eqs)
        ydot = zeros((Neq), "d")
        for k in range(Neq):
            ydot[k] = eval(eqs[k])
        return ydot


if __name__ == "__main__":
    inits = [1, 1]
    eqs = ["3.0*y[0]-2.0*y[0]*y[1]", "-2.0*y[1]+y[0]+[1]"]
    ODE = Model(eqs, inits, 10)
    y, t = ODE.Run()
    print(y)
    P.plot(t, y[0][:, 0], "v-", t, y[0][:, 1], "o-")
    P.legend(["Presa", "Predador"])
    P.show()
