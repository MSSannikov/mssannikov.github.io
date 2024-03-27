
# **What is the receipt lottery?**

The receipt lottery is the free lottery connected to the ITALIA CASHLESS
program developed by the Government to encourage the use of credit
cards, debit cards, debit cards, prepaid cards,cards and apps connected
to private payment circuits and with limited spendability in order to
modernize the country and encourage the development of a more digital,
faster, simpler and more transparent system. The receipt lottery costs
you nothing because it is connected to normal cashless purchases,
purchases made without cash, using electronic payment instruments.

Participating in the lottery is easy: if you are of age and resident in
Italy, obtain the lottery code on this site - in the Participate Now
section - and show it to the merchant at the time of each cashless
purchase. Once this is done, your electronic receipt will give you
virtual tickets to participate in the lottery: a virtual ticket for
every euro spent. For example: if you spend 10 euros you will get 10
virtual tickets, if you spend 45 you will get 45 virtual tickets and so
on up to a maximum of 1,000 virtual tickets for each receipt of an
amount equal to or greater than 1,000 euros; 10 receipts can therefore
get you up to 10,000 virtual tickets, 100 receipts up to 100,000 virtual
tickets and so on. If the amount spent is greater than one euro, any
decimal figure greater than 49 cents will produce another virtual
ticket.

**Do not allow to participate in the lottery:**

-   purchases of less than one euro
-   purchases made online
-   purchases made in the exercise of business

**In the starting phase of the lottery they do not allow to
participate:**

-   purchases documented by electronic invoices

-   purchases for which the fee data is transmitted to the Healthcare
    Card system (for example purchases made at pharmacies,
    parapharmacies, opticians, analysis laboratories, veterinary
    clinics, etc.)

-   purchases for which the buyer requests the merchant to acquire his
    tax code for the purpose of tax deduction or deduction.

Your task is to design a Conceptual, Logical and Physical (ddl) model to
support the application that implement the Lottery.

**Information to be managed includes:**

-   The user that participates in the lottery in terms of Unique code,
    name, surname, fiscal code, gender, birth date, birth
    place, address, email, telephone.

-   The retailer: name of the retailer, legal entity type (Spa, srl, …),
    partita iva, Unique code of the retailer, Retail category, sector,
    address

-   Point of sales: address, city, CAP, size

-   The POS terminal (registratore di cassa): ID_number, Model

-   The receipt includes: receipt unique identifier (per retailer/cash
    machine), type of payment, type_of_transaction (succeed,
    return, cancelled), credit-card number, type of card, purchase
    amount, POS terminal nr, date of purchase

-   Lottery ticket generated: ticket number, reference to the receipt

-   Lottery contest. Each ticket participates to a weekly,
    monthly, yearly  contest extraction of the winner ticket.

-   Prize and prize assignment  

    Moreover design a data warehouse schema to analyze
    data. Specifically, the business stakeholders need to analyze
    potential frauds (i.e. basically anomaly in the average of sales)
