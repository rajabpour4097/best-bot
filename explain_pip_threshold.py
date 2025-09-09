#!/usr/bin/env python3
"""
توضیح تفاوت بین threshold و pip برای USDJPY
"""

def explain_pip_vs_threshold():
    print("📊 تفاوت بین Threshold و Pip برای USDJPY")
    print("=" * 50)
    
    print("\n1️⃣ تعریف Pip:")
    print("   - EURUSD: 1 pip = 0.0001 (رقم چهارم)")
    print("   - USDJPY: 1 pip = 0.01 (رقم دوم)")
    print("   - نکته: JPY pairs دارای 2 رقم اعشار هستند")
    
    print("\n2️⃣ محاسبه در کد:")
    print("   فرمول: price_diff = abs(current_price - start_price) * 10000")
    
    print("\n3️⃣ مثال عملی USDJPY:")
    
    # مثال 1: حرکت 1 pip
    start_price = 146.50
    end_price_1pip = 146.51  # 1 pip بالاتر
    diff_1pip = abs(end_price_1pip - start_price) * 10000
    print(f"\n   🔹 حرکت 1 pip:")
    print(f"      {start_price} → {end_price_1pip}")
    print(f"      Threshold value: {diff_1pip}")
    
    # مثال 2: حرکت 5 pip  
    end_price_5pip = 146.55  # 5 pip بالاتر
    diff_5pip = abs(end_price_5pip - start_price) * 10000
    print(f"\n   🔹 حرکت 5 pip:")
    print(f"      {start_price} → {end_price_5pip}")
    print(f"      Threshold value: {diff_5pip}")
    
    # مثال 3: threshold فعلی ما
    threshold_current = 50
    equivalent_pips = threshold_current / 100  # تقسیم بر 100 برای JPY
    print(f"\n4️⃣ Threshold فعلی ما:")
    print(f"   Threshold = {threshold_current}")
    print(f"   معادل تقریبی: {equivalent_pips} pip")
    
    print(f"\n5️⃣ مقایسه:")
    print(f"   - 1 pip = {100} در واحد threshold")
    print(f"   - Threshold 50 = {50/100} pip")
    print(f"   - Threshold 6 برای EURUSD = {6/10} pip")
    
    print(f"\n6️⃣ معنی threshold در legs:")
    print(f"   - هر leg باید حداقل {equivalent_pips} pip حرکت داشته باشد")
    print(f"   - این یعنی حرکات کوچکتر نادیده گرفته می‌شوند")
    print(f"   - فقط حرکات معنادار به عنوان leg شناخته می‌شوند")
    
    print(f"\n💡 نتیجه:")
    print(f"   بله! هر leg حداقل {equivalent_pips} pip باید باشد")
    print(f"   این برای فیلتر کردن نویز (noise) بازار است")

if __name__ == "__main__":
    explain_pip_vs_threshold()
