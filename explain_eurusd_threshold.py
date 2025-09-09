#!/usr/bin/env python3
"""
توضیح threshold در EURUSD - 6 یعنی چه؟
"""

def explain_eurusd_threshold():
    print("📊 توضیح Threshold 6 در EURUSD")
    print("=" * 50)
    
    print("\n1️⃣ فرمول محاسبه در کد:")
    print("   price_diff = abs(current_price - start_price) * 10000")
    
    print("\n2️⃣ مثال‌های عملی EURUSD:")
    
    # مثال 1: حرکت کوچک (زیر threshold)
    start1 = 1.08500
    end1 = 1.08505
    diff1 = abs(end1 - start1) * 10000
    pip1 = (end1 - start1) / 0.0001
    print(f"\n   🔹 مثال 1 - حرکت کوچک:")
    print(f"      {start1} → {end1}")
    print(f"      Threshold value: {diff1}")
    print(f"      Pip واقعی: {pip1} pip")
    print(f"      نتیجه: {diff1} < 6 → نادیده گرفته می‌شود ❌")
    
    # مثال 2: حرکت روی threshold
    start2 = 1.08500
    end2 = 1.08506
    diff2 = abs(end2 - start2) * 10000
    pip2 = (end2 - start2) / 0.0001
    print(f"\n   🔹 مثال 2 - روی threshold:")
    print(f"      {start2} → {end2}")
    print(f"      Threshold value: {diff2}")
    print(f"      Pip واقعی: {pip2} pip")
    print(f"      نتیجه: {diff2} = 6 → به عنوان leg شناخته می‌شود ✅")
    
    # مثال 3: حرکت بزرگ
    start3 = 1.08500
    end3 = 1.08520
    diff3 = abs(end3 - start3) * 10000
    pip3 = (end3 - start3) / 0.0001
    print(f"\n   🔹 مثال 3 - حرکت بزرگ:")
    print(f"      {start3} → {end3}")
    print(f"      Threshold value: {diff3}")
    print(f"      Pip واقعی: {pip3} pip")
    print(f"      نتیجه: {diff3} > 6 → به عنوان leg شناخته می‌شود ✅")
    
    print(f"\n3️⃣ تبدیل Threshold به Pip:")
    threshold_eurusd = 6
    pip_equivalent = threshold_eurusd / 10  # برای EUR pairs
    print(f"   Threshold {threshold_eurusd} = {pip_equivalent} pip")
    
    print(f"\n4️⃣ معنی واقعی:")
    print(f"   ❌ غلط: هر leg حداقل 6 pip است")
    print(f"   ✅ درست: هر leg حداقل {pip_equivalent} pip است")
    print(f"   یعنی حرکات کمتر از {pip_equivalent} pip نادیده گرفته می‌شوند")
    
    print(f"\n5️⃣ مثال legs واقعی که ممکن است تشخیص داده شوند:")
    examples = [
        (0.6, "حداقل - روی threshold"),
        (1.2, "حرکت متوسط"),
        (3.5, "حرکت بزرگ"),
        (0.5, "نادیده گرفته می‌شود - زیر threshold")
    ]
    
    for pip_val, desc in examples:
        threshold_val = pip_val * 10
        status = "✅" if threshold_val >= 6 else "❌"
        print(f"   {status} {pip_val} pip = {threshold_val} threshold - {desc}")
    
    print(f"\n💡 خلاصه:")
    print(f"   Threshold 6 در EURUSD = حداقل 0.6 pip برای هر leg")
    print(f"   نه اینکه هر leg دقیقاً 6 pip باشد!")

if __name__ == "__main__":
    explain_eurusd_threshold()
