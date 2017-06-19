# -*- coding: utf-8 -*-
"""

Author
------
Bo Zhang

Email
-----
bozhang@nao.cas.cn

Created on
----------
- Mon Sep 05 12:00:00 2016

Modifications
-------------
- Mon Sep 05 12:00:00 2016

Aims
----
- SVR hyper-parameters

"""

import numpy as np
from astropy.table import Table
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV


__all__ = ['summarize_hyperparameters_to_table', 'summarize_table']


def summarize_hyperparameters_to_table(svrs):
    """ summarize hyper-parameters as a Table

    Parameters
    ----------
    svrs: list of sklearn.svm.SVR objects
        a list of fitted SVR objets

    """
    hyperparams = []
    for svr in svrs:
        if isinstance(svr, SVR):
            hyperparams.append((svr.C, svr.gamma, svr.epsilon))
        elif isinstance(svr, GridSearchCV):
            hyperparams.append((svr.best_estimator_.C,
                                svr.best_estimator_.gamma,
                                svr.best_estimator_.epsilon))
    hp_array = np.array(hyperparams)
    return Table(data=hp_array, names=['C', 'gamma', 'epsilon'])


def summarize_table(hpt):
    """ summarize table data

    Parameters
    ----------
    hpt: astropy.table.Table
        a table of parameter

    """

    # simply use pandas.DataFrame.describe()
    print(hpt.to_pandas().describe())

    return
