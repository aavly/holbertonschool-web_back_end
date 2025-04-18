export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(newCode) {
    this.code = newCode;
  }

  set name(newName) {
    this.name = newName;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
