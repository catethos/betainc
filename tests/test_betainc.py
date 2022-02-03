from betainc import betacdf
from scipy.stats import beta
import numpy as np
import time

def test_closeness():
    xs = np.random.rand(100000)
    x = betacdf(xs, 0.6, 0.5)
    y = beta(0.6, 0.5).cdf(xs)
    assert np.allclose(x, y)