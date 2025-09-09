#!/usr/bin/env python3
"""
تشخیص مشکل legs برای USDJPY
"""
from mt5_connector import MT5Connector
from get_legs import get_legs
from metatrader5_config import TRADING_CONFIG
import numpy as np

def debug_legs_detection():
    print("🔍 Debugging legs detection for USDJPY...")
    
    # اتصال MT5
    mt5_conn = MT5Connector()
    if not mt5_conn.initialize():
        print("❌ MT5 initialization failed")
        return
    
    # دریافت داده
    data = mt5_conn.get_historical_data(count=200)
    if data is None:
        print("❌ No data received")
        mt5_conn.shutdown()
        return
    
    data['status'] = np.where(data['open'] > data['close'], 'bearish', 'bullish')
    
    print(f"📊 Data info:")
    print(f"   - Records: {len(data)}")
    print(f"   - Time range: {data.index[0]} to {data.index[-1]}")
    print(f"   - Price range: {data['low'].min():.3f} - {data['high'].max():.3f}")
    
    # محاسبه price movements در points برای USDJPY
    price_changes = []
    for i in range(1, min(20, len(data))):  # بررسی 20 کندل اول
        price_change = abs(data['close'].iloc[i] - data['close'].iloc[i-1]) * 10000
        price_changes.append(price_change)
        print(f"   - Candle {i}: Close change = {price_change:.1f} points")
    
    avg_change = np.mean(price_changes)
    max_change = max(price_changes)
    
    print(f"\n📈 Price movement analysis:")
    print(f"   - Average change: {avg_change:.1f} points")
    print(f"   - Maximum change: {max_change:.1f} points")
    print(f"   - Current threshold: {TRADING_CONFIG['threshold']} points")
    
    # تست با threshold های مختلف
    print(f"\n🧪 Testing different thresholds:")
    for test_threshold in [1, 2, 3, 4, 5, 6, 10, 15, 20]:
        legs = get_legs(data, custom_threshold=test_threshold)
        print(f"   - Threshold {test_threshold}: {len(legs)} legs found")
        if len(legs) > 0:
            for i, leg in enumerate(legs[:3]):  # نمایش 3 leg اول
                print(f"     Leg {i+1}: {leg['direction']}, Length: {leg['length']:.1f} points")
    
    # بررسی volatility در timeframe فعلی
    print(f"\n📊 Volatility analysis:")
    highs = data['high'].values
    lows = data['low'].values
    volatility = []
    
    for i in range(1, len(data)):
        candle_range = (highs[i] - lows[i]) * 10000
        volatility.append(candle_range)
    
    avg_volatility = np.mean(volatility)
    print(f"   - Average candle range: {avg_volatility:.1f} points")
    print(f"   - Max candle range: {max(volatility):.1f} points")
    
    # پیشنهاد threshold بهینه
    suggested_threshold = max(2, int(avg_change * 1.5))
    print(f"\n💡 Suggested threshold: {suggested_threshold} points")
    
    mt5_conn.shutdown()

if __name__ == "__main__":
    debug_legs_detection()
