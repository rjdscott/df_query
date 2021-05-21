=======
DFQuery
=======


.. image:: https://img.shields.io/pypi/v/df_query.svg
        :target: https://pypi.python.org/pypi/df_query

.. image:: https://travis-ci.com/rjdscott/df_query.svg?branch=main
    :target: https://travis-ci.com/rjdscott/df_query

.. image:: https://readthedocs.org/projects/df-query/badge/?version=latest
        :target: https://df-query.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A Pandas DataFrame SQL Query Utility


* Free software: MIT license
* Documentation: https://df-query.readthedocs.io.

Getting started
_______________

Pip install the package

.. code-block:: console

    $ pip install df_query

To use DFQuery in a project

.. code-block:: python

    from df_query import QueryContext

    # by default the database will be stored in memory
    dfq = QueryContext()

    # OR if you want to persist you can specify a path on local disk
    dfq = query_context('path/to/data.sqlite')

    customer_data = {
        'id':[1,2,3,4],
        'name': ['Boris', 'Bobby', 'Judit']
    }

    order_data = {
        'id':[1,2,3,4,5,6],
        'customer_id':[1,2,1,3,3,1],
        'amount':[10,20,32,12,33,25]
    }
    customer_df = pd.DataFrame(customer_data)
    order_df =pd.DataFrame(order_data)

    # now we create the views in the db
    dfq.create_view(customer_df,'customers')
    dfq.create_view(order_df,'orders')

    # now we can construct the query and return another df
    sql_query = """
                select
                    c.name,
                    sum(o.amount)
                from customers c
                join orders o on o.customer_id = c.id
                group by c.name
                """
    
    # create a dataframe from the sql query
    df = dfq.sql(sql_query)
    print(df)
    
    # delete database if stored on disk
    df1.db_cleanup()



Features
--------

* use SparkSQL-like functinality with your pandas dataframes
* create temporary views and join them using SQL
* use in-memory sqliteDB or persist to disk

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
