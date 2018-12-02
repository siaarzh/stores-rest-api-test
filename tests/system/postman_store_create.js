var jsonData = JSON.parse(responseBody);
tests["Store name returned"] = jsonData.name === 'books';
tests["Store id returned"] = jsonData.id === 1;
tests["Store items are an empty list"] = jsonData.items.length === 0;

tests["Successful POST request"] = responseCode.code === 201;
tests["Response time is less than 200ms"] = responseTime < 200;

tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
tests["Content-Type is 'application/json'"] = postman.getResponseHeader("Content-Type") === 'application/json';

postman.setEnvironmentVariable("store_id", jsonData.id);