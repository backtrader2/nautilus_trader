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

from typing import List, Optional

import msgspec

from nautilus_trader.adapters.binance.core.enums import BinanceExchangeFilterType
from nautilus_trader.adapters.binance.core.enums import BinancePermissions
from nautilus_trader.adapters.binance.core.enums import BinanceRateLimitInterval
from nautilus_trader.adapters.binance.core.enums import BinanceRateLimitType
from nautilus_trader.adapters.binance.core.enums import BinanceSpotOrderType
from nautilus_trader.adapters.binance.core.enums import BinanceSymbolFilterType


class BinanceExchangeFilter(msgspec.Struct):
    """Represents a `Binance` exchange filter."""

    filterType: BinanceExchangeFilterType
    maxNumOrders: Optional[int] = None
    maxNumAlgoOrders: Optional[int] = None


class BinanceSymbolFilter(msgspec.Struct):
    """Represents a `Binance` symbol filter."""

    filterType: BinanceSymbolFilterType
    minPrice: Optional[str] = None
    maxPrice: Optional[str] = None
    tickSize: Optional[str] = None
    multiplierUp: Optional[str] = None
    multiplierDown: Optional[str] = None
    avgPriceMins: Optional[int] = None
    bidMultiplierUp: Optional[str] = None
    bidMultiplierDown: Optional[str] = None
    askMultiplierUp: Optional[str] = None
    askMultiplierDown: Optional[str] = None
    minQty: Optional[str] = None
    maxQty: Optional[str] = None
    stepSize: Optional[str] = None
    minNotional: Optional[str] = None
    applyToMarket: Optional[bool] = None
    limit: Optional[int] = None
    maxNumOrders: Optional[int] = None
    maxNumAlgoOrders: Optional[int] = None
    maxNumIcebergOrders: Optional[int] = None
    maxPosition: Optional[str] = None


class BinanceRateLimit(msgspec.Struct):
    """Represents a `Binance` rate limit spec."""

    rateLimitType: BinanceRateLimitType
    interval: BinanceRateLimitInterval
    intervalNum: int
    limit: int


class BinanceSymbolInfo(msgspec.Struct):
    """Represents a `Binance` symbol definition."""

    symbol: str
    status: str
    baseAsset: str
    baseAssetPrecision: int
    quoteAsset: str
    quotePrecision: int
    quoteAssetPrecision: int
    orderTypes: List[BinanceSpotOrderType]
    icebergAllowed: bool
    ocoAllowed: bool
    quoteOrderQtyMarketAllowed: bool
    allowTrailingStop: bool
    isSpotTradingAllowed: bool
    isMarginTradingAllowed: bool
    filters: List[BinanceSymbolFilter]
    permissions: List[BinancePermissions]


class BinanceExchangeInfo(msgspec.Struct):
    """Represents a `Binance` exchange markets information."""

    timezone: str
    serverTime: int
    rateLimits: List[BinanceRateLimit]
    exchangeFilters: List[BinanceExchangeFilter]
    symbols: List[BinanceSymbolInfo]


class BinanceTrade(msgspec.Struct):
    """Represents a `Binance` trade."""

    id: int
    price: str
    qty: str
    quoteQty: str
    time: int
    isBuyerMaker: bool
    isBestMatch: bool