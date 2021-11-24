import pytest

#from devices.auth0 import Auth0Client
from proxy_flare.services.auth0 import Auth0Client

#def test_get_devices_by_user_id(url_staging, auth_token_staging, customer_id, user_id):
def test_get_devices_by_user_id(auth_token_staging, customer_id, user_id):
    url_staging = "https://devices-staging.electric.ai/staging"

    # Given
    limit = None
    after = None
    filters = {}
    operator = None
    sort = None
    sort_by = None

    # When
    response = DevicesV2API(url_staging, auth_token_staging) \
        .devices(customer_id=customer_id) \
        .assigned_to(user_id=user_id) \
        .limit(limit=limit) \
        .after(after=after) \
        .filter_by(**filters) \
        .filter_by_operator(operator=operator) \
        .order_by(order=sort, order_by=sort_by) \
        .all() \
        .dump()

    # The FE is expecting the devices keyword
    # but we agreed that data is the keyword in the API for returning data.
    response["devices"] = response.pop("data")

    # Then
    assert response['total'] == 1
    assert response['count'] == 1
    assert response['devices'][0]['customer_id'] == customer_id
    assert response['devices'][0]['assigned_to'] == user_id

# jx
@pytest.fixture(name="url_staging", scope="session")
def get_url_staging():
    return "https://devices-staging.electric.ai/staging"



@pytest.fixture(name="auth_token_staging", scope="session")
def get_auth_token_staging():
    # Authentication.
    # This instantiation is using a singleton, thus this is not creating a new object
    auth_client = Auth0Client()
    return auth_client.token
