import pandas as pd
from statsmodels.tsa.stattools import acf, pacf

def get_acf_pacf_values(data, lags=40, alpha=0.05, show_table=True):
    """
    Calculate ACF and PACF values and optionally display as a table.

    Parameters:
    -----------
    data : numpy.ndarray
        Time series data
    lags : int
        Number of lags to calculate
    alpha : float
        Significance level for confidence intervals
    show_table : bool
        Whether to display the results as a table

    Returns:
    --------
    df : pandas.DataFrame
        DataFrame with ACF and PACF values and confidence intervals
    """
    acf_vals, acf_confint = acf(data, nlags=lags, alpha=alpha)
    pacf_vals, pacf_confint = pacf(data, nlags=lags, alpha=alpha, method='ywm')

    df = pd.DataFrame({
        'Lag': range(len(acf_vals)),
        'ACF': acf_vals,
        'PACF': pacf_vals,
    })

    if show_table:
        print("\n" + "=" * 100)
        print("ACF and PACF Values".center(100))
        print("=" * 100)
        print(df.to_string(index=False))
        print("=" * 100)

    return df
