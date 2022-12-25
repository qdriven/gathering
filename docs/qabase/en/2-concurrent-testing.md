# concurrency testing

What is concurrency testing?

Concurrency testing is a type of software testing that checks the performance of software when multiple users are logged in and perform actions simultaneously. Hence, it is also referred to as multi-user testing.

Concurrency testing is challenging to conduct compared to sequential testing, due to the following three problems:

- synchronization problems
- non-determinism
- time-related defects difficult to detect

Concurrency testing mainly monitors the system for deadlocking, locking, and single-threaded code.

Concurrent testing methods
Some common methods for performing concurrency testing include the following:
- Fuzz Test: The tester inserts incorrect random data and monitors the system’s response.
- Random Test: Multiple strands are tested simultaneously by randomizing the test inputs.
- Code Review: The testers verify the code and its structures.
- Static Analysis: The tester checks the coding system before the code’s execution.

Advantages
Some benefits of concurrency testing include the following:

Disadvantages
Some drawbacks of concurrency testing include the following:


What is Concurrency Testing?
‘Concurrency testing is a technique used to detect possible defects while multiple users log into an application simultaneously. Testing a concurrent program is more complex than trying a regular sequential program due to the synchronization problems.‘

Let us understand concurrency testing through an example:

Many of us make use of eCommerce websites such as Amazon to do online shopping. There comes a situation when multiple users log in to the website simultaneously and end up ordering the same product.

This requires maintaining the order in separate accounts without any confusion. So testing the behavior of the software at that very moment is concurrency testing. 

End-to-End Testing on real iOS, Android Devices & Browsers
Start Free Testing
1 4
Why Concurrency Testing is Important?
Concurrency testing is usually done for two reasons

1. How multiple user access at the same time affects the running process of a database or an application.

2. Determines how deadlocking, locking, single-threaded code, and constraining affect the resources that are shared.

 Advantages of Concurrency Testing:
Here is a list of advantages of the concurrent testing of an application:

●  It significantly decreases the effort for testing an application or database as it restricts the scope of general concurrent communication lines.

●  One can review just a fragment of the code without disturbing the whole code with the help of a specific value named encapsulation value.

●  After checking the processes of a concurrent program, it is updated with the reliability and vigor of the application.

Disadvantages of Concurrency Testing:
There are a few disadvantages or drawbacks of running a concurrent test on any application or database.

●  There is no special platform since very few development steps are taken during concurrent testing. Due to this unoptimized situation, multiple outlets are required to perform that whenever simultaneous testing is done.

●  Since concurrent programs are challenging to test, the defects are hard to find without a vigorous test.

●  Concurrent testing is highly time-consuming. The results of the operating functions on any part of the code do not return the outcome immediately. Instead, the result is returned later through a sort of notification or a separately designed callback function.

●  Without proper information representation of the flow of the actual program in the call stack, it is difficult to detect the defects. Thus, defragmenting the testing process.

●  There is an interconnection of all the concurrent systems that merge and interact with themselves while the program execution process is on. Thus, controlling the contemporary process becomes difficult as the interaction of the systems produces multiple paths of execution.

●  Concurrent programs have a reputation of failing more often than regular sequential programs.

●  Due to the multiple paths of execution, debugging the program becomes very troublesome.

Concurrency Testing Techniques:
Concurrency testing
Let us know different types of concurrency testing techniques

●  Reviewing Code- This process is quite time-consuming. Because you need to review and check every block of embedded code and its subsequent structure thoroughly.

●  Static Analysis- This is a standard process to evaluate and check the code thoroughly evaluated and checked before the final execution process. This process aims to determine bugs and errors of any sort in the program.

●  Con Testing- This method eliminates unwanted synchronization errors from a particular program, hence reducing running deficiencies.

●  Reachability Testing- This type of testing requires a lot of subtests in its follow-up. Hence, you need to select some precisely verified codes for reachability testing.

●  Fuzz Testing- This is a random test where the user deliberately inserts wrong codes to see how the program’s execution reacts.

●  Random Testing- This is a valuable method to test multiple threads mandatorily to improve the quality of the results. Hence it has a vast coverage area.

●   Extending Concolic Testing- This type of testing is suitable for multiple concurrent programs and numerous sequential programs. It is easily expandable in size and helps a lot.

 Types of Concurrency Defects:
Let’s discuss specific types of concurrency defects in detail below

●  Deadlock: This is a specific failure condition where the code stops working due to the deficiency of a particular resource. Here one of the components is locked by another one and vice versa. For example, a defect caused by two components does not move forward until the resource is free to use.

