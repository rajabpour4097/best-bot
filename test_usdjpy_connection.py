#!/usr/bin/env python3
"""
تست اتصال MT5 و نماد USDJPY
"""
import MetaTrader5 as mt5
from mt5_connector import MT5Connector
from metatrader5_config import MT5_CONFIG

def test_usdjpy_connection():
    print("🔄 Testing USDJPY connection...")
    
    # نمایش تنظیمات فعلی
    print(f"📊 Current symbol: {MT5_CONFIG['symbol']}")
    print(f"📊 Lot size: {MT5_CONFIG['lot_size']}")
    print(f"📊 Magic number: {MT5_CONFIG['magic_number']}")
    
    # ایجاد connector
    mt5_conn = MT5Connector()
    
    # تست initialize
    if not mt5_conn.initialize():
        print("❌ Failed to initialize MT5")
        return False
    
    print("✅ MT5 initialized successfully")
    
    # تست اطلاعات نماد
    print(f"\n🔍 Checking {MT5_CONFIG['symbol']} symbol info...")
    info = mt5.symbol_info(MT5_CONFIG['symbol'])
    if not info:
        print(f"❌ Symbol {MT5_CONFIG['symbol']} not found")
        mt5_conn.shutdown()
        return False
    
    print(f"✅ Symbol info retrieved:")
    print(f"   - Name: {info.name}")
    print(f"   - Description: {info.description}")
    print(f"   - Point: {info.point}")
    print(f"   - Digits: {info.digits}")
    print(f"   - Spread: {info.spread}")
    print(f"   - Min volume: {info.volume_min}")
    print(f"   - Max volume: {info.volume_max}")
    print(f"   - Volume step: {info.volume_step}")
    print(f"   - Visible: {info.visible}")
    
    # اگر نماد مرئی نیست، آن را فعال کن
    if not info.visible:
        print("🔄 Making symbol visible...")
        mt5.symbol_select(MT5_CONFIG['symbol'], True)
    
    # تست دریافت قیمت لحظه‌ای
    print(f"\n💹 Getting live price for {MT5_CONFIG['symbol']}...")
    price_data = mt5_conn.get_live_price()
    if price_data:
        print(f"✅ Live price retrieved:")
        print(f"   - Bid: {price_data['bid']}")
        print(f"   - Ask: {price_data['ask']}")
        print(f"   - Spread: {price_data['spread']:.1f} points")
        print(f"   - Time (Iran): {price_data['time']}")
    else:
        print("❌ Failed to get live price")
        mt5_conn.shutdown()
        return False
    
    # تست دریافت داده تاریخی
    print(f"\n📈 Getting historical data for {MT5_CONFIG['symbol']}...")
    hist_data = mt5_conn.get_historical_data(count=10)
    if hist_data is not None and len(hist_data) > 0:
        print(f"✅ Historical data retrieved:")
        print(f"   - Records count: {len(hist_data)}")
        print(f"   - Last close: {hist_data['close'].iloc[-1]}")
        print(f"   - Last time: {hist_data.index[-1]}")
    else:
        print("❌ Failed to get historical data")
        mt5_conn.shutdown()
        return False
    
    # تست بررسی وضعیت معاملات
    print(f"\n⏰ Checking trading conditions...")
    can_trade, message = mt5_conn.can_trade()
    print(f"   - Can trade: {can_trade}")
    print(f"   - Message: {message}")
    
    # تست اطلاعات حساب
    print(f"\n💰 Account information...")
    acc = mt5.account_info()
    if acc:
        print(f"   - Login: {acc.login}")
        print(f"   - Balance: {acc.balance}")
        print(f"   - Equity: {acc.equity}")
        print(f"   - Currency: {acc.currency}")
        print(f"   - Trading allowed: {acc.trade_allowed}")
    
    # بررسی filling modes
    print(f"\n🔧 Testing filling modes...")
    filling_modes = mt5_conn.get_supported_filling_modes()
    print(f"   - Supported filling modes: {filling_modes}")
    
    mt5_conn.shutdown()
    print("\n✅ All tests completed successfully!")
    return True

if __name__ == "__main__":
    try:
        success = test_usdjpy_connection()
        if success:
            print("\n🎉 USDJPY connection test PASSED")
        else:
            print("\n❌ USDJPY connection test FAILED")
    except Exception as e:
        print(f"\n💥 Error during test: {e}")
        import traceback
        traceback.print_exc()
