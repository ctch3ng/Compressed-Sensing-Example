## Reconstruction of an image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.ndimage as spimg
import scipy.fftpack as spfft
import matplotlib.pyplot as plt
from pylbfgs import owlqn

plt.close('all')

def dct2(x):
    return spfft.dct(spfft.dct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)

def idct2(x):
    return spfft.idct(spfft.idct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)



def evaluate(x, g, step):
    """An in-memory evaluation callback."""

    # we want to return two things: 
    # (1) the norm squared of the residuals, sum((Ax-b).^2), and
    # (2) the gradient 2*A'(Ax-b)

    # expand x columns-first
    x2 = x.reshape((nx, ny)).T

    # Ax is just the inverse 2D dct of x2
    Ax2 = idct2(x2)

    # stack columns and extract samples
    Ax = Ax2.T.flat[ri].reshape(b.shape)

    # calculate the residual Ax-b and its 2-norm squared
    Axb = Ax - b
    fx = np.sum(np.power(Axb, 2))

    # project residual vector (k x 1) onto blank image (ny x nx)
    Axb2 = np.zeros(x2.shape)
    Axb2.T.flat[ri] = Axb # fill columns-first

    # A'(Ax-b) is just the 2D dct of Axb2
    AtAxb2 = 2 * dct2(Axb2)
    AtAxb = AtAxb2.T.reshape(x.shape) # stack columns

    # copy over the gradient vector
    np.copyto(g, AtAxb)

    return fx

# fractions of the scaled image to randomly sample at
sample_sizes = (0.5, 0.3, 0.1, 0.01)

# read original image
Xorig = spimg.imread('Sample.png', mode='L')
#ny,nx,nchan = Xorig.shape
ny,nx = Xorig.shape

# for each sample size
Z = [np.zeros(Xorig.shape, dtype='uint8') for s in sample_sizes]
masks = [np.zeros(Xorig.shape, dtype='uint8') for s in sample_sizes]
for i,s in enumerate(sample_sizes):

    # create random sampling index vector
    k = round(nx * ny * s)
    ri = np.random.choice(nx * ny, k, replace=False) # random sample of indices

    # for each color channel
    #for j in range(nchan):

    # extract channel
    #X = Xorig[:,:,j].squeeze()
    X = Xorig[:,:].squeeze()

    # create images of mask (for visualization)
    Xm = 255 * np.ones(X.shape)
    Xm.T.flat[ri] = X.T.flat[ri]
    #masks[i][:,:,j] = Xm
    masks[i][:,:] = Xm

    # take random samples of image, store them in a vector b
    b = X.T.flat[ri].astype(float)

    # perform the L1 minimization in memory
    Xat2 = owlqn(nx*ny, evaluate, None, 5)

    # transform the output back into the spatial domain
    Xat = Xat2.reshape(nx, ny).T # stack columns
    Xa = idct2(Xat)
    #Z[i][:,:,j] = Xa.astype('uint8')
    Z[i][:,:] = Xa.astype('uint8')        



plt.figure(0)
plt.subplot(311)
plt.imshow(Xorig,cmap='gray', interpolation='nearest')
plt.title('Original image')
plt.subplot(312)
plt.imshow(masks[0],cmap='gray', interpolation='nearest')
plt.title('CS image 50% Mask')
plt.subplot(313)
plt.imshow(Z[0],cmap='gray', interpolation='nearest')
plt.title('CS image 50%')
plt.tight_layout()
plt.show()

plt.figure(1)
plt.subplot(311)
plt.imshow(Xorig,cmap='gray', interpolation='nearest')
plt.title('Original image')
plt.subplot(312)
plt.imshow(masks[1],cmap='gray', interpolation='nearest')
plt.title('CS image 30% Mask')
plt.subplot(313)
plt.imshow(Z[1],cmap='gray', interpolation='nearest')
plt.title('CS image 30%')
plt.tight_layout()
plt.show()

plt.figure(2)
plt.subplot(311)
plt.imshow(Xorig,cmap='gray', interpolation='nearest')
plt.title('Original image')
plt.subplot(312)
plt.imshow(masks[2],cmap='gray', interpolation='nearest')
plt.title('CS image 10% Mask')
plt.subplot(313)
plt.imshow(Z[2],cmap='gray', interpolation='nearest')
plt.title('CS image 10%')
plt.tight_layout()
plt.show()

plt.figure(3)
plt.subplot(311)
plt.imshow(Xorig,cmap='gray', interpolation='nearest')
plt.title('Original image')
plt.subplot(312)
plt.imshow(masks[3],cmap='gray', interpolation='nearest')
plt.title('CS image 1% Mask')
plt.subplot(313)
plt.imshow(Z[3],cmap='gray', interpolation='nearest')
plt.title('CS image 1%')
plt.tight_layout()
plt.show()
