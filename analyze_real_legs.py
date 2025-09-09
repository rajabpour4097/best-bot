#!/usr/bin/env python3
"""
بررسی legs واقعی و محاسبه pip آنها
"""
from mt5_connector import MT5Connector
from get_legs import get_legs
import numpy as np

def analyze_real_legs():
    print("🔍 بررسی Legs واقعی USDJPY و محاسبه Pip")
    print("=" * 50)
    
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
    
    # تشخیص legs
    legs = get_legs(data)
    print(f"✅ تعداد legs شناسایی شده: {len(legs)}")
    
    if len(legs) > 0:
        print(f"\n📊 تحلیل legs:")
        for i, leg in enumerate(legs):
            # محاسبه pip واقعی
            start_price = leg['start_value']
            end_price = leg['end_value']
            pip_movement = abs(end_price - start_price) / 0.01  # برای JPY: 1 pip = 0.01
            
            print(f"\n   Leg {i+1}:")
            print(f"   ├─ زمان: {leg['start']} → {leg['end']}")
            print(f"   ├─ قیمت: {start_price:.3f} → {end_price:.3f}")
            print(f"   ├─ جهت: {leg['direction']}")
            print(f"   ├─ Threshold value: {leg['length']:.1f}")
            print(f"   └─ حرکت واقعی: {pip_movement:.1f} pip")
            
            # بررسی آیا کمتر از threshold است
            if leg['length'] < 50:
                print(f"      ⚠️ این leg کمتر از threshold (50) است!")
    
    print(f"\n📈 خلاصه:")
    print(f"   - Threshold = 50 = 0.5 pip")
    print(f"   - یعنی legs کمتر از 0.5 pip نادیده گرفته می‌شوند")
    print(f"   - این کمک می‌کند تا فقط حرکات معنادار شناسایی شوند")
    
    mt5_conn.shutdown()

if __name__ == "__main__":
    analyze_real_legs()
