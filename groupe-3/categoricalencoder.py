import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin



class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """
    [TO MODIFY]
    Apply encoding to categorical variables.
    The input to this transformer should be a pandas.DataFrame. It encodes
    categorical columns with OneHotEncoder or OrdinalEncoder depending on the choosing `strategy`.
    
    Example:
    [ADD EXAMPLE HERE]
    
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        """
        Fit CategoricalEncoder to X.

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
        Transform X using categorical encoding.

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
