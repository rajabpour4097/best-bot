#!/usr/bin/env python3
"""
توضیح تفاوت threshold برای EURUSD vs USDJPY
"""
import MetaTrader5 as mt5

def explain_threshold_difference():
    print("📊 توضیح تفاوت Threshold بین EURUSD و USDJPY")
    print("=" * 60)
    
    # شبیه‌سازی قیمت‌ها
    print("\n1️⃣ مقایسه ساختار قیمت:")
    print("   EURUSD: 1.08945 (5 digits)")
    print("   USDJPY: 146.789 (3 digits)")
    
    print("\n2️⃣ تفاوت Point size:")
    print("   EURUSD Point: 0.00001")
    print("   USDJPY Point: 0.001")
    print("   نسبت: USDJPY point = 100 × EURUSD point")
    
    print("\n3️⃣ محاسبه price_diff در کد:")
    print("   فرمول: price_diff = abs(current_price - start_price) * 10000")
    
    # مثال محاسبه برای EURUSD
    print("\n   🔹 مثال EURUSD:")
    start_eur = 1.08945
    end_eur = 1.08951  # تغییر 0.6 pip
    diff_eur = abs(end_eur - start_eur) * 10000
    print(f"      Start: {start_eur}")
    print(f"      End: {end_eur}")
    print(f"      Diff: {diff_eur:.1f} (threshold=6 ✅)")
    
    # مثال محاسبه برای USDJPY
    print("\n   🔹 مثال USDJPY:")
    start_jpy = 146.789
    end_jpy = 146.795  # تغییر 0.6 pip
    diff_jpy = abs(end_jpy - start_jpy) * 10000
    print(f"      Start: {start_jpy}")
    print(f"      End: {end_jpy}")
    print(f"      Diff: {diff_jpy:.1f} (threshold=6 ❌ خیلی کم)")
    
    print("\n4️⃣ معادل‌سازی Threshold:")
    print("   برای همان حرکت 0.6 pip:")
    print(f"   EURUSD: threshold = 6")
    print(f"   USDJPY: threshold = 60 (تقریباً)")
    print("   نسبت: 10:1")
    
    print("\n5️⃣ چرا 50 انتخاب شد؟")
    print("   - میانگین حرکت USDJPY: 166 points")
    print("   - 50 = حدود 30% از میانگین حرکت")
    print("   - 6 برای EURUSD = حدود 30% از میانگین حرکت آن")
    
    print("\n6️⃣ مقایسه معنی واقعی:")
    threshold_eur_pips = 6 / 10  # تقریباً 0.6 pip
    threshold_jpy_pips = 50 / 10  # تقریباً 5 pips
    
    print(f"   EURUSD threshold 6 ≈ {threshold_eur_pips} pips")
    print(f"   USDJPY threshold 50 ≈ {threshold_jpy_pips} pips")
    print("   این تفاوت به دلیل طبیعت متفاوت این نمادهاست")
    
    print("\n💡 نتیجه‌گیری:")
    print("   50 معادل 6 نیست، بلکه معادل همان حساسیت در نماد USDJPY است")
    print("   هر نماد threshold خاص خودش را نیاز دارد")

if __name__ == "__main__":
    explain_threshold_difference()
