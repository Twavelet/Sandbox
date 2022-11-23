using System;
using System.Collections.Generic;

for (int i = 0; i < 101; i++)
{
    if (i % 3 == 0 && i % 5 == 0)
    {
        Console.WriteLine("FizzBuzz");
    }
    else if (i % 3 == 0)
    {
        Console.WriteLine("Fizz");
    }
    else if (i % 5 == 0)
    {
        Console.WriteLine("Buzz");
    }
    else
        Console.WriteLine(i);
}

int counter = 0;
int counter1 = 0;

while (counter <= 5)
{
    Console.WriteLine($"Counter is {counter}");
    counter++;
}

do
{
    Console.WriteLine($"Incrementing until {counter1} hits its upper boundary");
    counter1++;
} 
while (counter1 <= 5);

var names = new List<string> { "tim", "tam", "tun", "ten" };

foreach (var name in names)
{
    Console.WriteLine(name);
}


var fibonacci = new List<int> { };
Console.WriteLine(fibonacci.Count);

do
{
    if (fibonacci.Count == 0)
    {
        fibonacci.Add(0);
        fibonacci.Add(1);
        fibonacci.Add(1);
    }
    else if (fibonacci.Count >= 3)
    {
        fibonacci.Add(fibonacci[fibonacci.Count - 1] + fibonacci[fibonacci.Count - 2]);
        Console.WriteLine(fibonacci[fibonacci.Count-1]);
    }
}
while (fibonacci.Count <= 20);
Console.WriteLine($"The first 20 numbers of the Fibonacci sequence: [{string.Join(",", fibonacci)}].");

