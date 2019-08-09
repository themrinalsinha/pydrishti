import matplotlib.pyplot as plt

def plot_image(image, cmap=None, title=''):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.show()
