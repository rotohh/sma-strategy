class SimpleMA_strategy(IStrategy):
    
    ...
    
    # the following statement disables selling due to ROI
    minimal_roi = {
        "0": 100
    }
    
    # the following statement disables selling due to stop-loss
    stoploss = -1.0
    
	def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
	fast_period = 5
	slow_period = 50
	dataframe['fast_MA'] = ta.SMA(dataframe, timeperiod=fast_period)
	dataframe['slow_MA'] = ta.SMA(dataframe, timeperiod=slow_period)
	
	return dataframe

    
	def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
	dataframe.loc[
	  (
		qtpylib.crossed_above(dataframe['fast_MA'], dataframe['slow_MA'])
	  ),
	  'buy'] = 1
	
	return dataframe

        
	def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
	dataframe.loc[
	  (
		qtpylib.crossed_below(dataframe['fast_MA'], dataframe['slow_MA'])
	  ),
	  'sell'
	] = 1
	
	return dataframe

