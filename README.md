[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)

# Rewrite a Python Script in Rust

## Goal

> Duke University IDS 706 Weekly Mini Project 8

- Take an existing Python script for data processing
- Rewrite it in Rust
- Highlight improvements in speed and resource usage


## Explanation

Since I have already done the Rust Script in mini project 7, therefore, I implemented the Python script in this project.
Then I compare the performance between Python and Rust.

## Preparation

For the Rust script, please refer to [here](https://github.com/nogibjj/IDS706-MiniProject7-RustScriptCli)

As for the Python script, just use this script.

`python main.py "Your Plaintext" shift`


## Performance Comparison Report

For the comparison, I use the same plaintext and shift number to test the performance.

Meanwhile, I write a script to run the same script 1000 times and 10000 times to get the total elapsed time and resource usage.

|Language|      Run Script 1000 Times       |       Run Script 10000 Times        | Average Resource Usage                                                                                     |
|:---:|:--------------------------------:|:-----------------------------------:|:-----------------------------------------------------------------------------------------------------------|
|Python| Total time elapsed: 18.0 seconds |  Total time elapsed: 187.0 seconds  | User time: 0.02 seconds <br> System time: 0.01 seconds <br> CPU usage: 69% <br> Total time: 0.058 seconds  |
|Rust| Total time elapsed: 2.0 seconds  | Total time elapsed: 14.0 seconds | User time: 0.03 seconds<br> System time: 0.01 seconds <br> CPU usage: 9% <br> Total time: 0.461 seconds    |

Here are some possible explanations for these results:

1. Overhead: The Rust program might have some additional overhead due to the use of the Rust runtime and potentially additional optimizations and checks that Rust provides for safety. In contrast, Python might not have the same level of performance overhead, but it may not be as safe.

2. Compilation: The Rust program is compiled code (with optimizations), while the Python script is interpreted. The Rust compiler can perform various optimizations that can improve runtime performance.

3. CPU Utilization: The Python script utilized more CPU resources (69% vs. 9%) during execution. This could be due to different runtime behaviors, code execution characteristics, or the specific operations performed in each program.

4. Total Time: Despite the higher CPU utilization, the Rust script completed the task more quickly with a lower total time, suggesting that it is more efficient for this specific operation than Python.

It's important to note that these results can vary depending on the specific code, the hardware, and the system load. Rust is known for its performance and safety, but the actual performance can depend on the nature of the task and the quality of the code. In some cases, Rust will significantly outperform Python, while in others, the difference may be less pronounced.

> In addition, my running environment is 
> 
> CPU: Apple M1 Pro 8-Core CPU, 14-Core GPU, 16GB RAM
> 
> OS: macOS Sonoma 14.0
> 
> Different environment may have different results.
> 
> In addition, the Rust or Python may not have fully optimized for Apple chip and macOS 14.

## Reference

1.  https://github.com/nogibjj/python-template
2.  https://github.com/helenyjx/Rust-Powered-Calculator-Microservice-in-the-Cloud

