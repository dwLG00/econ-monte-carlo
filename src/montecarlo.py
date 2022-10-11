import numpy as np
import random

# MESSAGE TO JACK: I'm unsure about the math for all of this, so you should double check

# dlog(y) = dY/Y ~ Norm(0, sigma^2 dt)
# dlog(x) = dX/X ~ Norm(mu dt, Y^2 dt)

# We can integrate dY = sigma Y dB using Ito's lemma to get Y = Y0 * e^(sigma t - sigma^2 / 2 B)
# Then, because we know that dlog(x) ~ Norm(mu dt, Y^2 dt), and because dlog(x) = dX/X, we can say that X = X0 * e^dlog(x)

def Y(B, t, Y0, sigma):
	return Y0 * math.e**(sigma * t - sigma**2 / 2 * B)

#TODO: Equation for X
