#Source: https://stackoverflow.com/questions/62761517/typeerror-invalid-shape-100-100-1-for-image-data-when-plot-image
sample_training_images, _ = next(traindata)
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.plot(images_arr)
    plt.show()

plotImages(sample_training_images[:5])