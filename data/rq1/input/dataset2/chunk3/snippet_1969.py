#Source: https://stackoverflow.com/questions/68143331/scipy-optimise-typeerror-takes-1-positional-argument-but-2-were-given-with-ext
@njit(cache=True)
def fn(x, weights):
    return np.sum((x - weights) ** 2)


@njit(cache=True)
def fn_cons(x):
    return np.sum(np.abs(x)) - 1


cons = ({'type': 'eq',
         'fun': fn_cons
         })


class TestSpeedup:

    def normalise(self, weights):
        result = minimize(
            fn,
            np.array(weights),
            args=(weights,),
            jac=lambda x: 2 * (x - weights),
            bounds=[(0, np.infty) for _ in weights],
            constraints=cons
        )
        minimum = result.x

        # return np.max([new_weights, np.zeros(new_weights.size)], axis=0) / np.sum(np.max([new_weights, np.zeros(new_weights.size)], axis=0))
        return minimum / np.sum(np.abs(minimum))

weights = np.array([ 1.04632843e+00, -6.89001783e-02,  2.17089646e-01, -2.52113073e-01, 4.19467585e-03])


test = TestSpeedup()
result = test.normalise(weights)