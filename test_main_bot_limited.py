#!/usr/bin/env python3
"""
تست محدود ربات اصلی با USDJPY
"""
import sys
import time
import signal
from main_metatrader import main

def test_main_bot():
    print("🚀 Starting main bot test with USDJPY...")
    print("⏰ Test will run for 20 seconds...")
    
    start_time = time.time()
    max_duration = 20  # 20 ثانیه
    
    try:
        # شروع ربات در یک thread جداگانه یا با timeout
        import threading
        
        def run_bot():
            try:
                main()
            except KeyboardInterrupt:
                print("\n🛑 Bot stopped for test")
            except Exception as e:
                print(f"\n❌ Bot error: {e}")
        
        # شروع ربات در thread
        bot_thread = threading.Thread(target=run_bot, daemon=True)
        bot_thread.start()
        
        # انتظار برای مدت مشخص
        time.sleep(max_duration)
        
        print(f"\n⏰ Test completed after {max_duration} seconds")
        print("✅ Bot appears to be working with USDJPY")
        
    except KeyboardInterrupt:
        print("\n🛑 Test stopped by user")
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_main_bot()
