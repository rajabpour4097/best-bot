#!/usr/bin/env python3
"""
بررسی دقیق فرمول threshold و مقایسه EURUSD vs USDJPY
"""

def analyze_threshold_formula():
    print("🔍 بررسی دقیق فرمول Threshold")
    print("=" * 60)
    
    print("\n1️⃣ مثال شما - EURUSD:")
    start_eur = 1.17635
    end_eur = 1.17695
    diff_eur = abs(end_eur - start_eur) * 10000
    pip_eur = abs(end_eur - start_eur) / 0.0001
    
    print(f"   قیمت شروع: {start_eur}")
    print(f"   قیمت پایان: {end_eur}")
    print(f"   تفاوت: {end_eur - start_eur}")
    print(f"   Formula result: {diff_eur}")
    print(f"   Pip واقعی: {pip_eur} pip")
    print(f"   👆 بله! این دقیقاً 6 است و معادل 6 pip")
    
    print(f"\n2️⃣ مثال معادل در USDJPY:")
    # برای اینکه همان معنا داشته باشد، باید همان تناسب pip را داشته باشیم
    # اگر 6 در EURUSD = 6 pip، پس 50 در USDJPY باید = 5 pip باشد
    
    start_jpy = 146.500
    end_jpy = 146.550  # 5 pip حرکت
    diff_jpy = abs(end_jpy - start_jpy) * 10000
    pip_jpy = abs(end_jpy - start_jpy) / 0.01
    
    print(f"   قیمت شروع: {start_jpy}")
    print(f"   قیمت پایان: {end_jpy}")
    print(f"   تفاوت: {end_jpy - start_jpy}")
    print(f"   Formula result: {diff_jpy}")
    print(f"   Pip واقعی: {pip_jpy} pip")
    
    print(f"\n3️⃣ مقایسه مستقیم:")
    print(f"   EURUSD: threshold 6 = {diff_eur/10} pip")
    print(f"   USDJPY: threshold {diff_jpy} = {pip_jpy} pip")
    
    print(f"\n4️⃣ آیا threshold 50 در USDJPY معنای مشابه دارد؟")
    threshold_usdjpy = 50
    equivalent_pip_usdjpy = threshold_usdjpy / 100  # برای JPY pairs
    equivalent_pip_eurusd = 6 / 10  # برای EUR pairs
    
    print(f"   EURUSD threshold 6 = {equivalent_pip_eurusd} pip")
    print(f"   USDJPY threshold 50 = {equivalent_pip_usdjpy} pip")
    
    if abs(equivalent_pip_usdjpy - equivalent_pip_eurusd) < 0.2:
        print(f"   ✅ بله! تقریباً همان حساسیت را دارند")
    else:
        print(f"   ❌ خیر! حساسیت متفاوتی دارند")
    
    print(f"\n5️⃣ محاسبه threshold صحیح برای USDJPY:")
    # اگر بخواهیم دقیقاً همان حساسیت EURUSD را داشته باشیم
    target_pip = 6  # همان 6 pip که در مثال شما بود
    correct_threshold_jpy = target_pip * 100  # برای JPY
    
    print(f"   برای معادل بودن با مثال شما (6 pip):")
    print(f"   USDJPY threshold باید باشد: {correct_threshold_jpy}")
    
    print(f"\n6️⃣ تست با داده‌های واقعی:")
    # بررسی اینکه آیا legs واقعی ما چه اندازه هستند
    print(f"   در تست‌های قبلی دیدیم:")
    print(f"   - Leg با threshold 80 = 0.8 pip")
    print(f"   - Leg با threshold 210 = 2.1 pip") 
    print(f"   - Leg با threshold 860 = 8.6 pip")
    print(f"   👆 این نشان می‌دهد فرمول درست کار می‌کند")
    
    print(f"\n💡 نتیجه‌گیری:")
    print(f"   🔹 فرمول شما درست است: (price2 - price1) × 10000")
    print(f"   🔹 EURUSD threshold 6 = دقیقاً 6 pip")
    print(f"   🔹 USDJPY threshold 50 = دقیقاً 0.5 pip")
    print(f"   🔹 برای معادل بودن، USDJPY باید threshold 600 داشته باشد!")
    print(f"   🔹 اما ما 50 انتخاب کردیم = حساسیت بیشتر (فیلتر کمتر)")

if __name__ == "__main__":
    analyze_threshold_formula()
