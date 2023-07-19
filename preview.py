import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle


plt.style.use(r'nord-deep-new.mplstyle')
# Fixing random state for reproducibility
np.random.seed(19680801)


def plot_scatter(ax, prng, nb_samples=100):
    """Scatter plot."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X-label')
    ax.set_title('Axes title')
    return ax


# def plot_colored_lines(ax):
#     """Plot lines with colors following the style color cycle."""
#     t = np.linspace(-10, 10, 100)

#     def sigmoid(t, t0):
#         return 1 / (1 + np.exp(-(t - t0)))

#     nb_colors = len(plt.rcParams['axes.prop_cycle'])
#     print(nb_colors)
#     shifts = np.linspace(-5, 5, nb_colors)
#     amplitudes = np.linspace(1, 1.5, nb_colors)
#     for t0, a in zip(shifts, amplitudes):
#         ax.plot(t, a * sigmoid(t, t0), '-')
#     ax.set_xlim(-10, 10)


def plot_colored_sinusoidal_lines(ax):
    """Plot sinusoidal lines with colors following the style color cycle."""
    L = 2 * np.pi
    x = np.linspace(0, L)
    nb_colors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, nb_colors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), '-')
    ax.set_xlim([x[0], x[-1]])
    return ax


def plot_bar_graphs(ax, prng, min_value=5, max_value=25, nb_samples=5):
    """Plot two bar graphs side by side, with letters as x-tick labels."""
    # x = np.arange(nb_samples)
    # ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    # width = 0.25
    # ax.bar(x, ya, width)
    # ax.bar(x + width, yb, width, color='C2')
    # ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])

    labels = ['a', 'b', 'c', 'd', 'e']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    ax.bar(x - width/2, men_means, width, label='G1')
    ax.bar(x + width/2, women_means, width, label='G2')

    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    Plot circle patches.

    NB: draws a fixed amount of samples, rather than using the length of
    the color cycle, because different styles may have different numbers
    of colors.
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # Add title for enabling grid
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # to plot circles as circles
    return ax


def plot_histograms(ax, prng, nb_samples=10000):
    """Plot 4 histograms and a text annotation."""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # Add a small annotation.
    ax.annotate('Annotation', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
    )
    return ax


def plot_figure(style_label=""):
    """Setup and plot the demonstration figure with a given style."""
    # Use a dedicated RandomState instance to draw the same "random" values
    # across the different figures.
    prng = np.random.RandomState(96917002)

    fig, axs = plt.subplots(ncols=5, nrows=1, num=style_label,
                            figsize=(14.8, 2.8), layout='constrained')

    # make a suptitle, in the same style for all subfigures,
    # except those with dark backgrounds, which get a lighter color:

    plot_scatter(axs[0], prng)
    plot_bar_graphs(axs[1], prng)
    plot_colored_sinusoidal_lines(axs[2])
    plot_histograms(axs[3], prng)
    plot_colored_circles(axs[4], prng)


if __name__ == "__main__":
    plot_figure()

    plt.show()
