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
from enum import Enum
from typing import Any, Dict, Iterable, Type

from pydantic import BaseModel, create_model


class JSModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True

        @classmethod
        def schema_extra(cls, schema: Dict[str, Any], model: Type["BaseModel"]) -> None:
            schema.pop("title", None)
            schema.pop("description", None)
            for name, prop in schema.get("properties", {}).items():
                prop.pop("title", None)
                prop.pop("description", None)
                allow_none = model.__fields__[name].allow_none
                if "type" in prop:
                    if allow_none:
                        prop["type"] = ["null", prop["type"]]


class JSEnum(str, Enum):
    @classmethod
    def __modify_schema__(cls, schema):
        schema.pop("title", None)
        schema.pop("description", None)


class MetricsReport(JSModel):
    profileId: int
    recordType: str
    reportDate: str
    # This property will be overwritten with autogenerated model based on metrics list
    metric: None

    @classmethod
    def generate_metric_model(cls, metric_list: Iterable[str]) -> JSModel:
        metrics_obj_model = create_model("MetricObjModel", **{f: (str, None) for f in metric_list}, __base__=JSModel)
        return create_model("MetricsModel", metric=(metrics_obj_model, None), __base__=cls)


class State(JSEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    ARCHIVED = "archived"


class ExpressionType(JSEnum):
    MANUAL = "manual"
    AUTO = "auto"


class Targeting(JSModel):
    targetId: Decimal
    adGroupId: Decimal
    state: State
    expressionType: ExpressionType
    expression: str
    resolvedExpression: str
    bid: Decimal


class KeywordsBase(JSModel):
    keywordId: Decimal
    campaignId: Decimal
    adGroupId: Decimal
    state: State
    keywordText: str


class MatchType(JSEnum):
    EXACT = "exact"
    PHRASE = "phrase"
    BROAD = "broad"


class Keywords(KeywordsBase):
    nativeLanguageKeyword: str
    matchType: MatchType
    bid: Decimal


class NegativeMatchType(JSEnum):
    NEGATIVE_EXACT = "negativeExact"
    NEGATIVE_PHRASE = "negativePhrase"


class NegativeKeywords(KeywordsBase):
    matchType: NegativeMatchType
