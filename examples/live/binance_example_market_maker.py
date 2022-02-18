#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2022 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from decimal import Decimal

from nautilus_trader.adapters.binance.factories import BinanceLiveDataClientFactory
from nautilus_trader.adapters.binance.factories import BinanceLiveExecutionClientFactory
from nautilus_trader.examples.strategies.volatility_market_maker import VolatilityMarketMaker
from nautilus_trader.examples.strategies.volatility_market_maker import VolatilityMarketMakerConfig
from nautilus_trader.infrastructure.config import CacheDatabaseConfig
from nautilus_trader.live.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode


# *** THIS IS A TEST STRATEGY WITH NO ALPHA ADVANTAGE WHATSOEVER. ***
# *** IT IS NOT INTENDED TO BE USED TO TRADE LIVE WITH REAL MONEY. ***

# *** THIS INTEGRATION IS STILL UNDER CONSTRUCTION. ***
# *** PLEASE CONSIDER IT TO BE IN AN UNSTABLE BETA PHASE AND EXERCISE CAUTION. ***

# Configure the trading node
config_node = TradingNodeConfig(
    trader_id="TESTER-001",
    log_level="INFO",
    cache_database=CacheDatabaseConfig(),
    data_clients={
        "BINANCE": {
            # "api_key": "YOUR_BINANCE_API_KEY",
            # "api_secret": "YOUR_BINANCE_API_SECRET",
            "account_type": "spot",
            "base_url_http": None,
            "base_url_ws": None,
            "us": False,  # If client is for Binance US
            "sandbox_mode": True,  # If client uses the testnet
        },
    },
    exec_clients={
        "BINANCE": {
            # "api_key": "YOUR_BINANCE_API_KEY",
            # "api_secret": "YOUR_BINANCE_API_SECRET",
            "account_type": "spot",
            "base_url_http": None,
            "base_url_ws": None,
            "us": False,  # If client is for Binance US
            "sandbox_mode": True,  # If client uses the testnet,
        },
    },
    timeout_connection=5.0,
    timeout_reconciliation=5.0,
    timeout_portfolio=5.0,
    timeout_disconnection=5.0,
    check_residuals_delay=2.0,
)
# Instantiate the node with a configuration
node = TradingNode(config=config_node)

# Configure your strategy
strat_config = VolatilityMarketMakerConfig(
    instrument_id="ETHUSDT.BINANCE",
    bar_type="ETHUSDT.BINANCE-1-MINUTE-LAST-EXTERNAL",
    atr_period=20,
    atr_multiple=6.0,
    trade_size=Decimal("0.01"),
)
# Instantiate your strategy
strategy = VolatilityMarketMaker(config=strat_config)

# Add your strategies and modules
node.trader.add_strategy(strategy)

# Register your client factories with the node (can take user defined factories)
node.add_data_client_factory("BINANCE", BinanceLiveDataClientFactory)
node.add_exec_client_factory("BINANCE", BinanceLiveExecutionClientFactory)
node.build()


# Stop and dispose of the node with SIGINT/CTRL+C
if __name__ == "__main__":
    try:
        node.start()
    finally:
        node.dispose()