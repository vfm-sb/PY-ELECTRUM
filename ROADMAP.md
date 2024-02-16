# PY-ELECTRUM Roadmap

- [ ] Support for `Money` Objects without Mandatory `currency` Argument
    - Possibly After Version 2...
    - Plain Money Objects Functionality May Never Be Implemented!
- [ ] Currencies as Classes (For Example: `EUR` Class, `USD` Class, `GBP` Class as Alternative to `Money` with `Currency`)
- [ ] Currency Scraper -- Automatic Currency Builder & Maintainer
- [x] `FMoney` Class for More Advanced Financial Monetary Calculations & Operations.
- [ ] `Exchange` Class for Currency Exchange Operations.
- [x] Flexible **Round-Up** & **Round-Down** Models (Suitable for Different Use Cases)
- [x] Custom **Round-Up** & **Round-Down** Models Support


## Internal Changes

- [x] Use `pathlib` Module instead of String-Based Paths
- [ ] Move `data/currencies` into `electrum` Folder
- [x] Formatting Money based on Currencies
- [x] Default Formatting
- [x] Custom Formatting
- [ ] Refactor `Money` & `FMoney` for Future Improvements


## TODO

- [x] Negative Value Formatting Functionality
    - Version 0.2.5 generates correct representations only when positive monetary values are used.
- [x] Basic Custom Formatting Functionality
- [x] Predefined Custom Formatting Functionality

