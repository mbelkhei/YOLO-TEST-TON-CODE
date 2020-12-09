import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class NullImputer(BaseEstimator, TransformerMixin):
    """
    [TO MODIFY]
    impute columns with specific value or strategy

    Example:
    [ADD EXAMPLE]

    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        """
        Fit NullImputer to X.

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
        Transform X.

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
        Fit CategoricalEncoder to X, then transform X.
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
