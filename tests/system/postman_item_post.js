var jsonData = JSON.parse(responseBody);
tests["Item name returned"] = jsonData.name === 'alice';
tests["Item price returned"] = jsonData.price === 19.99;

tests["Successful POST request"] = responseCode.code === 201;
tests["Response time is less than 200ms"] = responseTime < 200;

tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
tests["Content-Type is 'application/json'"] = postman.getResponseHeader("Content-Type") === 'application/json';