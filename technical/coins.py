from tradingview_ta import TA_Handler, Interval, Exchange



class Hour():
        @staticmethod
        def summary(hour,pair):

                if hour == 1:Interv=Interval.INTERVAL_1_HOUR 
                elif hour == 2:Interv=Interval.INTERVAL_2_HOURS
                elif hour == 4:Interv=Interval.INTERVAL_4_HOURS

                ta = TA_Handler(
                symbol=pair.upper(),
                screener="CRYPTO",
                exchange="BINANCE",
                interval=Interv,
                # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
                )
                return ta.get_analysis().summary
