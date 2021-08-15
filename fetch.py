import pandas as pd
from polygon import RESTClient
import matplotlib.pyplot as plt



with RESTClient(api_key) as client:
    resp = client.reference_stock_financials("AAPL", type="Q")

    r = pd.DataFrame(resp.results)
    r['leverage'] = r['assets'] / r['marketCapitalization']
    df = r[['calendarDate', 'debtToEquityRatio', 'priceToEarningsRatio', 'priceToBookValue', 'leverage', 'assets', 'marketCapitalization', 'debt']]
    fig, axs = plt.subplots(4, 1)
    df.set_index('calendarDate', inplace=True)
    df.index = pd.to_datetime(df.index)
    df.leverage.plot(axs[0])
    df.debtToEquityRatio.plot(axs[1])
    df.priceToEarningsRatio.plot(axs[2])
    df.priceToBookValue.plot(axs[3])
    plt.show()
