# pyfortnox
python client for using Fortnox API

## Install package
`pip install pyfortnox`

### Usage
`import fortnox`

`client = fortnox.Client(access_token='Your-Access-Token', client_secret='Your-Client-Secret')`
# Get you necessary services
`customers = client.customers.list()` // <client>.<desired_service_name>.<option>
# Access the data by access/period with attribute name
`for customer in customers:`
    `print(customer.Name)`
