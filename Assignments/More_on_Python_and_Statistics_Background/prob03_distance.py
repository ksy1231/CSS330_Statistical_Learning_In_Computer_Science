import numpy as N
#import math

x = N.arange(5)
y = N.arange(4)

def distance(x, y, pt):
    """Calculate the distance between (x, y) and pt.

        Positional Input Parameters:
            x : numpy array
                Array of values.  Must all be numerical.

            y : numpy array
                Array of values.  Must all be numerical.
            
            pt : two points
        
        Returns:
             numpy array of the distance function.
    """
    """
    pt1, pt2 = pt
    dist = N.zeros((4,5), dtype='f')
    for i in range(len(y)):
        for j in range(len(x)):
            dist[i, j] = math.sqrt((x[j] - pt1)**2 + (y[i] - pt2)**2)
    return dist    
    """
    import numpy as N
    output_shape = (N.size(y), N.size(x))
    xall = N.resize(x, output_shape)
    yall = N.reshape(N.repeat(y, N.size(x)), output_shape)
    return (( (xall-pt[0])**2) + ((yall-pt[1])**2))**0.5
    
print(distance(x, y, [-2.3, 3.3]))