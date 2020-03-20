# fortnox-python
REST client for using Fortnox API

### Usage
`import fortnox`

`client = fortnox.Client(access_token='Your-Access-Token', client_secret='Your-Client-Secret')`
`customers = client.customers.list()` # <client>.<desired_service_name>.<option>
`for customer in customers:`
    `print(customer.Name)`