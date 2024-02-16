"""
Tests for Money Formatter
"""

# Local Modules
from electrum import Money


class TestMoneyFormatter:

    def test_eur_name_format(self):
        euro_sp = Money(1, "eur")
        assert euro_sp.name_format() == "1 Euro"
        euro_sn = Money(-1, "eur")
        assert euro_sn.name_format() == "-1 Euro"
        euro_hp = Money(100, "eur")
        assert euro_hp.name_format() == "100 Euros"
        euro_hn = Money(-20, "eur")
        assert euro_hn.name_format() == "-20 Euros"
        euro_bp = Money(0.01, "eur")
        assert euro_bp.name_format() == "1 Cent"
        euro_bn = Money(-0.01, "eur")
        assert euro_bn.name_format() == "-1 Cent"
        euro_lp = Money(0.42, "eur")
        assert euro_lp.name_format() == "42 Cents"
        euro_ln = Money(-0.42, "eur")
        assert euro_ln.name_format() == "-42 Cents"

    def test_bgn_name_format(self):
        leva_sp = Money(1, "bgn")
        assert leva_sp.name_format() == "1 Lev"
        leva_sn = Money(-1, "bgn")
        assert leva_sn.name_format() == "-1 Lev"
        leva_hp = Money(100, "bgn")
        assert leva_hp.name_format() == "100 Leva"
        leva_hn = Money(-20, "bgn")
        assert leva_hn.name_format() == "-20 Leva"
        leva_bp = Money(0.01, "bgn")
        assert leva_bp.name_format() == "1 Stotinka"
        leva_bn = Money(-0.01, "bgn")
        assert leva_bn.name_format() == "-1 Stotinka"
        leva_lp = Money(0.42, "bgn")
        assert leva_lp.name_format() == "42 Stotinki"
        leva_ln = Money(-0.42, "bgn")
        assert leva_ln.name_format() == "-42 Stotinki"

    def test_try_name_format(self):
        lira_sp = Money(1, "try")
        assert lira_sp.name_format() == "1 Lira"
        lira_sn = Money(-1, "try")
        assert lira_sn.name_format() == "-1 Lira"
        lira_hp = Money(100, "try")
        assert lira_hp.name_format() == "100 Lira"
        lira_hn = Money(-20, "try")
        assert lira_hn.name_format() == "-20 Lira"
        lira_bp = Money(0.01, "try")
        assert lira_bp.name_format() == "1 Kuruş"
        lira_bn = Money(-0.01, "try")
        assert lira_bn.name_format() == "-1 Kuruş"
        lira_lp = Money(0.42, "try")
        assert lira_lp.name_format() == "42 Kuruş"
        lira_ln = Money(-0.42, "try")
        assert lira_ln.name_format() == "-42 Kuruş"

    def test_eur_symbol_format(self):
        euro_sp = Money(1, "eur")
        assert euro_sp.symbolize == "€1"
        euro_sn = Money(-1, "eur")
        assert euro_sn.symbolize == "-€1"
        euro_hp = Money(100, "eur")
        assert euro_hp.symbolize == "€100"
        euro_hn = Money(-20, "eur")
        assert euro_hn.symbolize == "-€20"
        euro_bp = Money(0.01, "eur")
        assert euro_bp.symbolize == "1c"
        euro_bn = Money(-0.01, "eur")
        assert euro_bn.symbolize == "-1c"
        euro_lp = Money(0.42, "eur")
        assert euro_lp.symbolize == "42c"
        euro_ln = Money(-0.42, "eur")
        assert euro_ln.symbolize == "-42c"

    def test_bgn_symbol_format(self):
        leva_sp = Money(1, "bgn")
        assert leva_sp.symbolize == "1лв."
        leva_sn = Money(-1, "bgn")
        assert leva_sn.symbolize == "-1лв."
        leva_hp = Money(100, "bgn")
        assert leva_hp.symbolize == "100лв."
        leva_hn = Money(-20, "bgn")
        assert leva_hn.symbolize == "-20лв."
        leva_bp = Money(0.01, "bgn")
        assert leva_bp.symbolize == "1ст."
        leva_bn = Money(-0.01, "bgn")
        assert leva_bn.symbolize == "-1ст."
        leva_lp = Money(0.42, "bgn")
        assert leva_lp.symbolize == "42ст."
        leva_ln = Money(-0.42, "bgn")
        assert leva_ln.symbolize == "-42ст."

    def test_try_symbol_format(self):
        lira_sp = Money(1, "try")
        assert lira_sp.symbolize == "₺1"
        lira_sn = Money(-1, "try")
        assert lira_sn.symbolize == "-₺1"
        lira_hp = Money(100, "try")
        assert lira_hp.symbolize == "₺100"
        lira_hn = Money(-20, "try")
        assert lira_hn.symbolize == "-₺20"
        lira_bp = Money(0.01, "try")
        assert lira_bp.symbolize == "1kr."
        lira_bn = Money(-0.01, "try")
        assert lira_bn.symbolize == "-1kr."
        lira_lp = Money(0.42, "try")
        assert lira_lp.symbolize == "42kr."
        lira_ln = Money(-0.42, "try")
        assert lira_ln.symbolize == "-42kr."

    def test_eur_abbr_format(self):
        euro_sp = Money(1, "eur")
        assert euro_sp.abbreviate == "€1"
        euro_sn = Money(-1, "eur")
        assert euro_sn.abbreviate == "-€1"
        euro_hp = Money(100, "eur")
        assert euro_hp.abbreviate == "€100"
        euro_hn = Money(-20, "eur")
        assert euro_hn.abbreviate == "-€20"
        euro_bp = Money(0.01, "eur")
        assert euro_bp.abbreviate == "1c"
        euro_bn = Money(-0.01, "eur")
        assert euro_bn.abbreviate == "-1c"
        euro_lp = Money(0.42, "eur")
        assert euro_lp.abbreviate == "42c"
        euro_ln = Money(-0.42, "eur")
        assert euro_ln.abbreviate == "-42c"
