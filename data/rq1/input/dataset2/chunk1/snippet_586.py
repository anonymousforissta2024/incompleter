#Source: https://stackoverflow.com/questions/29078786/strange-nameerror-name-math-is-not-defined-while-import-math
import sigma as sgm # Module sigma has "import math" as well
import math
def sigma_crit(sigmaX, sigmaY, sigmaZ, Theta, Pw, Pres, nu, alpha, No):
    """
    Return value of critical stress calculated for one of three failure criterias.
    No: 1 - Simplified Mohr-Coulomb
        2 - Mohr-Coulomb
        3 - Drucker-Prager
        4 - list with 3 model's resutls
    sigmaX - stress at X wellbore axis
    sigmaY - stress at Y wellbore axis
    Theta - azimuth,anticlokwise from SH_max
    nu - Poisson's ratio
    alpha - Biot's  coefficient
    """ 
    sigma_theta = sgm.sigma_calc(sigmaX, sigmaY, sigmaZ, Theta, Pw, Pres, nu, alpha, 1)
    sigma_zi = sgm.sigma_calc(sigmaX, sigmaY, sigmaZ, Theta, Pw, Pres, nu, alpha, 2)
    sigma_thzi = sgm.sigma_calc(sigmaX, sigmaY, sigmaZ, Theta, Pw, Pres, nu, alpha,3)
    # Conerting degrees to radians for below equations...Caution above functions has built-in converter
    Theta = math.radians(Theta)
    # Simplified MC