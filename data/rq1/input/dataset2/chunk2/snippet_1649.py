#Source: https://stackoverflow.com/questions/63047188/converting-matlab-code-to-python-and-received-typeerror-numpy-ndarray-object
#simulate BE response over a line scan

# define experimental parameters
IO_rate = 4E6; #[samples/sec]
N_pixels = 128; # number of pixels along a line scan
N_points_per_pixel = 8192; # number of data points per pixel
w1 = 200E3; # lower edge of band
w2 = 400E3; # upper edge of band
noise_level = .1; #add noise to the signal

w_vec = np.arange(-IO_rate/2, IO_rate/2-IO_rate/N_points_per_pixel + 1, IO_rate/N_points_per_pixel)
# vary A, wo, Q, and phase over pixels
p_vec = np.arange(0, N_pixels-1)/N_pixels
A_vec = np.sin(2*np.pi*3*p_vec)+2 #amplitude
wo_vec = 250E3 + 100E3*p_vec #resonance
Q_vec = 100 - 50*p_vec # Q-factor
phi_vec = np.sign(p_vec-.5) # phase

D_vec = np.zeros(np.size(w_vec))
ind = (abs(w_vec)<w2) & (abs(w_vec)>w1);
D_vec[ind] = 1; #assign those indices to 1.
band_ind = np.nonzero(((w_vec)<w2) & ((w_vec)>w1));

d_vec = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(D_vec))) #find drive signal in the time domain
R_mat = np.zeros((N_pixels,N_points_per_pixel))
r_mat = np.zeros((N_pixels,N_points_per_pixel))

for k1 in range(N_pixels):
    H_vec = ((A_vec(k1)*wo_vec(k1)**2)*np.exp(1j*phi_vec(k1))/(w_vec**2 + 1j*wo_vec(k1)*w_vec/Q_vec(k1) - wo_vec(k1)**2)); #cantilever transfer function