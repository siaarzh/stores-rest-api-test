var jsonData = JSON.parse(responseBody);
tests["Store 'books' returned"] = jsonData.stores[0].name === 'books';
tests["ID of 'books' store returned"] = jsonData.stores[0].id === parseInt(environment.store_id);
tests["Item 'alice' name is returned in 'books' store"] = jsonData.stores[0].items[0].name === 'alice';
tests["Item 'alice' price is returned in 'books' store"] = jsonData.stores[0].items[0].price === 19.99;

tests["Response time is less than 200ms"] = responseTime < 200;

tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
tests["Content-Type is 'application/json'"] = postman.getResponseHeader("Content-Type") === 'application/json';