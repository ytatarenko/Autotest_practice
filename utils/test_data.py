valid_create_post = {"name": "morpheus", "job": "leader"}
valid_create_post_only_name = {"name": "morpheus"}
valid_create_post_only_job = {"job": "leader"}
valid_create_post_empty = {}

valid_register_post = {"email": "eve.holt@reqres.in", "password": "pistol"}
undefined_register_post = {"email": "test@test.test", "password": "pistol"} #{"error": "Note: Only defined users succeed registration"}
invalid_register_post_only_password = {"password": "pistol"} #{"error": "Missing email or username"}
invalid_register_post_only_email = {"email": "test@test.test"} #{"error": "Missing password"}
invalid_register_post_empty = {} #{"error": "Missing email or username"}

valid_login = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
invalid_login = {"email": "test@test.test", "password": "pistol"} #{"error": "user not found"}
login_only_email = {"email": "eve.holt@reqres.in"} #{"error": "Missing password"}
login_only_password = {"password": "pistol"} #{"error": "Missing email or username"}
login_empty = {} #{"error": "Missing email or username"}




