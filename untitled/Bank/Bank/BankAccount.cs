using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bank
{
    internal class BankAccount
    {
        //properties/characteristics (what a bank account has) and what they can do -- "get" == get them & "set" means you cna set them later on
        public string Number { get; }
        public string Owner { get; set; }
        public decimal Balance { 
            get {
                decimal balance = 0;
                foreach (var item in transactionList)
                {
                    balance += item.Amount;
                }
                return balance;
            }
        }

        private int accountNumberSeed = 123456;

        private List<Transaction> transactionList = new List<Transaction>();

        public BankAccount(string name, decimal initialBalance)
        {
            this.Owner = name;
            MakeDeposit(initialBalance, DateTime.Now, "Initial deposit");
            this.Number = accountNumberSeed.ToString();
            accountNumberSeed++;

        }

        //Methods -- what the Bank Account can do
        public void MakeDeposit(decimal amount, DateTime date, string note)
        {
            if (amount <= 0)
            {
                throw new ArgumentOutOfRangeException(nameof(amount), "Insufficient amount. The deposit has to be positive.");
            }
            var deposit = new Transaction(amount , date, note);
            transactionList.Add(deposit);
        }

        public void MakeWithdrawal(decimal amount, DateTime date, string note)
        {

            if (amount <= 0)
            {
                throw new ArgumentOutOfRangeException(nameof(amount), "Withdrawal amount must be positive.");

            }

            if (Balance - amount < 0)
            {
                throw new InvalidOperationException("Not enough funds to make this withdrawal");
            }
            var withdrawal = new Transaction(-amount , date, note);
            transactionList.Add(withdrawal);
            
        }

    }
}
