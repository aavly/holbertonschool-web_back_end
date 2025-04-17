export default class Currency {
  constructor(code, name) {
    this._code = code;
	this._name = name;
  }
  set setCode(code) {
    this.code = code;
  }
  set setName(name) {
    this.name = name;
  }
  get getCode() {
    return this.code;
  }
  get getName() {
    return this.name;
  }
  displayFullCurrency(currency) {
    return currency.code, currency.name;
  }
}


