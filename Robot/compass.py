from i2clibraries import i2c_hmc5883l
import math
 


def get_bearing():

    (x, y, z) = hmc5883l.getAxes()
    bearing  = math.atan2(y, x) 
    if (bearing < 0):
        bearing += 2 * math.pi
    
    print ("Bearing: ", math.degrees(bearing))
    return bearing

def __init__():
    hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)

    hmc5883l.setContinuousMode()
    hmc5883l.setDeclination(-0, 56)
    # magnetic declination for aberdeen found from magnetic-declination.com
    
    print(hmc5883l)

    # To scaled axes
    b = get_bearing()