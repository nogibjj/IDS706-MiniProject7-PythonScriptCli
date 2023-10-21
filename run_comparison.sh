#!/bin/bash

# Record the start time
start_time=$(date +%s.%N)

# Run the Python program 1000 times
for i in {1..10000}; do
    python main.py "Hello World" 3 > /dev/null
done

# Record the end time
end_time=$(date +%s.%N)

# Calculate the total elapsed time
elapsed_time=$(echo "$end_time - $start_time" | bc)

echo "Total time elapsed: $elapsed_time seconds"
