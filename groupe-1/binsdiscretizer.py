#finish docstring
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class BinsDiscretizer(BaseEstimator, TransformerMixin):
    """
    [TO MODIFY]
    Create Bins categories for one or more column of a dataframe following
    an automatic bin interval (ie: [1,2,3,4,5,6,7,8,9,10] =auto 2 bins> [1,2,3,4,5], [6,7,8,9,10] ) or specific strategy (ie: AGE < 12 => "kid") 

    Example:
    [ADD EXAMPLE]
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        """
        Fit BinsDiscretizer to X.

        Parameters
        ----------
        X : array-like, shape [n_samples, n_features]
        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`sklearn.pipeline.Pipeline`.

        Returns
        -------
        self
        """
        return self

    def transform(self, X, y=None):
        """
        Transform X using BinsDiscretizer.

        Parameters
        ----------
        X : array-like, shape [n_samples, n_features]
        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`sklearn.pipeline.Pipeline`.

        Returns
        -------
        pd.DataFrame
            Transformed input.
        """

        pass

    def fit_transform(self, X, y=None):
        """
        Fit BinsDiscretizer to X, then transform X.
        Equivalent to fit(X).transform(X) but more convenient.

        Parameters
        ----------
        X : array-like, shape [n_samples, n_features]
        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`sklearn.pipeline.Pipeline`.

        Returns
        -------
        pd.DataFrame
            Transformed input.
        """
        return self.fit(X).transform(X)