●  Livelock: A failure condition where a concurrent component never finishes its execution process due to the lack of necessary resources termed as the high-priority component.

●  Starvation: In this particular failure condition where the concurrent component has to wait indefinitely for its execution to complete because some other component occupies the resource it needs.

●  Suspension: It is a failure condition where the concurrent component is forced to wait for so long that when the resource is available to share, the execution cannot happen properly due to the delay.

●  Race Condition: Race condition is a failure condition where too many operations can lead to unexpected and inappropriate behavior of the system. This usually happens when you do not appropriately authorize the resources, and there is excessive access to them. The simultaneous errors can lead to the corruption of the whole system.

●  Priority Inversion: It is an unwanted failure condition that is first served for the low-priority concurrent component. Then before executing a high-priority concurrent component leading to disruption of the whole process.

Conclusion:

To summarise, all these above points elucidate that concurrency testing needs development and optimization of the highest sort in itself to be better used in the future.

But at the same time, it is also one of the effective techniques used by businesses to streamline operations in a better manner. 


As the name suggests, Concurrency means two or more events happening at the same time. Similarly, concurrence testing is done to identify how the application will be affected when multiple users are logged in at the same time and doing the same action. Concurrency Testing is also known as multi-user testing.

When multiple users are performing the same action at the same time then there can be issues like increased response time, application crashes etc. which are detected by concurrence testing. Concurrence testing helps improving reliability and robustness of concurrent programs. Concurrent programs run a number of the program at the same time and involved in sharing information. The sharing of information controls the order of execution of tasks. If there is any change in the sequence of execution of these processes then it produces incorrect results which result in repeatability of error. Concurrent testing ensures the reliability of concurrent programs. A real-time example of concurrency is: Trains running on the different track at the same time or train running in same track at different timings.
 

Concurrency Testing Process:
Creating a plan for concurrent testing.
Analyzing the plan and defining scope.
Creating a High level and low-level scenarios for concurrent testing.
Creating the environment for testing.
Now, testers two or more testers can begin the testing by performing the same task at the same timings.

In load runner, a Rendezvous point is used to create concurrency. The tester can create a scenario after recording and enhancing script in Visual User Generator. In the controller component of load runner, the tester can add a number of concurrent users.

All the users involved in the testing can wait at the same point (For example Login Button), all the users can press the login button at the same time. (Rendezvous point).

These days due to increase in a number of internet users, there is a possibility that a web server may be handling many different clients at the same time, in such types of situation server can go to a deadlock state as it is handling multiple users at the same point. To make sure this flow should go smooth and there should be no deadlock, concurrency testing is done.

 

Concurrency Testing Techniques:
Reviewing code: In this process embedded code and their structures are checked. This is a time-consuming process.
Static Analysis: Static analysis is used for checking and evaluating coding system before executing the code. It is useful in detecting bugs and errors in the system.
Con Testing: Contest removes synchronization faults in multithreaded java program. The contest also notes the deficiencies in unit testing.
Reachability Testing: Reachability testing is usually not possible for many applications as it needs large subtests. There are some proposed research programs to make reachability testing more useful for concurrent testing.
Fuzz Testing: In this testing, user feeds random incorrect data and then wait to see how the program responds. There is no logic behind fuzz testing, it is more of a guess where bad data is provided to crash a program.
Random testing: Coverage area is increased by randomizing test inputs. Multiple threads are tested at one time. For better results, 5-10 threads should be tested at a time.
Extending concolic testing: This can be used for testing multi-threaded or concurrent programs. This type of testing is easily extendable and expendable with flipping algorithms. Without an extension, concolic testing is effective for testing sequential program.
 

Key Challenges in Concurrency Testing:
The test case creation for Concurrency Testing is time-consuming and a very tough job which requires the regular help of the developers.
During concurrent testing, there are very high chances that new errors are introduced in code.
Concurrent testing needs to be done on different platforms.
This testing is more difficult as function return their results via notifications or call back functions instead of delivering immediately.
Debugging of the concurrent program.
The ratio of failure of Concurrency Testing is much more than the sequential program.
Most of the defects are time related and difficult to reproduce.
 

Over to you:
Concurrency Testing – To check the effect on the system when multiple users are logged in performing the same task at the same time.
Help in removing robustness of concurrent programs.
Used to detect issues like deadlock, increased response time, application crashes.

## References

- [testgrid](https://www.testgrid.io/blog/concurrency-testing/)
- [software-testing-conceptions](https://www.tutorialspoint.com/software_testing_dictionary/concurrency_testing.htm)
