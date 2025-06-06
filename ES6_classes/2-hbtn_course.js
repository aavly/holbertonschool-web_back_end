export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof length !== 'number') throw TypeError('length must be a number');
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw TypeError('Students must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof name !== 'string') throw TypeError('name must be a string');
    this._name = name;
  }

  set length(length) {
    if (typeof length !== 'number') throw TypeError('length must be a number');
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = students;
  }
}
