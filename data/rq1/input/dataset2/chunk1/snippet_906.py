#Source: https://stackoverflow.com/questions/36295380/typeerror-improper-input-n-2-must-not-exceed-m-1
import math

#stolen sig-fig function <--trust but verify
def round_figures(x, n): 
    return round(x, int(n - math.ceil(math.log10(abs(x))))) 

def try_michaelis_menten_fit( df, pretty=False ):

    # auto-guess
    p0 = ( df['productFinal'].max(), df['substrateConcentration'].mean() )

    popt, pcov = curve_fit( v, df['substrateConcentration'], df['productFinal'], p0=p0 )
    perr = sqrt( diag( pcov ) )

    kcat_km = popt[0] / popt[1]
    # error propegation
    kcat_km_err = (sqrt( (( (perr[0])  / popt[0])**2) + ((  (perr[1])  / popt[1])**2) ))

    kcat = ( popt[0] )
    kcat_std_err = ( perr[0] )

    km_uM = ( popt[1] * 1000000 )
    km_std_err = ( perr[1] *1000000)


    if pretty:



        results = { 

        'kcat': round_figures(kcat, 3),
        'kcat_std_err': round_figures(kcat_std_err, 3),

        'km_uM': round_figures(km_uM, 5),
        'km_std_err': round_figures(km_std_err, 3),

        'kcat/km': round_figures(kcat_km, 2),
        'kcat/km_err': round_figures(kcat_km_err, 2),

        }

        return pandas.Series( results )
    else: 
        return popt, perr 

df = pandas.read_csv( 'PNP_Raw2Fittr.csv' ) 



fits = df.groupby('sample').apply( try_michaelis_menten_fit, pretty=True ) 
fits.to_csv( 'fits_pretty_output.csv' )
print( fits ) 