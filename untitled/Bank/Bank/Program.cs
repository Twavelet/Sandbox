using System;

var trevorsAccount = new Bank.BankAccount("Trevor", 1000);
Console.WriteLine($"A new account has been opened for: {trevorsAccount.Owner} with an initial balance of {trevorsAccount.Balance}.");
