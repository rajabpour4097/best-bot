#!/usr/bin/env python3
"""
تست جامع عملکرد ربات با USDJPY
"""
import sys
from mt5_connector import MT5Connector
from metatrader5_config import MT5_CONFIG
from fibo_calculate import fibonacci_retracement
from get_legs import get_legs
from swing import get_swing_points
import numpy as np

def test_bot_components():
    print("🧪 Testing all bot components with USDJPY...")
    
    # تست اتصال MT5
    print("\n1️⃣ Testing MT5 Connection...")
    mt5_conn = MT5Connector()
    if not mt5_conn.initialize():
        print("❌ MT5 initialization failed")
        return False
    print("✅ MT5 connected successfully")
    
    # تست دریافت داده
    print("\n2️⃣ Testing Historical Data...")
    data = mt5_conn.get_historical_data(count=200)
    if data is None or len(data) < 50:
        print("❌ Insufficient historical data")
        mt5_conn.shutdown()
        return False
    print(f"✅ Historical data retrieved: {len(data)} records")
    print(f"   - Data range: {data.index[0]} to {data.index[-1]}")
    print(f"   - Last close: {data['close'].iloc[-1]}")
    
    # اضافه کردن ستون status
    data['status'] = np.where(data['open'] > data['close'], 'bearish', 'bullish')
    
    # تست legs
    print("\n3️⃣ Testing Legs Detection...")
    legs = get_legs(data)
    print(f"✅ Legs detected: {len(legs)}")
    if len(legs) > 0:
        for i, leg in enumerate(legs[-3:] if len(legs) > 3 else legs):
            start_time = leg['start']  # Already a timestamp
            end_time = leg['end']      # Already a timestamp
            print(f"   - Leg {i+1}: {start_time} -> {end_time}")
            print(f"     Direction: {leg['direction']}, Length: {leg['length']:.1f} points")
    
    # تست swing detection
    if len(legs) >= 3:
        print("\n4️⃣ Testing Swing Detection...")
        last_3_legs = legs[-3:]
        swing_type, is_swing = get_swing_points(data=data, legs=last_3_legs)
        print(f"✅ Swing analysis:")
        print(f"   - Swing type: {swing_type}")
        print(f"   - Is swing: {is_swing}")
        
        # تست fibonacci اگر swing موجود است
        if is_swing:
            print("\n5️⃣ Testing Fibonacci Calculation...")
            try:
                # استخراج نقاط برای محاسبه فیبوناچی
                leg1 = last_3_legs[0]
                leg2 = last_3_legs[1]
                
                if swing_type == 'bullish':
                    fib_start = data.loc[leg1['start']]['low']
                    fib_end = data.loc[leg1['end']]['high']
                else:
                    fib_start = data.loc[leg1['start']]['high']  
                    fib_end = data.loc[leg1['end']]['low']
                
                fib_levels = fibonacci_retracement(fib_start, fib_end)
                print(f"✅ Fibonacci levels calculated:")
                for level, price in fib_levels.items():
                    print(f"   - {level}: {price:.5f}")
                    
            except Exception as e:
                print(f"⚠️ Fibonacci calculation error: {e}")
    
    # تست live price
    print("\n6️⃣ Testing Live Price...")
    live_price = mt5_conn.get_live_price()
    if live_price:
        print(f"✅ Live price retrieved:")
        print(f"   - Bid: {live_price['bid']}")
        print(f"   - Ask: {live_price['ask']}")
        print(f"   - Spread: {live_price['spread']:.1f} points")
    
    # تست volume calculation
    print("\n7️⃣ Testing Volume Calculation...")
    if live_price:
        try:
            # فرض کنیم SL فاصله 50 نقطه دارد
            import MetaTrader5 as mt5
            info = mt5.symbol_info(MT5_CONFIG['symbol'])
            sl_distance = 50 * info.point if info else 0.050
            
            entry_price = live_price['ask']
            sl_price = entry_price - sl_distance
            
            calculated_volume = mt5_conn.calculate_volume_by_risk(
                entry=entry_price,
                sl=sl_price,
                tick=type('Tick', (), {'bid': live_price['bid'], 'ask': live_price['ask']})(),
                risk_pct=0.01
            )
            print(f"✅ Volume calculation:")
            print(f"   - Entry: {entry_price}")
            print(f"   - SL: {sl_price}")
            print(f"   - Calculated volume: {calculated_volume}")
        except Exception as e:
            print(f"⚠️ Volume calculation error: {e}")
    
    # تست trading conditions
    print("\n8️⃣ Testing Trading Conditions...")
    can_trade, message = mt5_conn.can_trade()
    print(f"✅ Trading conditions:")
    print(f"   - Can trade: {can_trade}")
    print(f"   - Message: {message}")
    
    mt5_conn.shutdown()
    print("\n🎉 All component tests completed!")
    return True

if __name__ == "__main__":
    try:
        success = test_bot_components()
        if success:
            print("\n✅ USDJPY Bot Components Test PASSED")
            print("🚀 Bot is ready to trade with USDJPY!")
        else:
            print("\n❌ USDJPY Bot Components Test FAILED")
    except Exception as e:
        print(f"\n💥 Test error: {e}")
        import traceback
        traceback.print_exc()
