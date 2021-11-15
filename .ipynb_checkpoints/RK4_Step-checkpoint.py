import numpy
def rk4_step(y,dydx_m,dx):
 #   A single 4th Order Runge Kutta Step
        k1 = dx*numpy.dot(dydx_m,y)
        k2 = dx*numpy.dot(dydx_m,y+k1/2)
        k3 = dx*numpy.dot(dydx_m,y+k2/2)
        k4 = dx*numpy.dot(dydx_m,y+k3)
        return k1/6 + k2/3 + k3/3 + k4/6