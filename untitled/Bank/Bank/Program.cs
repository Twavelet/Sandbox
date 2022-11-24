var trevorsAccount = new Bank.BankAccount("Trevor", 1000);
Console.WriteLine($"A new account ({trevorsAccount.Number}) has been opened for: {trevorsAccount.Owner} with an initial balance of {trevorsAccount.Balance}.");
trevorsAccount.MakeWithdrawal(100, DateTime.Now, "For Hammock");
Console.WriteLine(trevorsAccount.Balance);
