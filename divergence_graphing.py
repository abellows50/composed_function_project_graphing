import matplotlib.pyplot as plt
import numpy

# DEFINE THE HIGH AND LOW BOUNDS FOR DIVERGENCE. FOR ALL X
# NOT INCLUDED IN THE INTERVAL [LOW_BOUND, HIGH_BOUND] WILL
# BE GUARENTEED TO DIVERGE BY SIMPLE LOGIC
HIGH_BOUND = 10
LOW_BOUND = 0.9

MAX_ITERATIONS = 10000
DENSITY = 1000

# THIS IS THE FUNCTION
def f(x):
    k = 0.02
    a = 0.9
    b = 2.1
    c = 4
    d = 10

    return k*(x-a)*(x-b)*(x-c)*(x-d) + x

def time_to_divergence(x):
    """
    This function returns the number of iterations it takes for the
    function f(x) to diverge. If it does not diverge, it returns
    MAX_ITERATIONS.
    """
    for i in range(MAX_ITERATIONS):
        x = f(x)
        if x > HIGH_BOUND+0.5 or x < LOW_BOUND -0.5: # increment to avoid floating point errors
            return i
    return -1

def divergence_time_ray_to_color_ray(times:list):
    """
    This function returns a color based on the time to divergence.
    The color is a tuple of (R, G, B) values.
    Use the max value of the time to divergence in the ray to determine the color.
    """
    
    max_time = max(times)
    
    colors = []
    for time in times:
        if time == -1:
            colors.append((0, 0, 0))
        else:
            color = (1- time / max_time, 0, time / max_time)
            colors.append(color)
    return colors

    
# make the matplot lib plot, 
# y=x will be graphed in grey
# f will be graphed in a color determined by the time to divergence

def graph():
    """
    This function graphs the function f(x) and the line y=x.
    The color of the line is determined by the time to divergence.
    """
    
    """
    it should plot point by point determining the color of each point
    based on the time to divergence. Both the function and the line y=x should be visible
    """

    x = numpy.linspace(-8, 13, DENSITY)
    times = []
    for i in range(len(x)):
        times.append(time_to_divergence(x[i]))
    colors = divergence_time_ray_to_color_ray(times)
    plt.figure(figsize=(10, 10))
    plt.plot(x, x, color='grey', label='y=x')
    for i in range(len(x)):
        plt.plot(x[i], f(x[i]), color=colors[i], marker='o', markersize=1)
    plt.title('Divergence of f(x) = x^2 - 2')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(-8, 13)
    plt.ylim(-10, 15)
    plt.grid()
    plt.legend()
    # size window
    plt.gcf().set_size_inches(8, 8)
    plt.show()

if __name__ == "__main__":
    graph()
