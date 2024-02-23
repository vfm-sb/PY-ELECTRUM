# PY-ELECTRUM Roadmap

<br>
<hr>
<br>

## Py-Electrum Tasks

### General TODOs

- [ ] Support for `Money` Objects without Mandatory `currency` Argument
    - Possibly After Version 2...
    - Plain Money Objects Functionality May Never Be Implemented!
- [ ] Currencies as Classes (For Example: `EUR` Class, `USD` Class, `GBP` Class as Alternative to `Money` with `Currency`)
- [ ] Currency Scraper -- Automatic Currency Builder & Maintainer
- [x] `FMoney` Class for More Advanced Financial Monetary Calculations & Operations.
- [ ] `Exchange` Class for Currency Exchange Operations.
- [x] Flexible **Round-Up** & **Round-Down** Models (Suitable for Different Use Cases)
- [x] Custom **Round-Up** & **Round-Down** Models Support


### TODOs for Expected Internal Changes

- [x] Use `pathlib` Module instead of String-Based Paths
- [ ] Move `data/currencies` into `electrum` Folder
- [x] Formatting Money based on Currencies
- [x] Default Formatting
- [x] Negative Value Formatting Functionality
    - Version 0.2.5 generates correct representations only when positive monetary values are used.
- [ ] Custom Formatting
    - [ ] Basic Custom Formatting Functionality
    - [ ] Predefined Custom Formatting Functionality
- [x] Refactor `Money` & `FMoney` for Future Improvements


### Testing Tasks

**Additional Tests for Money Formatting**:

- [x] Test Japanese Yen or South Korean Won in Different Configurations.
    - Representing Currencies Without Subunits
- [x] Test Different Configurations of a Currency with No Symbol or Abbreviations (CHF & RON).
- [x] Test a Currency with Unit and Subunit Symbols (USD).