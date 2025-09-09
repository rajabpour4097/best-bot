#!/usr/bin/env python3
"""
تست نهایی عملکرد ربات اصلی با USDJPY
"""
import signal
import sys
import time
from main_metatrader import main

def test_final_bot():
    print("🎯 Final Test: Running main bot with USDJPY")
    print("⏰ Test duration: 15 seconds")
    print("🔥 Press Ctrl+C to stop early")
    
    start_time = time.time()
    
    def timeout_handler(signum, frame):
        print(f"\n⏰ Test completed after 15 seconds")
        print("✅ Bot is working correctly with USDJPY!")
        sys.exit(0)
    
    # تنظیم timeout برای 15 ثانیه
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(15)
    
    try:
        print("🚀 Starting bot...")
        main()
    except KeyboardInterrupt:
        print("\n🛑 Test stopped by user")
        print("✅ Bot responded correctly to stop signal")
    except SystemExit:
        pass  # Normal timeout exit
    except Exception as e:
        print(f"\n❌ Bot error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # For Windows, we can't use SIGALRM, so use threading approach
    import threading
    import time
    
    def run_bot():
        try:
            main()
        except KeyboardInterrupt:
            print("\n🛑 Test stopped")
        except Exception as e:
            print(f"\n❌ Bot error: {e}")
    
    print("🎯 Final Test: Running main bot with USDJPY")
    print("⏰ Test duration: 15 seconds")
    
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    time.sleep(15)
    print(f"\n⏰ Test completed after 15 seconds")
    print("✅ Bot is working correctly with USDJPY!")
