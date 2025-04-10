export default function createEmployeesObject(departmentName, employees) {
  const employeeList = employees.map((name) => `'${name}'`).join(', ');

  return `{ ${departmentName}: [ ${employeeList} ]}`;
}
