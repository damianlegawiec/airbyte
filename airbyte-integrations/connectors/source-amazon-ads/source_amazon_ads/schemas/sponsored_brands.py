#
# MIT License
#
# Copyright (c) 2020 Airbyte
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from decimal import Decimal
from typing import Dict

from .common import JSEnum, JSModel, State


class BudgetType(JSEnum):
    LIFETIME = "lifetime"
    DAILY = "daily"


class ServingStatus(JSEnum):
    ASIN_NOT_BUYABLE = "asinNotBuyable"
    BILLING_ERROR = "billingError"
    ENDED = "ended"
    LANDING_PAGE_NOT_AVAILABLE = "landingPageNotAvailable"
    OUT_OF_BUDGET = "outOfBudget"
    PAUSED = "paused"
    PENDING_REVIEW = "pendingReview"
    READY = "ready"
    REJECTED = "rejected"
    RUNNING = "running"
    SCHEDULED = "scheduled"
    TERMINATED = "terminated"


class AdFormat(JSEnum):
    PRODUCT_COLLECTION = "productCollection"
    VIDEO = "video"


class BrandsCampaign(JSModel):
    campaignId: Decimal
    name: str
    tags: Dict[str, str]
    budget: Decimal
    budgetType: BudgetType
    startDate: str
    endDate: str
    state: State
    servingStatus: ServingStatus
    brandEntityId: str
    portfolioId: Decimal
    landingPage: str
    bidOptimization: bool = None
    bidMultiplier: Decimal = None
    adFormat: AdFormat
    creative: str


class BrandsAdGroup(JSModel):
    campaignId: Decimal
    adGroupId: Decimal
    name: str
