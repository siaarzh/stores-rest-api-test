// new Postman format
var jsonData = pm.response.json();
tests["Response time is less than 200ms"] = responseTime < 200;
tests["Status code is 200"] = responseCode.code === 200;
tests["JWT token exist"] = jsonData.access_token !== undefined;

pm.environment.set("jwt_token", jsonData.access_token);

// old Postman format
// var jsonData = JSON.parse(responseBody)
// postman.setEnvironmentVariable("access_token", jsonData.access_token);