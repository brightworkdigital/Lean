# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from AlgorithmImports import *
from BasicSetAccountCurrencyAlgorithm import BasicSetAccountCurrencyAlgorithm

### <summary>
### Basic algorithm using SetAccountCurrency with an amount
### </summary>
class BasicSetAccountCurrencyWithAmountAlgorithm(BasicSetAccountCurrencyAlgorithm):
    def set_account_currency_and_amount(self):
        # Before setting any cash or adding a Security call SetAccountCurrency
        self.set_account_currency("EUR", 200000)
