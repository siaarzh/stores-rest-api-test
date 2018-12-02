pm.environment.unset("jwt_token")

tests["Response time is less than 200ms"] = responseTime < 200;

var jsonData = JSON.parse(responseBody);

tests["User created successfully"] = jsonData.message === 'User created successfully.';
tests["Content-Type is present in response"] = postman.getResponseHeader('Content-Type');
tests["Content-Type is 'application/json'"] = postman.getResponseHeader('Content-Type') === 'application/json';