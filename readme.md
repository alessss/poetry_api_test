To run tests:
1. Open project in IDE
2. Activate virtual environment
3. Install dependencies pip install -r requirements.txt
4. Click Play button in IDE

Test descriptions
1. test_author_linecount
Test search by author and linecount (positive)
Steps:
- Request data by author and number of lines for few combinations (positive)
Expected result: 
- Response code is 200 - to validate that request works fine
- Each request returns in response exact amount of poems in database - to validate that return
is idempotent
- Actual line number (excluding empty lines) equals to number of lines in poem object - to compare 
actual line numbers calculated in the test with numbers from DB

2. test_author_not_exist 
Test search return no result
Steps:
- Request data by author using string which is not in any of author's name (e.g. Abcefg)
Expected result:
- Response code is 200 - to validate that request works fine
- Return value is {"status":404,"reason":"Not found"} - to validate return text

3. test_search_by_partial_name
Test ssearch by partial author's name
Steps:
- Request data by author using one uppercase letter
- Request data by author using combination of uppercase and lowercase letter
- Request data by author using three uppercase letters
Expected result:
- Response code is 200 - to validate that request works fine
- Verify that search string is in each returned poem's author name (regardless of case) - check that
search is case-insensitive and it returns expected data
- Verify that each request returns at least 2 different authors - testdata is constructed in a way,
that we can receive more than one author in each request
   
    
