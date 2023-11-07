# NVISH_Exercise

1. **Exercise 1:** create a simple API listener / server process that can
respond to unauthenticated `/ping` calls. Be prepared to discuss any
framework decisions you make during the interview
2. **Exercise 2:** Come up with a method that can be used for
authentication using pre-shared secrets that can be added to the header
of the request. Create an `/authorize` endpoint for the API that will
authorize the header against a pre-shared key that can be loaded as a
secret when the API starts
3. **Exercise 3:** Assume that you will be reading from a database (use
`sqlite` for this exercise). Create an endpoint called `/save` that
allows POSTING of a key / value pair into a database table.
* Create another endpoint that allows the user to `/get` the data from
the database
* Create a final endpoint that removes the data from the database
`/delete`
4. **Exercise 4:** Employ a caching mechanism for your application to
speed up operations on `/save` and `/get`. Be prepared to discuss /
defend your choice and approach

5. **Exercise 5:** Write test cases (unit and end-to-end) that verify
both the operation and business logic you may have written. Assume the
tests will use `pytest` and be prepared to discuss testing topics in
general.
