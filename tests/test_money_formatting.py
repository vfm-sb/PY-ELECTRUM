"""
Tests for Money Formatter
"""

# Local Modules
from electrum import Money


class TestMoneyFormatter:

    def test_eur_default_format(self):
        euro_sp = Money(1, "eur")
        assert str(euro_sp) == "€1"
        euro_sn = Money(-1, "eur")
        assert str(euro_sn) == "-€1"
        euro_hp = Money(100, "eur")
        assert str(euro_hp) == "€100"
        euro_hn = Money(-20, "eur")
        assert str(euro_hn) == "-€20"
        euro_bp = Money(0.01, "eur")
        assert str(euro_bp) == "1c"
        euro_bn = Money(-0.01, "eur")
        assert str(euro_bn) == "-1c"
        euro_lp = Money(0.42, "eur")
        assert str(euro_lp) == "42c"
        euro_ln = Money(-0.42, "eur")
        assert str(euro_ln) == "-42c"

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

    def test_eur_symbol_format(self):
        euro_sp = Money(1, "eur")
        assert euro_sp.symbol_format() == "€1"
        euro_sn = Money(-1, "eur")
        assert euro_sn.symbol_format() == "-€1"
        euro_hp = Money(100, "eur")
        assert euro_hp.symbol_format() == "€100"
        euro_hn = Money(-20, "eur")
        assert euro_hn.symbol_format() == "-€20"
        euro_bp = Money(0.01, "eur")
        assert euro_bp.symbol_format() == "1c"
        euro_bn = Money(-0.01, "eur")
        assert euro_bn.symbol_format() == "-1c"
        euro_lp = Money(0.42, "eur")
        assert euro_lp.symbol_format() == "42c"
        euro_ln = Money(-0.42, "eur")
        assert euro_ln.symbol_format() == "-42c"

    def test_eur_abbr_format(self):
        euro_sp = Money(1, "eur")
        assert euro_sp.abbr_format() == "€1"
        euro_sn = Money(-1, "eur")
        assert euro_sn.abbr_format() == "-€1"
        euro_hp = Money(100, "eur")
        assert euro_hp.abbr_format() == "€100"
        euro_hn = Money(-20, "eur")
        assert euro_hn.abbr_format() == "-€20"
        euro_bp = Money(0.01, "eur")
        assert euro_bp.abbr_format() == "1c"
        euro_bn = Money(-0.01, "eur")
        assert euro_bn.abbr_format() == "-1c"
        euro_lp = Money(0.42, "eur")
        assert euro_lp.abbr_format() == "42c"
        euro_ln = Money(-0.42, "eur")
        assert euro_ln.abbr_format() == "-42c"

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

    def test_bgn_symbol_format(self):
        leva_sp = Money(1, "bgn")
        assert leva_sp.symbol_format() == "1лв."
        leva_sn = Money(-1, "bgn")
        assert leva_sn.symbol_format() == "-1лв."
        leva_hp = Money(100, "bgn")
        assert leva_hp.symbol_format() == "100лв."
        leva_hn = Money(-20, "bgn")
        assert leva_hn.symbol_format() == "-20лв."
        leva_bp = Money(0.01, "bgn")
        assert leva_bp.symbol_format() == "1ст."
        leva_bn = Money(-0.01, "bgn")
        assert leva_bn.symbol_format() == "-1ст."
        leva_lp = Money(0.42, "bgn")
        assert leva_lp.symbol_format() == "42ст."
        leva_ln = Money(-0.42, "bgn")
        assert leva_ln.symbol_format() == "-42ст."

    def test_bgn_abbr_format(self):
        leva_sp = Money(1, "bgn")
        assert leva_sp.abbr_format() == "1lv."
        leva_sn = Money(-1, "bgn")
        assert leva_sn.abbr_format() == "-1lv."
        leva_hp = Money(100, "bgn")
        assert leva_hp.abbr_format() == "100lv."
        leva_hn = Money(-20, "bgn")
        assert leva_hn.abbr_format() == "-20lv."
        leva_bp = Money(0.01, "bgn")
        assert leva_bp.abbr_format() == "1st."
        leva_bn = Money(-0.01, "bgn")
        assert leva_bn.abbr_format() == "-1st."
        leva_lp = Money(0.42, "bgn")
        assert leva_lp.abbr_format() == "42st."
        leva_ln = Money(-0.42, "bgn")
        assert leva_ln.abbr_format() == "-42st."

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

    def test_try_symbol_format(self):
        lira_sp = Money(1, "try")
        assert lira_sp.symbol_format() == "₺1"
        lira_sn = Money(-1, "try")
        assert lira_sn.symbol_format() == "-₺1"
        lira_hp = Money(100, "try")
        assert lira_hp.symbol_format() == "₺100"
        lira_hn = Money(-20, "try")
        assert lira_hn.symbol_format() == "-₺20"
        lira_bp = Money(0.01, "try")
        assert lira_bp.symbol_format() == "1kr."
        lira_bn = Money(-0.01, "try")
        assert lira_bn.symbol_format() == "-1kr."
        lira_lp = Money(0.42, "try")
        assert lira_lp.symbol_format() == "42kr."
        lira_ln = Money(-0.42, "try")
        assert lira_ln.symbol_format() == "-42kr."

    def test_try_abbr_format(self):
        lira_sp = Money(1, "try")
        assert lira_sp.abbr_format() == "1 TL"
        lira_sn = Money(-1, "try")
        assert lira_sn.abbr_format() == "-1 TL"
        lira_hp = Money(100, "try")
        assert lira_hp.abbr_format() == "100 TL"
        lira_hn = Money(-20, "try")
        assert lira_hn.abbr_format() == "-20 TL"
        lira_bp = Money(0.01, "try")
        assert lira_bp.abbr_format() == "1kr."
        lira_bn = Money(-0.01, "try")
        assert lira_bn.abbr_format() == "-1kr."
        lira_lp = Money(0.42, "try")
        assert lira_lp.abbr_format() == "42kr."
        lira_ln = Money(-0.42, "try")
        assert lira_ln.abbr_format() == "-42kr."

    def test_usd_symbol_format(self):
        dollar_sp = Money(1, "usd")
        assert dollar_sp.symbol_format() == "$1"
        dollar_sn = Money(-1, "usd")
        assert dollar_sn.symbol_format() == "-$1"
        dollar_hp = Money(100, "usd")
        assert dollar_hp.symbol_format() == "$100"
        dollar_hn = Money(-20, "usd")
        assert dollar_hn.symbol_format() == "-$20"
        dollar_bp = Money(0.01, "usd")
        assert dollar_bp.symbol_format() == "1¢"
        dollar_bn = Money(-0.01, "usd")
        assert dollar_bn.symbol_format() == "-1¢"
        dollar_lp = Money(0.42, "usd")
        assert dollar_lp.symbol_format() == "42¢"
        dollar_ln = Money(-0.42, "usd")
        assert dollar_ln.symbol_format() == "-42¢"

    def test_usd_abbr_format(self):
        dollar_sp = Money(1, "usd")
        assert dollar_sp.abbr_format() == "$1"
        dollar_sn = Money(-1, "usd")
        assert dollar_sn.abbr_format() == "-$1"
        dollar_hp = Money(100, "usd")
        assert dollar_hp.abbr_format() == "$100"
        dollar_hn = Money(-20, "usd")
        assert dollar_hn.abbr_format() == "-$20"
        dollar_bp = Money(0.01, "usd")
        assert dollar_bp.abbr_format() == "1¢"
        dollar_bn = Money(-0.01, "usd")
        assert dollar_bn.abbr_format() == "-1¢"
        dollar_lp = Money(0.42, "usd")
        assert dollar_lp.abbr_format() == "42¢"
        dollar_ln = Money(-0.42, "usd")
        assert dollar_ln.abbr_format() == "-42¢"

    def test_jpy_name_format(self):
        yen_scp = Money(1, "jpy")
        assert yen_scp.name_format() == "1 Yen"
        yen_scn = Money(-1, "jpy")
        assert yen_scn.name_format() == "-1 Yen"
        yen_hcp = Money(500, "jpy")
        assert yen_hcp.name_format() == "500 Yen"
        yen_hcn = Money(-500, "jpy")
        assert yen_hcn.name_format() == "-500 Yen"
        yen_snp = Money(1000, "jpy")
        assert yen_snp.name_format() == "1000 Yen"
        yen_snn = Money(-1000, "jpy")
        assert yen_snn.name_format() == "-1000 Yen"
        yen_hnp = Money(20000, "jpy")
        assert yen_hnp.name_format() == "20000 Yen"
        yen_hnn = Money(-20000, "jpy")
        assert yen_hnn.name_format() == "-20000 Yen"

    def test_jpy_symbol_format(self):
        yen_scp = Money(1, "jpy")
        assert yen_scp.symbol_format() == "¥1"
        yen_scn = Money(-1, "jpy")
        assert yen_scn.symbol_format() == "-¥1"
        yen_hcp = Money(500, "jpy")
        assert yen_hcp.symbol_format() == "¥500"
        yen_hcn = Money(-500, "jpy")
        assert yen_hcn.symbol_format() == "-¥500"
        yen_snp = Money(1000, "jpy")
        assert yen_snp.symbol_format() == "¥1000"
        yen_snn = Money(-1000, "jpy")
        assert yen_snn.symbol_format() == "-¥1000"
        yen_hnp = Money(20000, "jpy")
        assert yen_hnp.symbol_format() == "¥20000"
        yen_hnn = Money(-20000, "jpy")
        assert yen_hnn.symbol_format() == "-¥20000"

    def test_jpy_abbr_format(self):
        yen_scp = Money(1, "jpy")
        assert yen_scp.abbr_format() == "¥1"
        yen_scn = Money(-1, "jpy")
        assert yen_scn.abbr_format() == "-¥1"
        yen_hcp = Money(500, "jpy")
        assert yen_hcp.abbr_format() == "¥500"
        yen_hcn = Money(-500, "jpy")
        assert yen_hcn.abbr_format() == "-¥500"
        yen_snp = Money(1000, "jpy")
        assert yen_snp.abbr_format() == "¥1000"
        yen_snn = Money(-1000, "jpy")
        assert yen_snn.abbr_format() == "-¥1000"
        yen_hnp = Money(20000, "jpy")
        assert yen_hnp.abbr_format() == "¥20000"
        yen_hnn = Money(-20000, "jpy")
        assert yen_hnn.abbr_format() == "-¥20000"

    def test_chf_default_format(self):
        franc_sp = Money(1, "chf")
        assert str(franc_sp) == "CHF 1"
        franc_sn = Money(-1, "chf")
        assert str(franc_sn) == "-CHF 1"
        franc_hp = Money(100, "chf")
        assert str(franc_hp) == "CHF 100"
        franc_hn = Money(-20, "chf")
        assert str(franc_hn) == "-CHF 20"
        franc_bp = Money(0.01, "chf")
        assert str(franc_bp) == "CHF 0.01"
        franc_bn = Money(-0.01, "chf")
        assert str(franc_bn) == "-CHF 0.01"
        franc_lp = Money(0.42, "chf")
        assert str(franc_lp) == "CHF 0.42"
        franc_ln = Money(-0.42, "chf")
        assert str(franc_ln) == "-CHF 0.42"

    def test_chf_name_format(self):
        franc_sp = Money(1, "chf")
        assert franc_sp.name_format() == "1 Franc"
        franc_sn = Money(-1, "chf")
        assert franc_sn.name_format() == "-1 Franc"
        franc_hp = Money(100, "chf")
        assert franc_hp.name_format() == "100 Francs"
        franc_hn = Money(-20, "chf")
        assert franc_hn.name_format() == "-20 Francs"
        franc_bp = Money(0.01, "chf")
        assert franc_bp.name_format() == "1 Centime"
        franc_bn = Money(-0.01, "chf")
        assert franc_bn.name_format() == "-1 Centime"
        franc_lp = Money(0.42, "chf")
        assert franc_lp.name_format() == "42 Centimes"
        franc_ln = Money(-0.42, "chf")
        assert franc_ln.name_format() == "-42 Centimes"

    def test_chf_symbol_format(self):
        franc_sp = Money(1, "chf")
        assert franc_sp.symbol_format() == "1 Franc"
        franc_sn = Money(-1, "chf")
        assert franc_sn.symbol_format() == "-1 Franc"
        franc_hp = Money(100, "chf")
        assert franc_hp.symbol_format() == "100 Francs"
        franc_hn = Money(-20, "chf")
        assert franc_hn.symbol_format() == "-20 Francs"
        franc_bp = Money(0.01, "chf")
        assert franc_bp.symbol_format() == "1 Centime"
        franc_bn = Money(-0.01, "chf")
        assert franc_bn.symbol_format() == "-1 Centime"
        franc_lp = Money(0.42, "chf")
        assert franc_lp.symbol_format() == "42 Centimes"
        franc_ln = Money(-0.42, "chf")
        assert franc_ln.symbol_format() == "-42 Centimes"

    def test_chf_abbr_format(self):
        franc_sp = Money(1, "chf")
        assert franc_sp.abbr_format() == "1 Franc"
        franc_sn = Money(-1, "chf")
        assert franc_sn.abbr_format() == "-1 Franc"
        franc_hp = Money(100, "chf")
        assert franc_hp.abbr_format() == "100 Francs"
        franc_hn = Money(-20, "chf")
        assert franc_hn.abbr_format() == "-20 Francs"
        franc_bp = Money(0.01, "chf")
        assert franc_bp.abbr_format() == "1 Centime"
        franc_bn = Money(-0.01, "chf")
        assert franc_bn.abbr_format() == "-1 Centime"
        franc_lp = Money(0.42, "chf")
        assert franc_lp.abbr_format() == "42 Centimes"
        franc_ln = Money(-0.42, "chf")
        assert franc_ln.abbr_format() == "-42 Centimes"

    def test_ron_default_format(self):
        ron_sp = Money(1, "ron")
        assert str(ron_sp) == "1 Leu"
        ron_sn = Money(-1, "ron")
        assert str(ron_sn) == "-1 Leu"
        ron_hp = Money(100, "ron")
        assert str(ron_hp) == "100 Lei"
        ron_hn = Money(-20, "ron")
        assert str(ron_hn) == "-20 Lei"
        ron_bp = Money(0.01, "ron")
        assert str(ron_bp) == "1 Ban"
        ron_bn = Money(-0.01, "ron")
        assert str(ron_bn) == "-1 Ban"
        ron_lp = Money(0.42, "ron")
        assert str(ron_lp) == "42 Bani"
        ron_ln = Money(-0.42, "ron")
        assert str(ron_ln) == "-42 Bani"

    def test_ron_name_format(self):
        ron_sp = Money(1, "ron")
        assert ron_sp.name_format() == "1 Leu"
        ron_sn = Money(-1, "ron")
        assert ron_sn.name_format() == "-1 Leu"
        ron_hp = Money(100, "ron")
        assert ron_hp.name_format() == "100 Lei"
        ron_hn = Money(-20, "ron")
        assert ron_hn.name_format() == "-20 Lei"
        ron_bp = Money(0.01, "ron")
        assert ron_bp.name_format() == "1 Ban"
        ron_bn = Money(-0.01, "ron")
        assert ron_bn.name_format() == "-1 Ban"
        ron_lp = Money(0.42, "ron")
        assert ron_lp.name_format() == "42 Bani"
        ron_ln = Money(-0.42, "ron")
        assert ron_ln.name_format() == "-42 Bani"

    def test_ron_symbol_format(self):
        ron_sp = Money(1, "ron")
        assert ron_sp.symbol_format() == "1 Leu"
        ron_sn = Money(-1, "ron")
        assert ron_sn.symbol_format() == "-1 Leu"
        ron_hp = Money(100, "ron")
        assert ron_hp.symbol_format() == "100 Lei"
        ron_hn = Money(-20, "ron")
        assert ron_hn.symbol_format() == "-20 Lei"
        ron_bp = Money(0.01, "ron")
        assert ron_bp.symbol_format() == "1 Ban"
        ron_bn = Money(-0.01, "ron")
        assert ron_bn.symbol_format() == "-1 Ban"
        ron_lp = Money(0.42, "ron")
        assert ron_lp.symbol_format() == "42 Bani"
        ron_ln = Money(-0.42, "ron")
        assert ron_ln.symbol_format() == "-42 Bani"

    def test_ron_abbr_format(self):
        ron_sp = Money(1, "ron")
        assert ron_sp.abbr_format() == "1 Leu"
        ron_sn = Money(-1, "ron")
        assert ron_sn.abbr_format() == "-1 Leu"
        ron_hp = Money(100, "ron")
        assert ron_hp.abbr_format() == "100 Lei"
        ron_hn = Money(-20, "ron")
        assert ron_hn.abbr_format() == "-20 Lei"
        ron_bp = Money(0.01, "ron")
        assert ron_bp.abbr_format() == "1 Ban"
        ron_bn = Money(-0.01, "ron")
        assert ron_bn.abbr_format() == "-1 Ban"
        ron_lp = Money(0.42, "ron")
        assert ron_lp.abbr_format() == "42 Bani"
        ron_ln = Money(-0.42, "ron")
        assert ron_ln.abbr_format() == "-42 Bani"
