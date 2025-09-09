#!/usr/bin/env python3
"""
تست کامل swing detection با threshold جدید
"""
from mt5_connector import MT5Connector
from get_legs import get_legs
from swing import get_swing_points
from fibo_calculate import fibonacci_retracement
import numpy as np

def test_complete_workflow():
    print("🎯 Testing complete workflow with USDJPY and new threshold...")
    
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
    
    print(f"📊 Testing with {len(data)} records")
    print(f"   Time range: {data.index[0]} to {data.index[-1]}")
    
    # تشخیص legs
    legs = get_legs(data)
    print(f"✅ Found {len(legs)} legs")
    
    if len(legs) >= 3:
        # نمایش آخرین 3 legs
        last_3_legs = legs[-3:]
        print(f"\n📈 Last 3 legs:")
        for i, leg in enumerate(last_3_legs):
            print(f"   Leg {i+1}: {leg['start']} -> {leg['end']}")
            print(f"           Direction: {leg['direction']}, Length: {leg['length']:.1f} points")
        
        # تست swing detection
        print(f"\n🔄 Testing swing detection...")
        swing_type, is_swing = get_swing_points(data=data, legs=last_3_legs)
        print(f"   Swing type: {swing_type}")
        print(f"   Is swing: {is_swing}")
        
        if is_swing:
            print(f"✅ Swing detected! Type: {swing_type}")
            
            # تست fibonacci calculation
            try:
                leg1 = last_3_legs[0]
                
                if swing_type == 'bullish':
                    fib_start = data.loc[leg1['start']]['low']
                    fib_end = data.loc[leg1['end']]['high']
                else:
                    fib_start = data.loc[leg1['start']]['high']  
                    fib_end = data.loc[leg1['end']]['low']
                
                fib_levels = fibonacci_retracement(fib_start, fib_end)
                print(f"\n📊 Fibonacci levels:")
                for level, price in fib_levels.items():
                    print(f"   {level}: {price:.3f}")
                    
                # شبیه‌سازی شرایط entry
                current_price = data['close'].iloc[-1]
                print(f"\n💹 Current price: {current_price:.3f}")
                print(f"   Distance to 0.705: {abs(current_price - fib_levels['0.705']):.3f}")
                print(f"   Distance to 0.9: {abs(current_price - fib_levels['0.9']):.3f}")
                
                # بررسی شرایط entry
                entry_tolerance = 0.002  # 2 pips for USDJPY
                close_to_705 = abs(current_price - fib_levels['0.705']) <= entry_tolerance
                close_to_90 = abs(current_price - fib_levels['0.9']) <= entry_tolerance
                
                print(f"\n🎯 Entry conditions:")
                print(f"   Close to 0.705 (±{entry_tolerance:.3f}): {close_to_705}")
                print(f"   Close to 0.9 (±{entry_tolerance:.3f}): {close_to_90}")
                
                if close_to_705 or close_to_90:
                    print(f"🚀 Entry condition MET!")
                else:
                    print(f"⏳ Waiting for entry condition...")
                    
            except Exception as e:
                print(f"❌ Fibonacci calculation error: {e}")
        else:
            print(f"⏳ No swing detected, waiting...")
    
    else:
        print(f"⏳ Not enough legs for swing detection (need 3, have {len(legs)})")
    
    mt5_conn.shutdown()
    print(f"\n✅ Complete workflow test finished!")

if __name__ == "__main__":
    test_complete_workflow()
