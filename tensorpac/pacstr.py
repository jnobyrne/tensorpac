"""Simply get the name of defined methods."""

__all__ = ['pacstr']


def pacstr(idpac):
    """Return correspond methods string."""
    # Pac methods :
    if idpac[0] == 1:
        method = 'Mean Vector Length'
    elif idpac[0] == 2:
        method = 'Kullback-Leiber divergence'
    elif idpac[0] == 3:
        method = 'Heights ratio'
    elif idpac[0] == 4:
        method = 'ndPac'
    elif idpac[0] == 5:
        method = 'Phase-Synchrony'
    elif idpac[0] == 6:
        method = 'Event-Related Phase amplitude Coupling'

    # Surrogate method :
    if idpac[1] == 0:
        suro = 'No surrogates'
    elif idpac[1] == 1:
        suro = 'Swap phase/amplitude across trials'
    elif idpac[1] == 2:
        suro = 'Swap amplitude blocks across time'
    elif idpac[1] == 3:
        suro = 'Shuffle amplitude and phase time-series'
    elif idpac[1] == 4:
        suro = 'Shuffle phase time-series'
    elif idpac[1] == 5:
        suro = 'Shuffle amplitude time-series'
    elif idpac[1] == 6:
        suro = 'Time lag'
    elif idpac[1] == 7:
        suro = 'Circular shifting'

    # Normalization methods :
    if idpac[2] == 0:
        norm = 'No normalization'
    elif idpac[2] == 1:
        norm = 'Substract the mean of surrogates'
    elif idpac[2] == 2:
        norm = 'Divide by the mean of surrogates'
    elif idpac[2] == 3:
        norm = 'Substract then divide by the mean of surrogates'
    elif idpac[2] == 4:
        norm = "Substract the mean and divide by the deviation of the " + \
               "surrogates"

    return method, suro, norm
