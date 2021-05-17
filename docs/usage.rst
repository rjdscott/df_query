=====
Usage
=====

To use DFQuery in a project::

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

    dfq.sql(sql_query)
