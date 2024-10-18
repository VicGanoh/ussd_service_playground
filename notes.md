**Flow**:
    1. Receives USSD request with session ID
    2. Retrieves/creates session state from cache
    3. Processes user input based on current state
    4. Updates session state in cache
    5. Returns appropriate response message