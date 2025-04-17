import Currency from "./3-currency.js";

export default class Pricing extends Currency {
  constructor(amount, currency) {
    this._amount = amount;
	this._currency = currency;
  }
  get getAmount() {
	return this.amount;
  }
  get getCurrency() {
	return this.currency;
  }
  set setAmount(amount) {
	this.amount = amount;
  }
  set setCurrency(currency) {
	this.currency = currency;
  }
  displayFullPrice(pricing) {
    console.log(`${pricing.amount} ${super.name} ${pricing.currency}`);
  }
  convertPrice(amount, conversionRate) {
	return (amount * conversionRate);
  }
}