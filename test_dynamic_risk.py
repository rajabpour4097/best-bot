#!/usr/bin/env python3
"""
Test script for the new dynamic risk management configuration
"""

from metatrader5_config import DYNAMIC_RISK_CONFIG

def test_dynamic_risk_config():
    """Test the dynamic risk management configuration"""
    print("🧪 Testing Dynamic Risk Management Configuration")
    print("=" * 60)
    
    # Check if enabled
    print(f"Enabled: {DYNAMIC_RISK_CONFIG.get('enable', False)}")
    print(f"Base TP R: {DYNAMIC_RISK_CONFIG.get('base_tp_R', 1.2)}")
    print()
    
    # Check stages
    stages = DYNAMIC_RISK_CONFIG.get('stages', [])
    print(f"Number of stages: {len(stages)}")
    print()
    
    print("Stages Configuration:")
    print("-" * 40)
    for i, stage in enumerate(stages, 1):
        stage_id = stage.get('id', 'unknown')
        trigger_r = stage.get('trigger_R', 'N/A')
        sl_lock_r = stage.get('sl_lock_R', 'N/A')
        tp_r = stage.get('tp_R', 'N/A')
        
        print(f"{i:2d}. {stage_id}")
        print(f"    Trigger: {trigger_r}R -> SL: {sl_lock_r}R, TP: {tp_r}R")
    
    print()
    print("✅ Configuration looks good!")
    
    # Verify sequence is correct
    print("\n🔍 Verifying sequence...")
    expected_triggers = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
    expected_tps = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
    
    for i, stage in enumerate(stages):
        trigger_r = stage.get('trigger_R')
        sl_lock_r = stage.get('sl_lock_R')
        tp_r = stage.get('tp_R')
        
        if trigger_r != expected_triggers[i]:
            print(f"❌ Stage {i+1}: Expected trigger {expected_triggers[i]}R, got {trigger_r}R")
            return False
            
        if sl_lock_r != expected_triggers[i]:
            print(f"❌ Stage {i+1}: Expected SL lock {expected_triggers[i]}R, got {sl_lock_r}R")
            return False
            
        if tp_r != expected_tps[i]:
            print(f"❌ Stage {i+1}: Expected TP {expected_tps[i]}R, got {tp_r}R")
            return False
    
    print("✅ All stages are correctly configured!")
    return True

def simulate_position_progression():
    """Simulate a position going through all stages"""
    print("\n📈 Simulating position progression...")
    print("=" * 60)
    
    stages = DYNAMIC_RISK_CONFIG.get('stages', [])
    
    # Simulate a bullish position
    entry_price = 1.1000
    initial_stop = 1.0950  # 50 pips risk
    risk = entry_price - initial_stop  # 0.0050
    
    print(f"Position Details:")
    print(f"  Entry: {entry_price}")
    print(f"  Initial SL: {initial_stop}")
    print(f"  Risk (1R): {risk:.4f} ({risk * 10000:.0f} pips)")
    print()
    
    # Test each stage
    for stage in stages:
        trigger_r = stage.get('trigger_R')
        sl_lock_r = stage.get('sl_lock_R')
        tp_r = stage.get('tp_R')
        
        # Calculate prices for this stage
        trigger_price = entry_price + (trigger_r * risk)
        new_sl = entry_price + (sl_lock_r * risk)
        new_tp = entry_price + (tp_r * risk)
        
        print(f"Stage {stage.get('id')}:")
        print(f"  Trigger at: {trigger_price:.4f} ({trigger_r}R)")
        print(f"  New SL: {new_sl:.4f} ({sl_lock_r}R)")
        print(f"  New TP: {new_tp:.4f} ({tp_r}R)")
        print(f"  Reward/Risk: {tp_r}:1")
        print()

if __name__ == "__main__":
    success = test_dynamic_risk_config()
    if success:
        simulate_position_progression()
