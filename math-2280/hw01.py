
import numpy as np
import matplotlib.pyplot as plt


def plot_slope_field(f, x_range, y_range, x_points=20, y_points=20, ax=None):
    """
    Plots a slope field (direction field) for a 2D differential equation given by f(x, y)

    Parameters:
        f (function) : The differential equation
        x_range (list or tuple) : The range of x values to plot
        y_range (list or tuple) : The range of y values to plot
        x_points (int, optional) : The number of points to use in the x direction. Default is 20
        y_points (int, optional) : The number of points to use in the y direction. Default is 20
        ax (matplotlib.axes._subplots.AxesSubplot, optional) : The axes to use for plotting. If not provided, a new figure will be created

    Returns:
        matplotlib.axes._subplots.AxesSubplot : The axes used for plotting
    """

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = None

    x = np.linspace(x_range[0], x_range[1], x_points)
    y = np.linspace(y_range[0], y_range[1], y_points)
    X, Y = np.meshgrid(x, y)
    U = 1
    V = f(X,Y)
    ax.quiver(X, Y, U, V)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.set_title('Slope Field')
    if fig is not None:
        plt.show()
    return ax


def plot_particular_solution(x, y, x_range, y_range, ax=None):
    """
    Plots a particular solution to a 2D differential equation

    Parameters:
        x (numpy array) : The x values of the solution
        y (numpy array) : The y values of the solution
        x_range (list or tuple) : The range of x values to plot
        y_range (list or tuple) : The range of y values to plot
        ax (matplotlib.axes._subplots.AxesSubplot, optional) : The axes to use for plotting. If not provided, the slope field axes will be used

    Returns:
        matplotlib.axes._subplots.AxesSubplot : The axes used for plotting
    """

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = None

    ax.plot(x, y, 'c-', lw=2)
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('y\' = y - x')
    if fig is not None:
        plt.show()
    return ax


def dydx(x, y):
    return y - x


def get_particular(f, f0, dx, n):
    # f is the DE
    # dx is the step in x
    # n is the number of points to compute
    # y0 is the initial point (x,y) as a tuple
    pts = [f0]
    for i in range(n):
        x, y = pts[i][0], pts[i][1]
        diff = f(x, y)
        new_pt = (x + dx, y + (diff * dx))
        pts.append(new_pt)
    x_list = [x for x,y in pts]
    y_list = [y for x,y in pts]
    return x_list, y_list


#pts = [(x,2) for x in np.linspace(-3, 3, 6)]
# pts.extend([(x,-1) for x in np.linspace(-3, 3, 6)])
# pts.extend([(x,-1) for x in np.linspace(-2, 2, 10)])
# pts.extend([(x,-1) for x in np.linspace(-2, 2, 10)])
pts = [(4,0), (-4,0)]


# x, y = get_particular(dydx, (-1.5, -0.5), 0.1, 200)
fig, ax = plt.subplots()
plot_slope_field(dydx, [-5, 5], [-5, 5], ax=ax)

for pt in pts:
    x, y = get_particular(dydx, pt, 0.05, 1000)
    plot_particular_solution(x, y, [-5, 5], [-5, 5], ax)

plt.show()
