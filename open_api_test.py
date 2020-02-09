import requests
import json
from jsonschema import validate
from utils.test_data import *
from utils.request_manager import *
from utils.endpoints import *
import pytest


def load_json_schema(filename):
    """ Loads the given schema file """
    path = '/Users/ytatarenko/PycharmProjects/Autotest_practice/utils/json_schemas/' + filename + '.json'
    schema = open(path, 'r')
    json_schema = schema.read()
    return json.loads(json_schema)


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """
    schema = load_json_schema(schema_file)
    return validate(data, schema)


def rerun_test(test, number_of_reruns):
    i = 0
    while i < number_of_reruns:
        test()
        i += 1


@pytest.mark.parametrize('endpoint, schema, user_id, expected_status_code',
                         [
                            (single_user_operations, 'Get_schema_200_single_user', 1, 200),
                            (single_user_operations, 'Get_schema_404', 1000000, 404)
                         ]

                         )
def test_get_single_user(endpoint, schema, user_id, expected_status_code):
    try:
        response = get(endpoint.format(user_id=str(user_id)))
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_single_user(endpoint, schema, user_id, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, params, expected_status_code',
                         [
                            (get_list_of_users, 'Get_schema_200_list_users', {'page': 1}, 200),
                            (get_list_of_users, 'Get_schema_200_list_users_empty', {'page': 1000}, 200)
                         ]

                         )
def test_get_users_list(endpoint, schema, params, expected_status_code):
    try:
        response = get(endpoint, params=params)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_users_list(endpoint, schema, params, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, expected_status_code',
                         [
                            (list_resource, 'Get_schema_200_list_resource', 200)
                         ]

                         )
def test_get_list_resource(endpoint, schema, expected_status_code):
    try:
        response = get(endpoint)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_list_resource(endpoint, schema, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, resource_id, expected_status_code',
                         [
                            (single_record_list_resource, 'Get_schema_200_single_list_resource', 1, 200),
                            (single_record_list_resource, 'Get_schema_404', 1000000, 404)
                         ]

                         )
def test_get_single_resource(endpoint, schema, resource_id, expected_status_code):
    try:
        response = get(endpoint.format(resource_id=str(resource_id)))
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_single_resource(endpoint, schema, resource_id, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, data, expected_status_code',
                         [
                            (single_user_operations, 'Post_schema_201', valid_create_post, 201),
                            (single_user_operations, 'Post_schema_201', valid_create_post_only_name, 201),
                            (single_user_operations, 'Post_schema_201', valid_create_post_only_job, 201),
                            (single_user_operations, 'Post_schema_201', valid_create_post_empty, 201)
                         ]

                         )
def test_create_new_user(endpoint, schema, data, expected_status_code):
    try:
        response = post(endpoint, data=data)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_create_new_user(endpoint, schema, data, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, user_id, data, expected_status_code',
                         [
                            (single_user_operations, 'Update_schema_200', 1, valid_create_post, 200),
                            (single_user_operations, 'Update_schema_200', 10, valid_create_post_only_name, 200),
                            (single_user_operations, 'Update_schema_200', 100, valid_create_post_only_job, 200),
                            (single_user_operations, 'Update_schema_200', 1000, valid_create_post_empty, 200),
                            (single_user_operations, 'Update_schema_200', 10000, valid_create_post_empty, 200)
                         ]

                         )
def test_update_user_put(endpoint, schema, user_id, data, expected_status_code):
    try:
        response = put(endpoint.format(user_id=str(user_id)), data=data)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_update_user_put(endpoint, schema, data, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, user_id, data, expected_status_code',
                         [
                            (single_user_operations, 'Update_schema_200', 1, valid_create_post, 200),
                            (single_user_operations, 'Update_schema_200', 10, valid_create_post_only_name, 200),
                            (single_user_operations, 'Update_schema_200', 100, valid_create_post_only_job, 200),
                            (single_user_operations, 'Update_schema_200', 1000, valid_create_post_empty, 200),
                            (single_user_operations, 'Update_schema_200', 10000, valid_create_post_empty, 200)
                         ]

                         )
def test_update_user_patch(endpoint, schema, user_id, data, expected_status_code):
    try:
        response = patch(endpoint.format(user_id=str(user_id)), data=data)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_update_user_patch(endpoint, schema, data, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, user_id, expected_status_code',
                         [
                            (single_user_operations, 1, 204)
                         ]

                         )
#There is no json schema here because response has an empty body
def test_delete_single_user(endpoint, user_id, expected_status_code):
    try:
        response = delete(endpoint.format(user_id=str(user_id)))
        assert response.status_code == expected_status_code
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_single_user(endpoint, user_id, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, data, expected_status_code',
                         [
                            (registration, 'Post_schema_register_200', valid_register_post, 200),
                            (registration, 'Post_schema_400_only_email', invalid_register_post_only_email, 400),
                            (registration, 'Post_schema_400_only_password', invalid_register_post_only_password, 400),
                            (registration, 'Post_schema_400_only_password', invalid_register_post_empty, 400),
                            (registration, 'Post_schema_register_400_undefined_user', undefined_register_post, 400),
                         ]

                         )
def test_new_user_registration(endpoint, schema, data, expected_status_code):
    try:
        response = post(endpoint, data=data)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_create_new_user(endpoint, schema, data, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, data, expected_status_code',
                         [
                            (registration, 'Login_schema_200', valid_login, 200),
                            (registration, 'Post_schema_400_only_email', login_only_email, 400),
                            (registration, 'Post_schema_400_only_password', login_only_password, 400),
                            (registration, 'Post_schema_400_only_password', login_empty, 400),
                            (registration, 'Post_schema_register_400_undefined_user', invalid_login, 400),
                         ]

                         )
def test_login(endpoint, schema, data, expected_status_code):
    try:
        response = post(login, data=data)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_create_new_user(endpoint, schema, data, expected_status_code), 3)


@pytest.mark.parametrize('endpoint, schema, params, expected_status_code',
                         [
                            (get_list_of_users, 'Get_schema_200_list_users', {'delay': 3}, 200),
                            (get_list_of_users, 'Get_schema_200_list_users', {'delay': 5}, 200)
                         ]

                         )
def test_get_users_list(endpoint, schema, params, expected_status_code):
    try:
        response = get(endpoint, params=params)
        response_json = json.loads(response.text)
        assert response.status_code == expected_status_code
        assert_valid_schema(response_json, schema)
    except requests.exceptions.ConnectionError:
         rerun_test(test_get_users_list(endpoint, schema, params, expected_status_code), 3)