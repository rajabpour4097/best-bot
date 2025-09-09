#!/usr/bin/env python3
"""
تست threshold جدید 600 و نمایش 3 legs آخر
"""
from mt5_connector import MT5Connector
from get_legs import get_legs
import numpy as np

def test_new_threshold():
    print("🎯 تست Threshold جدید 600 برای USDJPY")
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
    
    print(f"📊 Data info:")
    print(f"   - Records: {len(data)}")
    print(f"   - Time range: {data.index[0]} to {data.index[-1]}")
    
    # تشخیص legs با threshold جدید
    legs = get_legs(data)
    print(f"✅ تعداد legs با threshold 600: {len(legs)}")
    
    if len(legs) == 0:
        print("❌ هیچ leg شناسایی نشد! threshold خیلی بزرگ است")
        # تست با threshold کوچکتر
        print("\n🔄 تست با threshold های کوچکتر:")
        for test_threshold in [100, 200, 300, 400, 500]:
            test_legs = get_legs(data, custom_threshold=test_threshold)
            print(f"   Threshold {test_threshold}: {len(test_legs)} legs")
    
    elif len(legs) >= 3:
        print(f"\n📈 3 legs آخر:")
        last_3_legs = legs[-3:]
        
        for i, leg in enumerate(last_3_legs):
            # محاسبه pip واقعی
            start_price = leg['start_value']
            end_price = leg['end_value']
            pip_movement = abs(end_price - start_price) / 0.01  # برای JPY: 1 pip = 0.01
            
            duration = leg['end'] - leg['start']
            
            print(f"\n   📍 Leg {i+1}:")
            print(f"   ├─ زمان: {leg['start']} → {leg['end']}")
            print(f"   ├─ مدت: {duration}")
            print(f"   ├─ قیمت: {start_price:.3f} → {end_price:.3f}")
            print(f"   ├─ جهت: {leg['direction']}")
            print(f"   ├─ Threshold value: {leg['length']:.1f}")
            print(f"   └─ حرکت واقعی: {pip_movement:.1f} pip")
            
            # مقایسه با EURUSD
            equivalent_eurusd = leg['length'] / 100  # تبدیل به معادل EURUSD
            print(f"      💡 معادل EURUSD: {equivalent_eurusd:.1f}")
    
    else:
        print(f"\n⚠️ فقط {len(legs)} legs شناسایی شد (کمتر از 3)")
        for i, leg in enumerate(legs):
            start_price = leg['start_value']
            end_price = leg['end_value']
            pip_movement = abs(end_price - start_price) / 0.01
            
            print(f"\n   📍 Leg {i+1}:")
            print(f"   ├─ زمان: {leg['start']} → {leg['end']}")
            print(f"   ├─ قیمت: {start_price:.3f} → {end_price:.3f}")
            print(f"   ├─ جهت: {leg['direction']}")
            print(f"   ├─ Threshold value: {leg['length']:.1f}")
            print(f"   └─ حرکت واقعی: {pip_movement:.1f} pip")
    
    print(f"\n💡 خلاصه threshold جدید:")
    print(f"   - Threshold 600 = حداقل 6 pip برای هر leg")
    print(f"   - معادل threshold 6 در EURUSD")
    print(f"   - فقط حرکات بزرگ و معنادار شناسایی می‌شوند")
    
    mt5_conn.shutdown()

if __name__ == "__main__":
    test_new_threshold()
