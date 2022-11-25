var trevorsAccount = new Bank.BankAccount("Trevor", 1000);
Console.WriteLine($"A new account '{trevorsAccount.accountNumber}' has been opened for: {trevorsAccount.Owner} with an initial balance of {trevorsAccount.Balance}.");
trevorsAccount.MakeWithdrawal(100, DateTime.Now, "For Hammock");
Console.WriteLine(trevorsAccount.Balance);
trevorsAccount.MakeDeposit(100, DateTime.Now, "Tips");
Console.Write(trevorsAccount.GetAccountHistory());