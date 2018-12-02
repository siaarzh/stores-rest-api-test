var jsonData = JSON.parse(responseBody);
tests["Message returned"] = jsonData.message === 'Item deleted';

tests["Success code"] = responseCode.code === 200;
tests["Response time is less than 200ms"] = responseTime < 200;

tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
tests["Content-Type is 'application/json'"] = postman.getResponseHeader("Content-Type") === 'application/json';