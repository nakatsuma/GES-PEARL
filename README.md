# GES-PEARL <!-- omit in toc -->

## Course materials for GENERAL EDUCATION SEMINAR (PEARL) <!-- omit in toc -->

Teruo Nakatsuma (Faculty of Economics, Keio University, Japan)

---

- [How to set up Python and necessary packages](#how-to-set-up-python-and-necessary-packages)
  - [Step 1: Installing Anaconda](#step-1-installing-anaconda)
  - [Step 2: (Windows only) Installing Microsoft Visual Studio Build Tools](#step-2-windows-only-installing-microsoft-visual-studio-build-tools)
  - [Step 3: Creating an environment](#step-3-creating-an-environment)
- [How to start JupyterLab](#how-to-start-jupyterlab)
  - [Method 2: From Anaconda Navigator](#method-2-from-anaconda-navigator)
- [-->](#)
- [Jupyter Notebooks and related files in `notebook`](#jupyter-notebooks-and-related-files-in-notebook)
- [Python codes and related files in `python`](#python-codes-and-related-files-in-python)

---

## How to set up Python and necessary packages

I strongly recommend using [Anaconda](https://www.anaconda.com/). It can install Python along with numerous essential packages at once and allows us to manage those packages flexibly.

### Step 1: Installing Anaconda

1. If you have an older Anaconda on your PC, uninstall it completely by folloiwng [instructions](https://docs.anaconda.com/anaconda/install/uninstall/).

2. Download an Anaconda installer (Windows, macOS or Linux) from [here](https://www.anaconda.com/distribution/). Choose a Python 3 installer.

3. Doubleclick the installer and follow the instructions on the screen. Do not change the default settings.

### Step 2: (Windows only) Installing Microsoft Visual Studio Build Tools

1. Download the installer for Microsoft Visual Studio Build Tools from [here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16).

2. Doubleclick the installer and follow the instructions on the screen. It is sufficient to install `C++ build tools`. See [this link](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view?usp=sharing) for the install instructions.

### Step 3: Creating an environment

Start `Anaconda Powershell Prompt` (Windows) or `Terminal` (macOS, Linux) and type

```IPython
(base) PS C:\Users\Thomas> conda update conda
```

This will update conda (package manager) in Anaconda. Then type

```IPython
(base) PS C:\Users\Thomas> conda create -n finance python=3.7 jupyterlab seaborn spyder nodejs nose
```

This will create a new enviromnemt named `finance`. Then type

```IPython
(base) PS C:\Users\Thomas> conda activate finance
```

You will notice that the prompt is altered as

```IPython
(finance) PS C:\Users\Thomas>
```

To install CVXPY, type

```IPython
(finance) PS C:\Users\Thomas> pip install cvxpy
```

To check whether CVXPY is installed without errors, type
```IPython
(finance) PS C:\Users\Thomas> nosetests cvxpy
```
If no error message appears, CVXPY is properly installed. Finally type

```IPython
(finance) PS C:\Users\Thomas> python -m ipykernel install --user --name finance --display-name "Python (Finance)"
```

Now you are ready for Python!

---

## How to start JupyterLab

<!---
### Method 1: From the command line
-->

Start `Anaconda Powershell Prompt` (Windows) or `Terminal` (macOS, Linux) and type

```IPython
(base) PS C:\Users\Thomas> conda activate finance
```

Then type

```IPython
(finance) PS C:\Users\Thomas> jupyter lab
```

Your default browser will pop up. Click the `Python (Finance)` button to create a Jupyter notebook.

![Anaconda Navigator](Screenshot-JupyterLab.png)

<!---
### Method 2: From Anaconda Navigator

Start `Anaconda Navigator`. You may find it in `Start Menu` (Windows) or `Launchpad` (macOS). Alternatively you just type

```IPython
(base) PS C:\Users\Thomas> anaconda-navigator
```

in `Anaconda Powershell Prompt` (Windows) or `Terminal` (macOS, Linux).

Click the `Launch` button in the `JupyterLab` panel.

![Anaconda Navigator](Screenshot-AnacondaNavigator.png)
-->
---

## Jupyter Notebooks and related files in `notebook`

| file name | description |
|:-------------------------------|:-------------------------------------------|
| asset_return_data.csv          | simulated asset returns                    |
| capm.csv                       | market capitalization data                 |
| ges_alt_risk.ipynb             | portfolio with alternative risk measures   |
| ges_bond.ipynb                 | yield, duration and convexity of bond      |
| ges_interst.ipynb              | interest rate                              |
| ges_mvf_riskfree.ipynb         | mean-variance portfolio w/ risk-free asset |
| ges_mvf_sample.ipynb           | mean-variance portfolio with data          |
| ges_mvf.ipynb                  | mean-variance portfolio                    |
| ges_npv_irr.ipynb              | present value, internal rate of return     |
| ges_portfolio.ipynb            | introduction to portfolio analysis         |
| ges_riskparity.ipybn           | risk parity portfolio                      |
| ges_shortselling.py            | mean-variance portfolio w/o short selling  |
| ges_tracking_error.py          | traking error minimization problem         |
| stock_market_cap.csv           | market capitalization data                 |

---

## Python codes and related files in `python`

| file name | description |
|:-------------------------------|:-------------------------------------------|
| asset_return_data.csv          | simulated asset returns                    |
| capm.csv                       | market capitalization data                 |
| ges_ad_portfolio_ver1.py       | mean absolute deviation portfolio          |
| ges_ad_portfolio.py            | compatible with old CVXPY                  |
| ges_asset_return_simulation.py | simulation of asset returns                |
| ges_black_scholes.py           | Black-Scholes formula for option pricing   |
| ges_bond_duration_convexity.py | duration and convexity of bond             |
| ges_bond_yield_curve.py        | yield curve of bond                        |
| ges_bond_yield_price.py        | price-yield relationship                   |
| ges_capm.py                    | CAPM beta estimation                       |
| ges_es_portfolio_ver1.py       | expected shortfall portfolio               |
| ges_es_portfolio.py            | compatible with old CVXPY                  |
| ges_interest.py                | interest rate                              |
| ges_min_tracking_error_ver1.py | tracking-error minimization                |
| ges_min_tracking_error.py      | compatible with old CVXPY                  |
| ges_mvf_example1.py            | mean-variance portfolio                    |
| ges_mvf_example2_ver1.py       | mean-variance portfolio w/o short selling  |
| ges_mvf_example2.py            | compatible with old CVXPY                  |
| ges_mvf_example3_ver1.py       | mean-variance portfolio with data          |
| ges_mvf_example3.py            | compatible with old CVXPY                  |
| ges_npv_irr.py                 | present value, internal rate of return     |
| ges_option_pricing.py          | option pricing with binomial tree model    |
| ges_risk_parity.py             | risk parity portfolio                      |
| ges_sv_portfolio_ver1.py       | semivariance portfolio                     |
| ges_sv_portfolio.py            | compatible with old CVXPY                  |

---
