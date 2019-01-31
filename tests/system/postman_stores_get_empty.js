var jsonData = JSON.parse(responseBody);
tests["List of stores returned"] = jsonData.stores.isEmpty();

tests["Response time is less than 200ms"] = responseTime < 200;

tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
tests["Content-Type is 'application/json'"] = postman.getResponseHeader("Content-Type") === 'application/json';